from http import HTTPStatus
from sqlalchemy import text
from api.student import schemas
from common.decorators import requires_role
from common.enums import Roles
from common.lists import degrees
from flask import request
from flask_restx import Resource
from helper.response import failure, success
from model.department import Department
from model.interest import Interest
from model.role import Role
from model.student import Student
from model.user import User

from . import api


@api.route("")
class StudentList(Resource):

    @api.marshal_with(schemas.student_response, skip_none=True)
    def get(self):
        # Pagination parameters
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 10))

        # Sorting parameters
        sort_column = request.args.get("sort", "id")
        sort_direction = request.args.get("direction", "asc")

        # Map the sort_column to actual table and column names
        column_mapping = {
            "id": Student.id,
            "user.name": User.name,
            "department.name": Department.name,
            "interest.name": Interest.name,
        }

        # Determine the column to sort based on the mapping
        sort_column_mapped = column_mapping.get(sort_column, Student.id)

        # Query students based on pagination and sorting
        students_query = (
            Student.query
            .join(User)
            .join(Department)
            .join(Interest)
            .order_by(text(f"{sort_column_mapped} {sort_direction}"))
            .paginate(page=page, per_page=page_size, error_out=False)
        )

        # Extract required data from paginated result
        students_list = students_query.items

        return success(students_list, total_rows=students_query.total)

    @api.expect(schemas.student_model, validate=True)
    @requires_role("admin")
    @api.marshal_with(schemas.student_response, skip_none=True)
    def post(self):
        try:
            data = request.get_json()

            # Check if the degree exists
            degree_name = data.get("degree")
            if degree_name not in degrees:
                return failure("Degree not found"), HTTPStatus.NOT_FOUND

             # Check if the department exists.
            department_data = data.get("department", {})
            department_name = department_data.get('name', '') 
            department = Department.get_by_name(department_name)
            if not department:
                return failure("Department not found"), HTTPStatus.NOT_FOUND


             # Check if the interest already exists, if not, add it
            interest_data = data.get("interest", {})
            interest_name = interest_data.get('name')
            interest = Interest.get_by_name(interest_name)
            if not interest:
                interest = Interest(name=interest_name)
                new_interest = interest.insert()
            else:
                new_interest = interest

            std_role = Role.get_role_by_name(Roles.STUDENT)
            user_data = data.get("user", {})
            to_add = {
                "name":user_data.get("name"),
                "email":user_data.get("email"),
                "role" :std_role,
            }

            # Construct the student data with department and interest IDs
            added_user = User(**to_add).insert()

            to_add_std = {
                "user": added_user,
                "roll_number": data.get("roll_number"),
                "department" : department,
                "interest" : new_interest,
                "degree" : data.get("degree"),
                "dob":data.get("dob"),
                "city":data.get("city"),
                "gender":data.get("gender"),
                "start_date":data.get("start_date"),
                "end_date":data.get("end_date"),
            }
            Student(**to_add_std).insert()

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
        student = Student.get_by_id(student_id)
        if not student:
            return failure("Student not found"), HTTPStatus.NOT_FOUND

        return success(student, total_rows=1)

    @requires_role("admin")
    def delete(self, student_id):
        try:
            student = Student.get_by_id(student_id)

            if not student:
                return failure("Student not found"), HTTPStatus.NOT_FOUND

            student.delete()

            return success({"message": "Student deleted successfully"}, total_rows=1)
        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    @api.expect(schemas.student_model, validate=True)
    @requires_role("admin")
    @api.marshal_with(schemas.student_response, skip_none=True)
    def patch(self, student_id):
        try:
            data = request.get_json()

            # Check if the degree exists
            degree_name = data.get("degree")
            if degree_name not in degrees:
                return failure("Degree not found"), HTTPStatus.NOT_FOUND

            # Check if the department exists.
            department_data = data.get("department", {})
            department_name = department_data.get('name', '') 
            department = Department.get_by_name(department_name)
            if not department:
                return failure("Department not found"), HTTPStatus.NOT_FOUND

            user_data = data.get("user", {})
            user = User.query.get(student_id)
            to_update_user = {
                "name" : user_data.get('name'),
                "email" : user_data.get('email'),
            }
            if user:
                user.update(student_id, user_data)

            # Check if the interest already exists, if not, add it
            interest_data = data.get("interest", {})
            interest_name = interest_data.get('name')
            interest = Interest.get_by_name(interest_name)
            if not interest:
                interest = Interest(name=interest_name)
                new_interest = interest.insert()
            else:
                new_interest = interest

            student_data = data.get("student", {})
            to_update_student = {
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
            Student.update(student_id, to_update_student)

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


@api.route("/degrees")
class StudentDegreeResource(Resource):
    def get(self):
        return success(degrees, total_rows=len(degrees)), HTTPStatus.OK

@api.route("/cities")
class StudentDegreeResource(Resource):
    def get(self):
        cities = Student.query.distinct(Student.city).all()
        city_names = list(set([city.city for city in cities]))
        return success(city_names, total_rows=len(city_names)), HTTPStatus.OK
