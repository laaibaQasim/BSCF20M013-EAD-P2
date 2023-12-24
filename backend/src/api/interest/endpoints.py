from flask import request, jsonify
from flask_restx import Resource
from http import HTTPStatus

from api.interest import schemas

from helper.response import success, failure

from model.interest import Interest

from . import api


@api.route("")
class DepartmentList(Resource):
    @api.marshal_with(schemas.interest_response, skip_none=True)
    def get(self):
        try:
            interests = Interest.get()
            if not interests:
                return failure("No interest found"), HTTPStatus.NOT_FOUND

            data = [
                {
                    "ID": interest.id,
                    "name": interest.name,
                }
                for interest in interests
            ]
            return success(data, total_rows=len(data))

        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
