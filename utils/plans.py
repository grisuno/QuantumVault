from typing import Dict

class SubscriptionPlans:
    """Define los planes de suscripción disponibles."""

    PLANS: Dict[str, Dict] = {
        "free": {
            "storage_quota": 10 * 1024 * 1024,  # 10MB
            "trial_days": 14,
            "price": 0.0
        },
        "bronze": {
            "storage_quota": 100 * 1024 * 1024,  # 100MB
            "trial_days": 0,
            "price": 5.0
        },
        "silver": {
            "storage_quota": 500 * 1024 * 1024,  # 500MB
            "trial_days": 0,
            "price": 10.0
        },
        "gold": {
            "storage_quota": 1024 * 1024 * 1024,  # 1GB
            "trial_days": 0,
            "price": 20.0
        }
    }

    @staticmethod
    def get_plan(plan_name: str) -> Dict:
        """Obtiene los detalles de un plan.

        Args:
            plan_name (str): Nombre del plan.

        Returns:
            Dict: Detalles del plan.
        """
        return SubscriptionPlans.PLANS.get(plan_name, SubscriptionPlans.PLANS["free"])

    @staticmethod
    def validate_plan_payment(plan_name, amount_paid):
        """Valida que el monto pagado coincide con el plan."""
        plan = SubscriptionPlans.get_plan(plan_name)
        if not plan:
            return False
        # Permitir una pequeña tolerancia para errores de redondeo
        return abs(float(amount_paid) - plan['price']) < 0.01
