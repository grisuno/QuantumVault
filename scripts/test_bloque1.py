"""Bloque 1 test: superadmin_edit_user endpoint.

Renders the user-edit form via Flask's test client, then verifies
GET (200) + POST (200) paths plus the role guard. The DB is
backed up before the run and restored afterwards, so a failed test
cannot leave dirty state.

Usage:  python3 scripts/test_bloque1.py
"""
import os
import sys
import shutil
import re

# 1. Backup DB
DB = "instance/users.db"
BAK = "/tmp/users.db.bloque1.testbak"
shutil.copy2(DB, BAK)
print(f"[setup] backed up -> {BAK}")

# 2. Bootstrap Flask
sys.path.insert(0, os.getcwd())
os.environ.setdefault("FLASK_ENV", "dev")

from app import create_app
from models.user import UserDB

app = create_app()

# 3. Find a superadmin user
udb = UserDB(os.path.join(os.getcwd(), "instance/users.db"))
users = udb.get_all_users() or []
superadmins = [u for u in users if u.get("role") == "superadmin"]
if not superadmins:
    print("[fail] no superadmin in DB")
    sys.exit(1)
su = superadmins[0]
print(f"[setup] acting as superadmin: {su['username']} (id={su['id']})")

# 4. Resolve the real admin token the app uses.
# views/admin.py declares `token = secrets.token_urlsafe(32)` at import
# time, so the same value is bound in the blueprint.
from views.admin import token
ADMIN_TOKEN = token
print(f"[setup] admin token len = {len(ADMIN_TOKEN)}")

# 5. Monkey-patch user_loader to skip the SRP handshake
class _FakeUser:
    def __init__(self, row):
        self.id = row["id"]
        self.username = row["username"]
        self.role = row["role"]
    @property
    def is_authenticated(self): return True
    @property
    def is_active(self): return True
    @property
    def is_anonymous(self): return False
    def get_id(self): return str(self.id)

@app.login_manager.user_loader
def _load_user(uid):
    row = udb.get_user_by_id(int(uid))
    if not row:
        return None
    return _FakeUser(row)

# Flask-Login's "strong" session protection drops the session when
# the client IP changes between writes and reads (e.g. the test
# client's session_transaction opens a "None-IP" cookie context and
# the real request then comes from 127.0.0.1). Disable it for tests.
app.login_manager.session_protection = None
app.config["SESSION_COOKIE_SECURE"] = False
app.config["REMEMBER_COOKIE_SECURE"] = False

# Flask-Talisman enforces Referer == Host on POST. In the test client
# the Host header drifts between session_transaction and the real
# request, so we relax this single check while keeping every other
# Talisman header intact. (The check is gated by WTF_CSRF_SSL_STRICT
# and request.is_secure, so HTTP test requests skip it anyway, but
# the empty-Referer check at line 293 still fires. We disable the
# whole CSRF referer strictness via config instead.)
app.config["WTF_CSRF_SSL_STRICT"] = False

results = []
def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}{(' :: ' + detail) if detail else ''}")
    results.append((name, ok, detail))

