# `views.subscription`

> Source: [views/subscription.py:1](../../views/subscription.py#L1) | language `py` | coverage 60.0% | [API index](../index.md)

## Contents

- **Classes:** [`SubscriptionForm`](#subscriptionform)
- **Functions:** [`subscribe`](#subscribe), [`payment_success`](#payment_success)

## Type Diagram

```mermaid
classDiagram
    direction LR
    class SubscriptionForm
    SubscriptionForm : __init__()
    SubscriptionForm : plan
    SubscriptionForm : submit
```

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_views_subscription_py__subscribe(["subscribe"])
    n_views_subscription_py__SubscriptionForm___init__(["SubscriptionForm.__init__"])
    n_models_plans_py__PlanDB___init__["plans.PlanDB.__init__"]
    n_models_plans_py__PlanDB_get_all_plans["plans.PlanDB.get_all_plans"]
    n_utils_utils_py__database_path["utils.database_path"]
    n_models_plans_py__PlanDB_get_plan["plans.PlanDB.get_plan"]
    n_views_subscription_py__payment_success(["payment_success"])
    n_models_plans_py__PlanDB_validate_plan_payment["plans.PlanDB.validate_plan_payment"]
    n_models_user_py__UserDB___init__["user.UserDB.__init__"]
    n_models_user_py__UserDB_update_role["user.UserDB.update_role"]
    n_views_subscription_py__subscribe --> n_views_subscription_py__SubscriptionForm___init__
    n_views_subscription_py__SubscriptionForm___init__ -.-> n_models_plans_py__PlanDB___init__
    n_views_subscription_py__SubscriptionForm___init__ -.-> n_models_plans_py__PlanDB_get_all_plans
    n_views_subscription_py__SubscriptionForm___init__ -.-> n_utils_utils_py__database_path
    n_views_subscription_py__subscribe -.-> n_models_plans_py__PlanDB___init__
    n_views_subscription_py__subscribe -.-> n_models_plans_py__PlanDB_get_plan
    n_views_subscription_py__subscribe -.-> n_utils_utils_py__database_path
    n_views_subscription_py__payment_success -.-> n_models_plans_py__PlanDB___init__
    n_views_subscription_py__payment_success -.-> n_models_plans_py__PlanDB_get_plan
    n_views_subscription_py__payment_success -.-> n_models_plans_py__PlanDB_validate_plan_payment
    n_views_subscription_py__payment_success -.-> n_models_user_py__UserDB___init__
    n_views_subscription_py__payment_success -.-> n_models_user_py__UserDB_update_role
    n_views_subscription_py__payment_success -.-> n_utils_utils_py__database_path
```

## Classes

<a id="subscriptionform"></a>

### `SubscriptionForm`

`class` | [views/subscription.py:24](../../views/subscription.py#L24)

```python
class SubscriptionForm(FlaskForm)
```

Bases: `FlaskForm`

Formulario para seleccionar un plan de suscripción.

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`plan`](#subscriptionform-plan) |  | `SelectField('Subscription Plan', validators=[DataRequired()])` |  |
| [`submit`](#subscriptionform-submit) |  | `SubmitField('Subscribe')` |  |

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#subscriptionform-__init__) | constructor |  |

<a id="subscriptionform-__init__"></a>

#### `SubscriptionForm.__init__`

`constructor` | [views/subscription.py:26](../../views/subscription.py#L26)

```python
def __init__(self, *args, **kwargs)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `*args` |  |  |  |
| `**kwargs` |  |  |  |

*Calls:* [`PlanDB.__init__`](models.plans.py.md#plandb-__init__), [`PlanDB.get_all_plans`](models.plans.py.md#plandb-get_all_plans), [`database_path`](utils.utils.py.md#database_path)

*Called by:* [`subscribe`](#subscribe)

---

## Functions

<a id="subscribe"></a>

### `subscribe`

`function` | [views/subscription.py:37](../../views/subscription.py#L37)

Decorators: `@subscription_bp.route('/subscribe', methods=['GET', 'POST'])`, `@limiter.limit('10 per minute')`

```python
def subscribe()
```

Maneja la selección de planes y el proceso de pago.

*Calls:* [`PlanDB.__init__`](models.plans.py.md#plandb-__init__), [`PlanDB.get_plan`](models.plans.py.md#plandb-get_plan), [`database_path`](utils.utils.py.md#database_path), [`SubscriptionForm.__init__`](#subscriptionform-__init__)

---

<a id="payment_success"></a>

### `payment_success`

`function` | [views/subscription.py:86](../../views/subscription.py#L86)

Decorators: `@subscription_bp.route('/payment/success')`, `@login_required`, `@limiter.limit('10 per minute')`

```python
def payment_success()
```

Maneja el éxito del pago y actualiza el plan del usuario.

*Calls:* [`PlanDB.__init__`](models.plans.py.md#plandb-__init__), [`PlanDB.get_plan`](models.plans.py.md#plandb-get_plan), [`PlanDB.validate_plan_payment`](models.plans.py.md#plandb-validate_plan_payment), [`UserDB.__init__`](models.user.py.md#userdb-__init__), [`UserDB.update_role`](models.user.py.md#userdb-update_role), [`database_path`](utils.utils.py.md#database_path)

---
