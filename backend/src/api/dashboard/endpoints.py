from flask import request, jsonify
from flask_restx import Resource
from http import HTTPStatus

from api.dashboard import schemas
from model.interest import Interest
from model.student import Student
from model.user_activity import UserActivity

from helper.response import success, failure

from . import api


@api.route("/top-interests")
class TopInterestsResource(Resource):
    def get(self):
        """
        Get top 5 interests among students.

        :return: Top 5 Interests
        """
        try:
            # Call the class method to get top interests
            top_interests = Student.get_top_interests()

            return success(top_interests, len(top_interests)), HTTPStatus.OK

        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/bottom-interests")
class BottomInterestsResource(Resource):
    def get(self):
        """
        Get bottom 5 interests among students.

        :return: Bottom 5 Interests
        """
        try:
            # Call the class method to get top interests
            bottom_interests = Student.get_bottom_interests()

            return success(bottom_interests, len(bottom_interests)), HTTPStatus.OK

        except Exception as e:
            return failure(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/provincial-distribution")
class ProvincialDistributionResource(Resource):
    def get(self):
        """
        Get provincial distribution among students.

        :return: Provincial distribution data
        """
        distribution = Student.calculate_provincial_distribution()
        if distribution:
            return success(distribution, len(distribution)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/submission-chart")
class SubmissionChartResource(Resource):
    def get(self):
        """
        Get daily student creation counts for the last 30 days.

        :return: List of dictionaries with 'date' and 'count'
        """
        counts = Student.calculate_daily_creation_counts()
        if counts:
            return success(counts, len(counts)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/age-distribution")
class AgeDistributionResource(Resource):
    def get(self):
        """
        Get the age distribution of students.

        :return: List of dictionaries with 'age' and 'count'
        """
        age_distribution = Student.calculate_age_distribution()
        if age_distribution:
            return success(age_distribution, len(age_distribution)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/department-distribution")
class DepartmentDistributionResource(Resource):
    def get(self):
        """
        Get the department distribution of students.

        :return: List of dictionaries with 'department' and 'count'
        """
        department_distribution = Student.calculate_department_distribution()
        if department_distribution:
            return (
                success(department_distribution, len(department_distribution)),
                HTTPStatus.OK,
            )
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/degree-distribution")
class DegreeDistributionResource(Resource):
    def get(self):
        """
        Get the degree distribution of students.

        :return: List of dictionaries with 'degree' and 'count'
        """
        degree_distribution = Student.calculate_degree_distribution()
        if degree_distribution:
            return success(degree_distribution, len(degree_distribution)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/gender-distribution")
class GenderDistributionResource(Resource):
    def get(self):
        """
        Get the gender distribution of students.

        :return: List of dictionaries with 'gender' and 'count'
        """
        gender_distribution = Student.calculate_gender_distribution()
        if gender_distribution:
            return success(gender_distribution, len(gender_distribution)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/last_30_days_activity")
class Last30DaysActivityResource(Resource):
    def get(self):
        """
        Get the number of actions performed daily for the last 30 days.
        :return: List of dictionaries with 'date' and 'count'
        """
        result = UserActivity.calculate_last_30_days_activity()
        print(result)
        if result:
            return success(result, len(result)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/last_24_hours_activity")
class Last24HoursActivityResource(Resource):
    def get(self):
        """
        Get the number of actions performed every 15 minutes for the last 24 hours.
        :return: List of dictionaries with 'time' and 'count'.
        """
        data = UserActivity.calculate_last_24_hours_activity()
        if data:
            return success(data, len(data)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND


@api.route("/active-hours")
class MostActiveHoursResource(Resource):
    def get(self):
        most_active_hours = UserActivity.get_most_active_hours()
        least_active_hours = UserActivity.get_least_active_hours()
        dead_hours = UserActivity.get_dead_hours()
        res = {
            "Most Active Hours": most_active_hours,
            "Least Active Hours": least_active_hours,
            "Dead Hours": dead_hours,
        }
        if most_active_hours:
            return success(res, len(res)), HTTPStatus.OK
        else:
            return failure("No data found"), HTTPStatus.NOT_FOUND
