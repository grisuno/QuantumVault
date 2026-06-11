from pydantic import BaseModel
from typing import Optional
from flask_login import UserMixin
import sqlite3
from datetime import datetime, timedelta, timezone
import pytz

class UserModel(BaseModel, UserMixin):
    """Pydantic model for a user with Flask-Login support.

    Attributes:
        id: Unique user ID.
        username: Unique username.
        role: User role (free, bronze, silver, gold, admin, superadmin).
        email: User's email address.
        phone: User's phone number.
        first_name: User's first name.
        last_name: User's last name.
        storage_quota: Storage quota in bytes.
        trial_start: Trial period start date.
        trial_end: Trial period end date.
        subscription_status: Subscription status (active, inactive).
        email_verified: Whether the email is verified.
        confirmation_token: Email confirmation token.
        phone_verified: Whether the phone number is verified.
        phone_verification_code_hash: Peppered hash of the phone verification code.
        phone_code_expires: Phone verification code expiration.
        mfa_code_hash: Peppered hash of the current MFA code.
        mfa_code_expires: MFA code expiration.
        mfa_enabled: Whether MFA is enabled for the user.
    """
    id: Optional[int] = None
    username: str
    role: str = "free"
    email: Optional[str] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    storage_quota: int = 10 * 1024 * 1024  # Default 10MB
    trial_start: Optional[datetime] = None
    trial_end: Optional[datetime] = None
    subscription_status: str = "active"
    email_verified: bool = False
    confirmation_token: str = ""
    phone_verified: bool = False
    phone_verification_code_hash: Optional[str] = None
    phone_code_expires: Optional[datetime] = None
    mfa_code_hash: Optional[str] = None
    mfa_code_expires: Optional[datetime] = None
    mfa_enabled: bool = False

    def get_id(self) -> str:
        """Return the user ID as a string (required by Flask-Login).

        Returns:
            str: The user ID as a string, or an empty string when the
                user is anonymous.
        """
        return str(self.id) if self.id else ""

    # ``is_authenticated`` and ``is_anonymous`` are provided by
    # ``UserMixin`` and depend on whether the instance is a real
    # authenticated user (``is_authenticated`` -> True) or the
    # ``AnonymousUser`` sentinel (``is_authenticated`` -> False,
    # ``is_anonymous`` -> True). Do not override them: a class-level
    # ``return True`` makes every UserModel look like an authenticated
    # user to downstream consumers and breaks ``current_user`` checks.

    @property
    def is_active(self) -> bool:
        """Return True while the user can use the application.

        Inactive (lapsed-subscription) users can still sign in to renew
        or download their data, so we do NOT tie this to
        ``subscription_status``. The previous implementation returned
        False for inactive users, which logged them out of every
        @login_required route. Subscription-gated features should
        check ``subscription_status`` directly in the view that needs
        the gate, not via Flask-Login's activation hook.
        """
        return True

