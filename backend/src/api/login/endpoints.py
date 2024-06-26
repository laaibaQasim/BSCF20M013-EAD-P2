from http import HTTPStatus

from api.login import schemas
from auth.authentication import authenticate
from common.context import CurrentUser
from flask import jsonify, request
from flask_restx import Resource
from helper.response import failure, success
from model.user import User

from . import api


@api.route("")
class LoginResource(Resource):
    @api.expect(schemas.login_model, validate=True)
    @api.marshal_with(schemas.login_response, skip_none=True)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user, exist = authenticate(email, password)

        if user and exist:
            return success(user, total_rows=1), HTTPStatus.OK
        elif user and not exist:
            return failure("User not found"), HTTPStatus.NOT_FOUND
        else:
            return failure("Invalid Credentials"), HTTPStatus.UNAUTHORIZED

    def get(self):
        cuser = CurrentUser.cuser
        if cuser:
            return success(CurrentUser.role_name, total_rows=1), HTTPStatus.OK
        else:
            return failure("You are not Logged In."), HTTPStatus.NOT_FOUND
