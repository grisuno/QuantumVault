# `utils.plans`

> Source: [utils/plans.py:1](../../utils/plans.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

## Contents

- **Classes:** [`SubscriptionPlans`](#subscriptionplans)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_utils_plans_py__SubscriptionPlans_validate_plan_payment(["SubscriptionPlans.validate_plan_payment"])
    n_utils_plans_py__SubscriptionPlans_get_plan(["SubscriptionPlans.get_plan"])
    n_utils_plans_py__SubscriptionPlans_validate_plan_payment --> n_utils_plans_py__SubscriptionPlans_get_plan
```

## Classes

<a id="subscriptionplans"></a>

### `SubscriptionPlans`

`class` | [utils/plans.py:3](../../utils/plans.py#L3)

```python
class SubscriptionPlans
```

Define los planes de suscripción disponibles.

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`PLANS`](#subscriptionplans-plans) | `Dict[str, Dict]` | `{'free': {'storage_quota': 10 * 1024 * 1024, 'trial_days': 14, 'price': 0.0}, 'bronze': {'storage_quota': 100 * 1024 * 1024, 'trial_days': 0, 'price': 5.0}, 'silver': {'storage_quota': 500 * 1024 * 1024, 'trial_days': 0, 'price': 10.0}, 'gold': {'storage_quota': 1024 * 1024 * 1024, 'trial_days': 0, 'price': 20.0}}` |  |

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`get_plan`](#subscriptionplans-get_plan) | staticmethod | Obtiene los detalles de un plan. |
| [`validate_plan_payment`](#subscriptionplans-validate_plan_payment) | staticmethod | Valida que el monto pagado coincide con el plan. |

<a id="subscriptionplans-get_plan"></a>

#### `SubscriptionPlans.get_plan`

`staticmethod` | [utils/plans.py:30](../../utils/plans.py#L30)

Decorators: `@staticmethod`

```python
def get_plan(plan_name: str) -> Dict
```

Obtiene los detalles de un plan.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `plan_name` | `str` |  | Nombre del plan. |

**Returns:** `Dict` - Detalles del plan.

*Called by:* [`SubscriptionPlans.validate_plan_payment`](#subscriptionplans-validate_plan_payment)

<a id="subscriptionplans-validate_plan_payment"></a>

#### `SubscriptionPlans.validate_plan_payment`

`staticmethod` | [utils/plans.py:42](../../utils/plans.py#L42)

Decorators: `@staticmethod`

```python
def validate_plan_payment(plan_name, amount_paid)
```

Valida que el monto pagado coincide con el plan.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `plan_name` |  |  |  |
| `amount_paid` |  |  |  |

*Calls:* [`SubscriptionPlans.get_plan`](#subscriptionplans-get_plan)

---
