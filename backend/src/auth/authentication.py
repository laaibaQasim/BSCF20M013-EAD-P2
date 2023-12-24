from common.context import CurrentUser
from model.user import User


def authenticate(email, password):
    user = User.get_by_email(email)

    if user and user.password == password:
        CurrentUser.set_current_user(user)
        return user

    return None
