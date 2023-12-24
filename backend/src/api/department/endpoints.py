from http import HTTPStatus

from api.department import schemas
from flask import jsonify, request
from flask_restx import Resource
from helper.response import failure, success
from model.department import Department

from . import api


@api.route("")
class DepartmentList(Resource):
    @api.marshal_with(schemas.department_response, skip_none=True)
    def get(self):
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
