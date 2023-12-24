from flask import request, jsonify
from flask_restx import Resource
from http import HTTPStatus

from api.department import schemas

from helper.response import success, failure

from model.department import Department

from . import api


@api.route("")
class DepartmentList(Resource):
    @api.marshal_with(schemas.department_response, skip_none=True)
    def get(self):
        try:
            departments = Department.get()
            if not departments:
                return failure("No departments found"), HTTPStatus.NOT_FOUND

            data = [
                {
                    "ID": dept.id,
                    "name": dept.name,
                }
                for dept in departments
            ]
            return success(data, total_rows=len(data))

        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
