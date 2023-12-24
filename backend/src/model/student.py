from datetime import datetime, timedelta

from common.enums import Activities
from helper.utils import create_activity
from model.base import Base, db
from model.department import Department
from model.interest import Interest
from sqlalchemy import Column, Date, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class Student(Base, db.Model):
    __tablename__ = "student"

    id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    department_id = Column(Integer, ForeignKey("department.id"))
    interest_id = Column(Integer, ForeignKey("interest.id"))
    roll_number = Column(String(20), unique=True, nullable=True)
    city = Column(String(50))
    gender = Column(String(10))
    dob = Column(Date)
    degree = Column(String(50), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)

    # Define the back references
    user = relationship("User", back_populates="student")
    department = relationship("Department", back_populates="student")
    interest = relationship("Interest", back_populates="student")

    @classmethod
    def get_by_roll_number(cls, roll_number):
        student = db.session.query(cls).filter(cls.roll_number == roll_number).first()
        return student

    @classmethod
    def get_top_interests(cls, limit=5):
        """
        Get the top N interests and their counts.

        :param limit: Number of top interests to retrieve
        :return: List of dictionaries with 'interest' and 'count'
        """
        top_interests = (
            db.session.query(Interest.name, func.count(Interest.name).label("count"))
            .join(Student)
            .group_by(Interest.name)
            .order_by(func.count(Interest.name).desc())
            .limit(5)
            .all()
        )

        return [
            {"interest": interest_name, "count": count}
            for interest_name, count in top_interests
        ]

    @classmethod
    def get_bottom_interests(cls, limit=5):
        """
        Get the bottom N interests and their counts.

        :param limit: Number of bottom interests to retrieve
        :return: List of dictionaries with 'interest' and 'count'
        """
        bottom_interests = (
            db.session.query(Interest.name, func.count(Interest.name).label("count"))
            .join(Student)
            .group_by(Interest.name)
            .order_by(func.count(Interest.name))
            .limit(5)
            .all()
        )

        return [
            {"interest": interest_name, "count": count}
            for interest_name, count in bottom_interests
        ]

    def insert_log(self):
        super().insert_log()
        create_activity(
            Activities.INSERT.name,
            Activities.INSERT.value + self.__tablename__ + " " + str(self.user.name),
        )

    def delete_log(self):
        super().delete_log()
        create_activity(
            Activities.DELETE.name,
            Activities.DELETE.value + self.__tablename__ + " " + str(self.user.name),
        )

    @classmethod
    def update_log(cls, id):
        super().update_log(id)
        create_activity(
            Activities.UPDATE.name,
            Activities.UPDATE.value + cls.__tablename__ + " " + str(id),
        )

    @classmethod
    def get_log(cls):
        super().get_log()
        create_activity(
            Activities.VIEW.name, Activities.VIEW.value + cls.__tablename__ + "s"
        )

    @classmethod
    def get_by_id_log(cls, id):
        super().get_by_id_log(id)
        create_activity(
            Activities.VIEW.name,
            Activities.VIEW.value + cls.__tablename__ + " with ID: " + str(id),
        )

    @classmethod
    def calculate_provincial_distribution(cls):
        """
        Calculate provincial distribution among students.

        :return: Dictionary with provincial distribution
        """
        distribution_query = (
            db.session.query(Student.city, func.count(Student.city).label("count"))
            .group_by(Student.city)
            .all()
        )

        distribution = {province: count for province, count in distribution_query}
        return distribution

    @classmethod
    def calculate_daily_creation_counts(cls):
        """
        Calculate the daily student creation counts for the last 30 days.

        :return: List of dictionaries with 'date' and 'count'
        """
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=30)

        counts_query = (
            db.session.query(
                func.date(Student.created_at).label("date"), func.count().label("count")
            )
            .filter(Student.created_at.between(start_date, end_date))
            .group_by(func.date(Student.created_at))
            .all()
        )

        counts = [
            {"date": date.strftime("%Y-%m-%d"), "count": count}
            for date, count in counts_query
        ]
        return counts

    @classmethod
    def calculate_age_distribution(cls):
        """
        Calculate the age distribution of students.

        :return: List of dictionaries with 'age' and 'count'
        """
        current_date = datetime.utcnow()

        age_distribution_query = (
            db.session.query(
                func.floor(func.datediff(current_date, Student.dob) / 365).label("age"),
                func.count().label("count"),
            )
            .group_by("age")
            .all()
        )

        age_distribution = [
            {"age": age, "count": count} for age, count in age_distribution_query
        ]
        return age_distribution

    @classmethod
    def calculate_department_distribution(cls):
        """
        Calculate the department distribution of students.

        :return: List of dictionaries with 'department' and 'count'
        """
        department_distribution = (
            Student.query.join(Department)
            .with_entities(Department.name, func.count().label("count"))
            .group_by(Department.name)
            .all()
        )
        return [
            {"department": department, "count": count}
            for department, count in department_distribution
        ]

    @classmethod
    def calculate_degree_distribution(cls):
        """
        Calculate the degree distribution of students.

        :return: List of dictionaries with 'degree' and 'count'
        """
        degree_distribution = (
            Student.query.with_entities(Student.degree, func.count().label("count"))
            .group_by(Student.degree)
            .all()
        )
        return [
            {"degree": degree, "count": count} for degree, count in degree_distribution
        ]

    @classmethod
    def calculate_gender_distribution(cls):
        """
        Calculate the gender distribution of students.

        :return: List of dictionaries with 'gender' and 'count'
        """
        gender_distribution = (
            Student.query.with_entities(Student.gender, func.count().label("count"))
            .group_by(Student.gender)
            .all()
        )
        return [
            {"gender": gender, "count": count} for gender, count in gender_distribution
        ]

    @classmethod
    def get_currently_studying_count(cls):
        """
        Get the number of students currently studying in the university.

        :return: Integer
        """
        currently_studying_count = Student.query.filter(
            Student.end_date > datetime.utcnow()
        ).count()
        return currently_studying_count

    @classmethod
    def get_recently_enrolled_count(cls, days=30):
        """
        Get the number of students recently enrolled.

        :param days: Number of days to consider for "recently enrolled"
        :return: Integer
        """
        start_date = datetime.utcnow() - timedelta(days=days)
        recently_enrolled_count = Student.query.filter(
            Student.start_date >= start_date
        ).count()
        return recently_enrolled_count

    @classmethod
    def get_about_to_graduate_count(cls, days=60):
        """
        Get the number of students about to graduate in 60 days.

        :param days: Number of days to consider for "about to graduate"
        :return: Integer
        """
        end_date = datetime.utcnow() + timedelta(days=days)
        about_to_graduate_count = Student.query.filter(
            Student.end_date >= datetime.utcnow(), Student.end_date <= end_date
        ).count()
        return about_to_graduate_count

    @classmethod
    def get_graduated_count(cls):
        """
        Get the number of students graduated.

        :param days: Number of days to consider for "graduated"
        :return: Integer
        """
        # end_date = datetime.utcnow() - timedelta(days=days)
        graduated_count = Student.query.filter(
            Student.end_date < datetime.utcnow()
        ).count()
        return graduated_count
