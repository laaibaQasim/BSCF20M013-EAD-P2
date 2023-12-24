from model.user_activity import UserActivity
from common.context import CurrentUser


def create_activity(action, details):
    if not CurrentUser.cuser:
        return
    user_activity = UserActivity()
    user_activity.user_id = CurrentUser.cuser.id
    user_activity.action = action
    user_activity.details = details
    user_activity.insert()