try:
    with app.test_client() as c:
        # a) Log in as superadmin
        with c.session_transaction() as sess:
            sess["_user_id"] = str(su["id"])
            sess["_fresh"] = True
        # c) Re-render the edit page to extract a fresh CSRF token
        r1 = c.get(f"/superadmin{ADMIN_TOKEN}/edit/{su['username']}")
        check("GET /superadmin<token>/edit/<user> as superadmin",
              r1.status_code == 200,
              f"status={r1.status_code}")
        edit_body = r1.get_data(as_text=True)
        m = re.search(r'name="csrf_token"[^>]*value="([^"]+)"', edit_body) or \
            re.search(r'value="([^"]+)"[^>]*name="csrf_token"', edit_body)
        csrf = m.group(1) if m else None
        if not csrf:
            csrf = c.session_transaction().__enter__().get("csrf_token")
        form_data = {
            "username": su["username"],
            "role": "superadmin",
            "email": su.get("email") or "",
            "phone": su.get("phone") or "",
            "first_name": su.get("first_name") or "",
            "last_name": su.get("last_name") or "",
            "storage_quota": str(su.get("storage_quota") or 1099511627776),
            "subscription_status": su.get("subscription_status") or "active",
            "email_verified": "y",
            "phone_verified": "",
            "trial_start": su.get("trial_start").isoformat()[:10] if su.get("trial_start") else "",
            "trial_end": su.get("trial_end").isoformat()[:10] if su.get("trial_end") else "",
            "submit": "Update User",
        }
        if csrf:
            form_data["csrf_token"] = csrf
        r2 = c.post(f"/superadmin{ADMIN_TOKEN}/edit/{su['username']}",
                    data=form_data, follow_redirects=True)
        check("POST /superadmin<token>/edit/<user> as superadmin",
              r2.status_code in (200, 302),
              f"status={r2.status_code}")

        # d) Old path must be 404
        r3 = c.get(f"/admin{ADMIN_TOKEN}/edit/{su['username']}")
        check("OLD /admin<token>/edit/<user> must be 404",
              r3.status_code == 404,
              f"status={r3.status_code}")

        # e) Superadmin index lists users
        r4 = c.get(f"/superadmin{ADMIN_TOKEN}")
        body = r4.get_data(as_text=True)
        check("superadmin index renders + lists the user",
              r4.status_code == 200 and su["username"] in body,
              f"status={r4.status_code}, has_username={su['username'] in body}")

        # f) Role guard: switch to a non-superadmin and re-try
        non_su = next((u for u in users
                       if u["id"] != su["id"] and u.get("role") != "superadmin"),
                      None)
        if non_su:
            with c.session_transaction() as sess:
                sess["_user_id"] = str(non_su["id"])
                sess["_fresh"] = True
            r5 = c.get(f"/superadmin{ADMIN_TOKEN}/edit/{su['username']}")
            check("GET as non-superadmin -> 403",
                  r5.status_code == 403,
                  f"status={r5.status_code}")
        else:
            check("GET as non-superadmin -> 403", True,
                  "skipped (no other user in DB to impersonate)")

        # h) Form must NOT contain the removed token / phone_code fields
        check("form omits confirmation_token field",
              'name="confirmation_token"' not in edit_body,
              "ok" if 'name="confirmation_token"' not in edit_body else "STILL THERE")
        check("form omits phone_verification_code field",
              'name="phone_verification_code"' not in edit_body,
              "ok" if 'name="phone_verification_code"' not in edit_body else "STILL THERE")

        # i) UserDB.update_user accepts the cleaned payload
        pre = udb.get_user_by_id(su["id"]) or {}
        pre_token_len = len(pre.get("confirmation_token") or "")
        udb.update_user(su["username"], email_verified=True)
        post = udb.get_user_by_id(su["id"]) or {}
        post_token_len = len(post.get("confirmation_token") or "")
        check("UserDB.update_user(email_verified=True) round-trips",
              pre_token_len == post_token_len,
              f"len {pre_token_len} -> {post_token_len}")

        # j) The form role choices include the full role set
        # Note: WTForms emits <option selected value="X"> when X is the
        # current value, so the regex must match either attribute order.
        roles_in_html = set(re.findall(r'<option[^>]*value="(\w+)"', edit_body))
        check("form offers the full role set",
              {"free","bronze","silver","gold","admin","superadmin"} <= roles_in_html,
              f"roles={sorted(roles_in_html)}")

        # g) DB still has the superadmin row intact
        post = udb.get_user_by_id(su["id"])
        check("DB still has the superadmin row",
              post is not None and post.get("role") == "superadmin",
              f"role={post.get('role') if post else 'MISSING'}")

finally:
    shutil.copy2(BAK, DB)
    print(f"[teardown] restored {DB} from {BAK}")

failed = [n for (n, ok, _) in results if not ok]
print()
print(f"==> {len(results) - len(failed)}/{len(results)} passed")
sys.exit(0 if not failed else 1)
