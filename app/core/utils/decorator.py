from functools import wraps

from flask import current_app
from flask_login.utils import current_user


def admin_only(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_staff:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view
