from http import HTTPStatus
from flask_restx import Resource
from flask import request
from helper.response import failure, success

from model.user_activity import UserActivity
from common.context import CurrentUser

from . import api


@api.route("")
class LogRespnse(Resource):
    def post(self):
        if CurrentUser.cuser:
            data = request.get_json()
            action = data.get('action')
            details = data.get('details')
            if not action or not details:
                return failure("Incorrect Data"), HTTPStatus.NO_CONTENT
            to_add = {
                "user_id":CurrentUser.cuser.id,
                "action":action.upper(),
                "details":details
            }
            UserActivity(**to_add).insert()
            return success("Logged out"), HTTPStatus.OK
        return failure("No logged in user"), HTTPStatus.NOT_FOUND
