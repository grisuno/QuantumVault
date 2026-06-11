from typing import Dict, List, Optional
import sqlite3

class PlanDB:
    """Database operations for subscription plans."""
    def __init__(self, db_path: str):
        """Initialize the PlanDB with the database path.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Initialize the plans table with required fields."""
        with sqlite3.connect(self.db_path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                storage_quota INTEGER NOT NULL,
                trial_days INTEGER NOT NULL DEFAULT 0,
                price REAL NOT NULL
            )''')
            # Insert default plans if table is empty
            cursor = db.execute('SELECT COUNT(*) FROM plans')
            if cursor.fetchone()[0] == 0:
                default_plans = [
                    ('free', 10 * 1024 * 1024, 14, 0.0),
                    ('bronze', 100 * 1024 * 1024, 0, 5.0),
                    ('silver', 500 * 1024 * 1024, 0, 10.0),
                    ('gold', 1024 * 1024 * 1024, 0, 20.0)
                ]
                db.executemany('INSERT INTO plans (name, storage_quota, trial_days, price) VALUES (?, ?, ?, ?)', default_plans)
                db.commit()

    def get_plan(self, plan_name: str) -> Optional[Dict]:
        """Retrieve a plan by name.

        Args:
            plan_name (str): Name of the plan to search for.

        Returns:
            Optional[Dict]: Plan data as a dictionary or None if not found.
        """
        with sqlite3.connect(self.db_path) as db:
            plan = db.execute('SELECT * FROM plans WHERE name = ?', (plan_name,)).fetchone()
            return self._convert_row_to_dict(plan) if plan else None

    def get_all_plans(self) -> List[Dict]:
        """Retrieve all plans.

        Returns:
            List[Dict]: List of dictionaries containing plan data.
        """
        with sqlite3.connect(self.db_path) as db:
            plans = db.execute('SELECT * FROM plans').fetchall()
            return [self._convert_row_to_dict(plan) for plan in plans]

    def create_plan(self, name: str, storage_quota: int, trial_days: int, price: float) -> None:
        """Create a new plan.

        Args:
            name (str): Name of the plan.
            storage_quota (int): Storage quota in bytes.
            trial_days (int): Number of trial days.
            price (float): Price of the plan.
        """
        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute('INSERT INTO plans (name, storage_quota, trial_days, price) VALUES (?, ?, ?, ?)',
                           (name, storage_quota, trial_days, price))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise Exception(f"Error creating plan: {e}")

    def update_plan(self, name: str, storage_quota: Optional[int] = None, trial_days: Optional[int] = None,
                    price: Optional[float] = None) -> None:
        """Update an existing plan.

        Args:
            name (str): Name of the plan to update.
            storage_quota (Optional[int]): New storage quota in bytes.
            trial_days (Optional[int]): New number of trial days.
            price (Optional[float]): New price of the plan.
        """
        params = []
        fields = []
        if storage_quota is not None:
            fields.append("storage_quota = ?")
            params.append(storage_quota)
        if trial_days is not None:
            fields.append("trial_days = ?")
            params.append(trial_days)
        if price is not None:
            fields.append("price = ?")
            params.append(price)
        if not fields:
            return

        query = f"UPDATE plans SET {', '.join(fields)} WHERE name = ?"
        params.append(name)

        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute(query, tuple(params))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise Exception(f"Error updating plan: {e}")

    def delete_plan(self, name: str) -> None:
        """Delete a plan by name.

        Args:
            name (str): Name of the plan to delete.
        """
        with sqlite3.connect(self.db_path) as db:
            try:
                db.execute('DELETE FROM plans WHERE name = ?', (name,))
                db.commit()
            except sqlite3.Error as e:
                db.rollback()
                raise Exception(f"Error deleting plan: {e}")

    def _convert_row_to_dict(self, row) -> Optional[Dict]:
        """Convert an SQLite row to a dictionary."""
        if not row:
            return None
        return {
            "id": row[0],
            "name": row[1],
            "storage_quota": row[2],
            "trial_days": row[3],
            "price": row[4]
        }

    def validate_plan_payment(self, plan_name: str, amount_paid: float) -> bool:
        """Validate that the paid amount matches the plan price.

        Args:
            plan_name (str): Name of the plan.
            amount_paid (float): Amount paid.

        Returns:
            bool: True if the amount matches the plan price within tolerance.
        """
        plan = self.get_plan(plan_name)
        if not plan:
            return False
        return abs(float(amount_paid) - plan['price']) < 0.01
