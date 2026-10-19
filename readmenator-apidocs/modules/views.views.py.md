# `views.views`

> Source: [views/views.py:1](../../views/views.py#L1) | language `py` | coverage 66.7% | [API index](../index.md)

Top-level non-API views: home page, account preferences, etc.

## Contents

- **Classes:** [`MFAEnableForm`](#mfaenableform)
- **Functions:** [`home`](#home)

## Type Diagram

```mermaid
classDiagram
    direction LR
    class MFAEnableForm
    MFAEnableForm : mfa_enabled
    MFAEnableForm : submit
```

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_views_views_py__home(["home"])
    n_views_views_py__MFAEnableForm(["MFAEnableForm"])
    n_models_user_py__UserDB___init__["user.UserDB.__init__"]
    n_models_user_py__UserDB_count_users["user.UserDB.count_users"]
    n_utils_utils_py__database_path["utils.database_path"]
    n_views_views_py__home --> n_views_views_py__MFAEnableForm
    n_views_views_py__home -.-> n_models_user_py__UserDB___init__
    n_views_views_py__home -.-> n_models_user_py__UserDB_count_users
    n_views_views_py__home -.-> n_utils_utils_py__database_path
```

## Classes

<a id="mfaenableform"></a>

### `MFAEnableForm`

`class` | [views/views.py:15](../../views/views.py#L15)

```python
class MFAEnableForm(FlaskForm)
```

Bases: `FlaskForm`

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`mfa_enabled`](#mfaenableform-mfa_enabled) |  | `BooleanField('Enable Two-Factor Authentication (2FA)')` |  |
| [`submit`](#mfaenableform-submit) |  | `SubmitField('Save')` |  |

---

## Functions

<a id="home"></a>

### `home`

`function` | [views/views.py:21](../../views/views.py#L21)

Decorators: `@views_bp.route('/')`

```python
def home()
```

Render the landing/home page.

The total user count is fetched with ``SELECT COUNT(*)`` directly
rather than loading every row into memory, so the cost is O(1)
regardless of the user table size.

*Calls:* [`UserDB.__init__`](models.user.py.md#userdb-__init__), [`UserDB.count_users`](models.user.py.md#userdb-count_users), [`database_path`](utils.utils.py.md#database_path), [`MFAEnableForm`](#mfaenableform)

---
