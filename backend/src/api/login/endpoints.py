from flask import request, jsonify
from flask_restx import Resource
from http import HTTPStatus

from api.login import schemas

from helper.response import success, failure

from auth.authentication import authenticate

from common.context import CurrentUser

from . import api


@api.route("")
class LoginResource(Resource):
    @api.expect(schemas.user_model, validate=True)
    @api.marshal_with(schemas.user_response, skip_none=True)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email, password)

        if user:
            return success(user, total_rows=1)
        else:
            return failure("User not found"), HTTPStatus.NOT_FOUND

    @api.marshal_with(schemas.user_response, skip_none=True)
    def get(self):
        cuser = CurrentUser.cuser
        if cuser:
            return success(cuser, total_rows=1)
        else:
            return failure("User not found"), HTTPStatus.NOT_FOUND
