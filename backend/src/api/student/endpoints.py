from flask import request
from flask_restx import Resource
from http import HTTPStatus

from common.decorators import requires_role
from helper.response import success, failure

from model.department import Department
from model.user import User
from model.interest import Interest
from model.role import Role
from model.student import Student


from common.lists import degrees
from common.enums import Roles

from api.student import schemas

from . import api


@api.route("")
class StudentList(Resource):
    @api.marshal_with(schemas.student_response, skip_none=True)
    def get(self):
        try:
            # Pagination parameters
            page = int(request.args.get("page", 1))
            page_size = int(request.args.get("page_size", 3))

            # Query students based on pagination
            students_paginated = Student.query.paginate(
                page=page, per_page=page_size, error_out=False
            )

            # Extract required data from paginated result
            students_list = students_paginated.items
            data = [
                {
                    "ID": student.user.id,
                    "name": student.user.name,
                    "roll_number": student.roll_number,
                    "department": student.department.name,
                    "degree": student.degree,
                    "dob": student.dob,
                    "city": student.city,
                    "interest": student.interest.name,
                }
                for student in students_list
            ]

            return success(data, total_rows=students_paginated.total)
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    @api.expect(schemas.student_model, validate=True)
    @requires_role("admin")
    @api.marshal_with(schemas.student_response, skip_none=True)
    def post(self):
        try:
            # Parse student data from the request
            data = request.get_json()

            # Check if the department exists.
            department_name = data.get("department")
            department = Department.get_by_name(department_name)
            if not department:
                return failure("Department not found"), HTTPStatus.NOT_FOUND

            # Check if the interest already exists, if not, add it
            interest_name = data.get("interest")
            interest = Interest.get_by_name(interest_name)
            if not interest:
                interest = Interest(name=interest_name)
                new_interest = interest.insert()
            else:
                new_interest = interest

            # Check if the degree exists
            degree_name = data.get("degree")
            if degree_name not in degrees:
                return failure("Degree not found"), HTTPStatus.NOT_FOUND

            # Construct the student data with department and interest IDs
            std_role = Role.get_role_by_name(Roles.STUDENT)
            new_user = User(
                name=data.get("name"),
                email=data.get("email"),
                password="pucit",
                role=std_role,
            )

            new_student = Student(
                user=new_user,
                roll_number=data.get("roll_number"),
                department=department,
                interest=new_interest,
                degree=data.get("degree"),
                dob=data.get("dob"),
                city=data.get("city"),
                gender=data.get("gender"),
                start_date=data.get("start_date"),
                end_date=data.get("end_date"),
            )
            new_student.insert()

            # Return success response
            return (
                success({"message": "Student added successfully"}),
                HTTPStatus.CREATED,
            )
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/<int:student_id>")
class StudentItem(Resource):
    @api.marshal_with(schemas.student_response, skip_none=True)
    def get(self, student_id):
        try:
            student = Student.get_by_id(student_id)
            if not student:
                return failure("Student not found"), HTTPStatus.NOT_FOUND
            data = [
                {
                    "ID": student.user.id,
                    "name": student.user.name,
                    "roll_number": student.roll_number,
                    "department": student.department.name,
                    "degree": student.degree,
                    "dob": student.dob,
                    "city": student.city,
                    "interest": student.interest.name,
                }
            ]

            return success(data, total_rows=1)
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    @requires_role("admin")
    def delete(self, student_id):
        try:
            # Query student by ID
            student = Student.get_by_id(student_id)

            # Check if the student exists
            if not student:
                return failure("Student not found"), HTTPStatus.NOT_FOUND

            # Delete the student
            student.delete()

            # Return success response
            return success({"message": "Student deleted successfully"}, total_rows=1)
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    @api.expect(schemas.student_model, validate=True)
    @requires_role("admin")
    @api.marshal_with(schemas.student_response, skip_none=True)
    def put(self, student_id):
        try:
            # Parse student data from the request
            data = request.get_json()

            user_to_update = User.get_by_id(student_id)
            if not user_to_update:
                return failure("Student not found"), HTTPStatus.NOT_FOUND

            # Check if the department exists.
            department_name = data.get("department")
            department = Department.get_by_name(department_name)
            if not department:
                return failure("Department not found"), HTTPStatus.NOT_FOUND

            # Check if the interest already exists, if not, add it
            interest_name = data.get("interest")
            interest = Interest.get_by_name(interest_name)
            if not interest:
                interest = Interest(name=interest_name)
                new_interest = interest.insert()
            else:
                new_interest = interest

            # Check if the degree exists
            degree_name = data.get("degree")
            if degree_name not in degrees:
                return failure("Degree not found"), HTTPStatus.NOT_FOUND

            to_update = {
                "roll_number": data.get("roll_number"),
                "degree": data.get("degree"),
                "dob": data.get("dob"),
                "city": data.get("city"),
                "gender": data.get("gender"),
                "start_date": data.get("start_date"),
                "end_date": data.get("end_date"),
                "department_id": department.id,
                "interest_id": new_interest.id,
            }

            Student.update(student_id, to_update)

            # Return success response
            return (
                success({"message": "Student updated successfully"}, total_rows=1),
                HTTPStatus.OK,
            )
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/status")
class StudentsStatusResource(Resource):
    def get(self):
        """
        Get the number of students about to graduate in 60 days, graduated and enrolled in last 30 days.
        :return : Dictionary
        """
        currently_studying = Student.get_currently_studying_count()
        recently_enrolled = Student.get_recently_enrolled_count()
        about_to_graduate = Student.get_about_to_graduate_count()
        graduated = Student.get_graduated_count()

        res = {
            "currently_studying": currently_studying,
            "recently_enrolled": recently_enrolled,
            "about_to_graduate": about_to_graduate,
            "graduated": graduated,
        }
        if res:
            return success(res, total_rows=4)
        else:
            return failure("No Data Found."), HTTPStatus.NOT_FOUND