class UserDB:
    """Database operations for users."""
    def __init__(self, db_path: str):
        """Initialize the UserDB with the database path.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._init_db()

    # Columns that the v7 KEM-based auth schema carried as NOT NULL BLOBs.
    # They are no longer used (v8 is zero-knowledge SRP-6a) but if a pre-v8
    # database is opened, their NOT NULL constraint will reject every insert
    # because the v8 controller never writes them. The migration in
    # _init_db() rebuilds the table and drops these.
    _LEGACY_DROP_COLUMNS = (
        'password_ciphertext',
        'password_secret_key',
        'password_ciphertext_kem',
    )

    def _init_db(self) -> None:
        """Initialize the users table with all fields for zero-knowledge auth.

        The table stores only zero-knowledge credential material: the SRP salt
        and verifier (the password itself is never received), the user's public
        key, the password-encrypted private key blob, and the key-derivation
        salt used to protect that blob. The server can decrypt none of it.

        Phone verification codes and MFA codes are stored as peppered
        SHA-256 digests (``*_code_hash`` columns) instead of plaintext so
        a database dump does not hand an attacker ready-to-use codes.

        The ``phone`` column is not unique: phone numbers are recycled by
        carriers and SIM-swap attacks invalidate the uniqueness guarantee
        anyway. ``email`` remains unique because it is the primary
        recovery identity.

        If the table was created by an older v7 schema (which carried
        NOT NULL KEM blob columns the v8 controller never writes),
        migrate in place: rebuild the table under the v8 shape and preserve
        the surviving identity columns. The legacy password blobs are
        intentionally dropped: v7 ciphertexts are useless without the
        matching v7 KEM code path that has been removed.
        """
        with sqlite3.connect(self.db_path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                srp_salt TEXT,
                srp_verifier TEXT,
                public_key TEXT,
                encrypted_private_key TEXT,
                kdf_salt TEXT,
                role TEXT NOT NULL DEFAULT 'free',
                email TEXT UNIQUE,
                phone TEXT,
                first_name TEXT,
                last_name TEXT,
                storage_quota INTEGER NOT NULL DEFAULT 10485760,
                trial_start DATETIME,
                trial_end DATETIME,
                subscription_status TEXT NOT NULL DEFAULT 'active',
                email_verified BOOLEAN DEFAULT FALSE,
                confirmation_token TEXT,
                confirmation_token_expires DATETIME,
                phone_verified BOOLEAN DEFAULT FALSE,
                phone_verification_code_hash TEXT,
                phone_code_expires DATETIME,
                mfa_code_hash TEXT,
                mfa_code_expires DATETIME,
                mfa_enabled BOOLEAN DEFAULT FALSE
            )''')
            db.commit()

            # Legacy v7 schema detection: a pre-v8 users table that still has
            # any of the NOT NULL KEM blob columns. We can't ALTER them away
            # in SQLite, so rebuild the table.
            existing = {row[1] for row in db.execute("PRAGMA table_info(users)").fetchall()}
            legacy_present = [c for c in self._LEGACY_DROP_COLUMNS if c in existing]
            if legacy_present:
                self._migrate_from_v7(legacy_present)
                existing = {row[1] for row in db.execute("PRAGMA table_info(users)").fetchall()}

            # Fresh-or-already-v8 path: add any columns the v8 controller needs
            # but the table still lacks. This is the path a brand-new install
            # takes when the table is created above with every v8 column.
            for column, ddl in (
                ('last_name', "ALTER TABLE users ADD COLUMN last_name TEXT"),
                ('confirmation_token_expires', "ALTER TABLE users ADD COLUMN confirmation_token_expires DATETIME"),
                ('srp_salt', "ALTER TABLE users ADD COLUMN srp_salt TEXT"),
                ('srp_verifier', "ALTER TABLE users ADD COLUMN srp_verifier TEXT"),
                ('public_key', "ALTER TABLE users ADD COLUMN public_key TEXT"),
                ('encrypted_private_key', "ALTER TABLE users ADD COLUMN encrypted_private_key TEXT"),
                ('kdf_salt', "ALTER TABLE users ADD COLUMN kdf_salt TEXT"),
                ('mfa_enabled', "ALTER TABLE users ADD COLUMN mfa_enabled BOOLEAN DEFAULT FALSE"),
                ('phone_verification_code_hash', "ALTER TABLE users ADD COLUMN phone_verification_code_hash TEXT"),
                ('mfa_code_hash', "ALTER TABLE users ADD COLUMN mfa_code_hash TEXT"),
            ):
                if column not in existing:
                    db.execute(ddl)
            db.commit()

            # Drop UNIQUE on phone if it survived from a v7 install. SQLite does
            # not support ALTER COLUMN, so we rebuild only when the index exists.
            self._drop_phone_unique_if_present()

    def _has_phone_unique_constraint(self) -> bool:
        """Return True if the ``users.phone`` column is UNIQUE.

        SQLite does not expose UNIQUE column constraints via ``PRAGMA
        table_info``; the only reliable signal is the auto-index that
        SQLite materialises for any ``UNIQUE`` column (``sqlite_autoindex_users_N``).
        """
        with sqlite3.connect(self.db_path) as db:
            for row in db.execute("PRAGMA index_list('users')").fetchall():
                idx_name = row[1]
                if not idx_name.startswith("sqlite_autoindex_users_"):
                    continue
                cols = [
                    r[2] for r in db.execute(
                        f"PRAGMA index_info('{idx_name}')"
                    ).fetchall()
                ]
                if cols == ["phone"]:
                    return True
        return False

    def _drop_phone_unique_if_present(self) -> None:
        """Remove the UNIQUE constraint on ``users.phone``.

        The v7 schema declared ``phone TEXT UNIQUE``. Carriers recycle
        numbers, so the uniqueness guarantee is illusory; it also makes
        account recovery hostile when a number changes hands.

        SQLite forbids ``DROP INDEX`` on an auto-index backing a UNIQUE
        column, so we have to rebuild the table. The rebuild follows
        the same shape as :meth:`_migrate_from_v7` but copies every
        column by position (the schema is now already v8-shaped thanks
        to the prior migration step, so we know the column order).
        """
        if not self._has_phone_unique_constraint():
            return
        with sqlite3.connect(self.db_path) as db:
            # Recover the column order from the live table.
            info = db.execute("PRAGMA table_info('users')").fetchall()
            columns = [r[1] for r in info]
            column_list = ",".join(columns)
            db.execute("PRAGMA foreign_keys=OFF")
            db.execute("ALTER TABLE users RENAME TO users__v7_phone_unq")
            # v8 schema (no UNIQUE on phone). This mirrors the fresh
            # CREATE above; if either side evolves, keep them in sync.
            db.execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                role TEXT NOT NULL DEFAULT 'free',
                email TEXT,
                phone TEXT,
                first_name TEXT,
                last_name TEXT,
                storage_quota INTEGER DEFAULT 0,
                trial_start DATETIME,
                trial_end DATETIME,
                subscription_status TEXT DEFAULT 'active',
                email_verified BOOLEAN DEFAULT 0,
                confirmation_token TEXT,
                phone_verified BOOLEAN DEFAULT 0,
                phone_verification_code_hash TEXT,
                phone_code_expires DATETIME,
                srp_salt TEXT,
                srp_verifier TEXT,
                public_key TEXT,
                encrypted_private_key TEXT,
                kdf_salt TEXT,
                mfa_enabled BOOLEAN DEFAULT 0,
                mfa_code_hash TEXT,
                mfa_code_expires DATETIME
            )''')
            db.execute(
                f"INSERT INTO users ({column_list}) SELECT {column_list} FROM users__v7_phone_unq"
            )
            db.execute("DROP TABLE users__v7_phone_unq")
            db.execute("PRAGMA foreign_keys=ON")
            db.commit()

    def _migrate_from_v7(self, legacy_columns):
        """Rebuild the users table to drop legacy v7 NOT NULL KEM columns.

        SQLite cannot drop a column or relax a NOT NULL constraint in place,
        so we rename the old table, create a fresh v8-shaped users table,
        copy every surviving column, then drop the renamed legacy table.
        """
        with sqlite3.connect(self.db_path) as db:
            db.execute("PRAGMA foreign_keys=ON")
            db.execute("BEGIN")
            db.execute("ALTER TABLE users RENAME TO users__v7_legacy")
            db.execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                srp_salt TEXT,
                srp_verifier TEXT,
                public_key TEXT,
                encrypted_private_key TEXT,
                kdf_salt TEXT,
                role TEXT NOT NULL DEFAULT 'free',
                email TEXT UNIQUE,
                phone TEXT,
                first_name TEXT,
                last_name TEXT,
                storage_quota INTEGER NOT NULL DEFAULT 10485760,
                trial_start DATETIME,
                trial_end DATETIME,
                subscription_status TEXT NOT NULL DEFAULT 'active',
                email_verified BOOLEAN DEFAULT FALSE,
                confirmation_token TEXT,
                confirmation_token_expires DATETIME,
                phone_verified BOOLEAN DEFAULT FALSE,
                phone_verification_code_hash TEXT,
                phone_code_expires DATETIME,
                mfa_code_hash TEXT,
                mfa_code_expires DATETIME,
                mfa_enabled BOOLEAN DEFAULT FALSE
            )''')
            legacy_cols = {row[1] for row in db.execute("PRAGMA table_info(users__v7_legacy)").fetchall()}
            shared = [c for c in (
                'id', 'username', 'role', 'email', 'phone', 'first_name', 'last_name',
                'storage_quota', 'trial_start', 'trial_end', 'subscription_status',
                'email_verified', 'confirmation_token', 'confirmation_token_expires',
                'phone_verified',
                'mfa_enabled',
                'srp_salt', 'srp_verifier', 'public_key', 'encrypted_private_key', 'kdf_salt',
            ) if c in legacy_cols]
            cols_csv = ", ".join(shared)
            db.execute(f"INSERT INTO users ({cols_csv}) SELECT {cols_csv} FROM users__v7_legacy")
            db.execute("DROP TABLE users__v7_legacy")
            db.execute("COMMIT")
            return  # noqa: not used as a return value; keeps readability


    def create_user(self, username: str, srp_salt: str, srp_verifier: str, public_key: str, encrypted_private_key: str,
                    kdf_salt: str, email: str, phone: str, first_name: str, last_name: str, role: str, storage_quota: int,
                    trial_start: Optional[datetime], trial_end: Optional[datetime], subscription_status: str,
                    email_verified: bool, confirmation_token: Optional[str], phone_verified: bool,
                    phone_verification_code_hash: Optional[str], phone_code_expires: Optional[datetime], mfa_enabled: bool) -> None:
        """Persist a new user from client-provided zero-knowledge credentials.

        All cryptographic material (salt, verifier, public key, encrypted
        private key, KDF salt) is generated on the client; this method only
        stores opaque values and never derives or sees the password.
        Phone and MFA codes are stored as the peppered hash supplied by
        the controller; the plaintext only ever lives in the SMS that
        leaves the building.
        """
        confirmation_token_expires = datetime.now(timezone.utc) + timedelta(hours=24) if confirmation_token else None

        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            try:
                cursor.execute(
                    """INSERT INTO users (username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, confirmation_token_expires, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, confirmation_token_expires, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled)
                )
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise

    def update_user_phone_status(self, username: str, phone_verified: bool = None,
                                phone_verification_code_hash: Optional[str] = None,
                                phone_code_expires: Optional[datetime] = None):
        """Update phone verification status and related fields.

        The ``phone_verification_code_hash`` parameter accepts the
        peppered SHA-256 digest. Passing ``None`` clears the stored
        hash (e.g. after the user verifies successfully).
        """
        params = []
        fields = []
        if phone_verified is not None:
            fields.append("phone_verified")
            params.append(phone_verified)
        if phone_verification_code_hash is not None:
            fields.append("phone_verification_code_hash")
            params.append(phone_verification_code_hash)
        if phone_code_expires is not None:
            fields.append("phone_code_expires")
            params.append(phone_code_expires)
        if not fields:
            return

        query = f"UPDATE users SET {', '.join(f'{field} = ?' for field in fields)} WHERE username = ?"
        params.append(username)

        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute(query, tuple(params))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise

    def update_user_mfa_status(self, username: str, mfa_code_hash: Optional[str] = None,
                              mfa_code_expires: Optional[datetime] = None,
                              mfa_enabled: Optional[bool] = None):
        """Update MFA code, expiration, and enabled status.

        The ``mfa_code_hash`` parameter accepts the peppered SHA-256
        digest of the freshly-generated 6-digit code. ``mfa_enabled`` is
        a tri-state: ``None`` leaves the value alone.
        """
        params = []
        fields = []
        if mfa_code_hash is not None:
            fields.append("mfa_code_hash")
            params.append(mfa_code_hash)
        if mfa_code_expires is not None:
            fields.append("mfa_code_expires")
            params.append(mfa_code_expires)
        if mfa_enabled is not None:
            fields.append("mfa_enabled")
            params.append(mfa_enabled)
        if not fields:
            return

        query = f"UPDATE users SET {', '.join(f'{field} = ?' for field in fields)} WHERE username = ?"
        params.append(username)

        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute(query, tuple(params))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise

    def update_user(self, username: str, email_verified: Optional[bool] = None, confirmation_token: Optional[str] = None):
        """Update specific user fields."""
        params = []
        fields = []
        if email_verified is not None:
            fields.append("email_verified")
            params.append(email_verified)
        if confirmation_token is not None:
            fields.append("confirmation_token")
            params.append(confirmation_token)
        if not fields:
            return

        query = f"UPDATE users SET {', '.join(f'{field} = ?' for field in fields)} WHERE username = ?"
        params.append(username)

        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute(query, tuple(params))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise

    def get_user(self, username: str) -> Optional[dict]:
        """Retrieve a user by username.

        Args:
            username (str): Username to search for.

        Returns:
            Optional[dict]: User data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            user = db.execute('''SELECT * FROM users WHERE username = ?''', (username,)).fetchone()
            return self._convert_row_to_dict(user) if user else None

    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        """Retrieve a user by ID.

        Args:
            user_id (int): ID of the user to search for.

        Returns:
            Optional[dict]: User data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            user = db.execute('''SELECT * FROM users WHERE id = ?''', (user_id,)).fetchone()
            return self._convert_row_to_dict(user) if user else None

    def get_user_by_email(self, email: str) -> Optional[dict]:
        """Retrieve a user by email address.

        Args:
            email (str): Email address to search for.

        Returns:
            Optional[dict]: User data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            user = db.execute('''SELECT * FROM users WHERE email = ?''', (email,)).fetchone()
            return self._convert_row_to_dict(user) if user else None

    def get_user_by_phone(self, phone: str) -> Optional[dict]:
        """Retrieve a user by phone number.

        Args:
            phone (str): Phone number to search for.

        Returns:
            Optional[dict]: User data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            user = db.execute('''SELECT * FROM users WHERE phone = ?''', (phone,)).fetchone()
            return self._convert_row_to_dict(user) if user else None

    def get_user_by_confirmation_token(self, token: str) -> Optional[dict]:
        """Retrieve a user by confirmation token.

        Args:
            token (str): Confirmation token to search for.

        Returns:
            Optional[dict]: User data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            user = db.execute('''SELECT * FROM users WHERE confirmation_token = ?''', (token,)).fetchone()
            return self._convert_row_to_dict(user) if user else None

    def update_role(self, username: str, role: str, storage_quota: int = 10 * 1024 * 1024, subscription_status: str = "active") -> None:
        """Update a user's role, storage quota, and subscription status.

        Args:
            username (str): Username of the user to update.
            role (str): New role for the user.
            storage_quota (int): New storage quota in bytes (default: 10MB).
            subscription_status (str): New subscription status (default: 'active').
        """
        with sqlite3.connect(self.db_path) as db:
            db.execute('''UPDATE users SET role = ?, storage_quota = ?, subscription_status = ? WHERE username = ?''',
                       (role, storage_quota, subscription_status, username))

    def count_users(self) -> int:
        """Return the total number of users.

        Implemented as ``SELECT COUNT(*)`` rather than ``len(get_all_users())``
        so the home page does not materialise the entire table on every
        request.
        """
        with sqlite3.connect(self.db_path) as db:
            row = db.execute("SELECT COUNT(*) FROM users").fetchone()
            return int(row[0]) if row else 0

    def get_all_users(self) -> list[dict]:
        """Retrieve all users.

        Returns:
            list[dict]: List of dictionaries containing user data.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            users = db.execute('''SELECT * FROM users''').fetchall()
            return [self._convert_row_to_dict(user) for user in users]

    @staticmethod
    def _parse_datetime(value) -> Optional[datetime]:
        """Parse a stored timestamp into a datetime, tolerating the format.

        Args:
            value: A datetime, an ISO-like timestamp string, or None.

        Returns:
            The parsed datetime, or None when the value is empty or unparseable.
        """
        if not value:
            return None
        if isinstance(value, datetime):
            return value
        for fmt in ('%Y-%m-%d %H:%M:%S.%f%z', '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%d %H:%M:%S'):
            try:
                return datetime.strptime(value, fmt)
            except (ValueError, TypeError):
                continue
        try:
            return datetime.fromisoformat(value)
        except (ValueError, TypeError):
            return None

    def _convert_row_to_dict(self, row) -> Optional[dict]:
        """Convert a name-keyed SQLite row into a plain dictionary.

        Reads access columns by name (the connection uses ``sqlite3.Row``), so
        the mapping is robust to column ordering and additive migrations.

        Args:
            row: A ``sqlite3.Row`` produced by a read query, or None.

        Returns:
            A dictionary of user fields, or None when the row is empty.
        """
        if not row:
            return None

        available = set(row.keys())

        def value(name, default=None):
            return row[name] if name in available else default

        # The plain ``phone_verification_code`` / ``mfa_code`` columns
        # are the legacy v7 names. Read whichever exists so the auth
        # controller's constant-time verifier keeps working during the
        # cutover; new code should look at ``*_hash`` only.
        return {
            "id": value("id"),
            "username": value("username"),
            "srp_salt": value("srp_salt"),
            "srp_verifier": value("srp_verifier"),
            "public_key": value("public_key"),
            "encrypted_private_key": value("encrypted_private_key"),
            "kdf_salt": value("kdf_salt"),
            "role": value("role", "free"),
            "email": value("email"),
            "phone": value("phone"),
            "first_name": value("first_name"),
            "last_name": value("last_name"),
            "storage_quota": value("storage_quota", 10 * 1024 * 1024),
            "trial_start": self._parse_datetime(value("trial_start")),
            "trial_end": self._parse_datetime(value("trial_end")),
            "subscription_status": value("subscription_status", "active"),
            "email_verified": bool(value("email_verified", False)),
            "confirmation_token": value("confirmation_token"),
            "confirmation_token_expires": self._parse_datetime(value("confirmation_token_expires")),
            "phone_verified": bool(value("phone_verified", False)),
            "phone_verification_code_hash": value("phone_verification_code_hash") or value("phone_verification_code"),
            "phone_verification_code": value("phone_verification_code") or value("phone_verification_code_hash"),
            "phone_code_expires": self._parse_datetime(value("phone_code_expires")),
            "mfa_code_hash": value("mfa_code_hash") or value("mfa_code"),
            "mfa_code": value("mfa_code") or value("mfa_code_hash"),
            "mfa_code_expires": self._parse_datetime(value("mfa_code_expires")),
            "mfa_enabled": bool(value("mfa_enabled", False)),
        }

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[dict]:
        """Execute a query and return the first result as a dictionary.

        Args:
            query (str): SQL query to execute.
            params (tuple): Parameters for the query (default: empty tuple).

        Returns:
            Optional[dict]: First row as a dictionary or None if no results or an error occurs.
        """
        try:
            with sqlite3.connect(self.db_path) as db:
                db.row_factory = sqlite3.Row
                cursor = db.execute(query, params)
                row = cursor.fetchone()
                return self._convert_row_to_dict(row)
        except sqlite3.Error:
            from flask import current_app
            if current_app:
                current_app.logger.exception("fetch_user: query failed")
            return None
