from http import HTTPStatus
from flask_restx import Resource
from helper.response import failure, success

from common.context import CurrentUser

from . import api


@api.route("")
class LogoutRespnse(Resource):
    def post(self):
        if CurrentUser.cuser:
            CurrentUser.cuser = None
            CurrentUser.role_name = None
            return success("Logged out"), HTTPStatus.OK
        return success("Login First"), HTTPStatus.OK
