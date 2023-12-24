from functools import wraps
from common.context import CurrentUser
from common.enums import Roles
from flask import jsonify


def requires_role(role_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CurrentUser.cuser and CurrentUser.role_name == Roles.ADMIN:
                return func(*args, **kwargs)
            else:
                response = jsonify(
                    {
                        "error": "Permission denied. Required role: {}".format(
                            Roles.ADMIN
                        )
                    }
                )
                response.status_code = 403
                return response

        return wrapper

    return decorator
