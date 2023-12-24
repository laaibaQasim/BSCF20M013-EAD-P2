from flask import Flask
from flask_cors import CORS

from api import blueprint
from config import settings
from model.base import db

from model.department import Department
from model.user import User
from model.interest import Interest
from model.role import Role
from model.student import Student
from model.user_activity import UserActivity

from common.lists import degrees
from common.enums import Departments, Roles, Activities
from common.context import CurrentUser


import random
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship


def generate_dummy_data():
    # Dummy interests
    interest_names = [
        "Math",
        "Artificial Intelligence",
        "Machine Learning",
        "Science",
        "Art",
        "Sports",
        "Music",
        "Coding",
        "Literature",
        "History",
        "Languages",
        "Painting",
    ]
    interests = [Interest(name=name) for name in interest_names]

    # Dummy departments
    department_names = [
        Departments.CS.value,
        Departments.IT.value,
        Departments.ME.value,
        Departments.SE.value,
        Departments.ARTS.value,
    ]
    departments = [Department(name=name) for name in department_names]

    # Dummy users
    for _ in range(25):
        user = User(
            name=f"User {random.randint(1000, 9999)}",
            email=f"user{random.randint(1000, 9999)}@example.com",
            password="pucit",
            role_id=2,
        )
        db.session.add(user)

    # Commit interests, departments, degrees, and users to the database
    for interest in interests:
        interest.insert()

    for department in departments:
        department.insert()

    # Generate dummy students
    for user in User.get():
        name = user.name
        email = user.email
        password = user.password
        birth_date = datetime.now() - timedelta(days=random.randint(18 * 365, 22 * 365))
        interest = random.choice(interests)
        department = random.choice(departments)
        degreec = random.choice(degrees)

        student = Student(
            user=user,
            department=department,
            interest=interest,
            roll_number=f"R{random.randint(1000, 9999)}",
            city=f"City{random.randint(1, 10)}",
            gender=random.choice(["Male", "Female"]),
            dob=birth_date,
            degree=degreec,
            start_date=datetime.now() - timedelta(days=random.randint(365, 1800)),
            end_date=datetime.now() + timedelta(days=random.randint(180, 365)),
        )

        student.insert()


def add_dummy_data():
    with app.app_context():
        db.drop_all()
        db.session.commit()
        db.create_all()
        db.session.commit()
    role1 = Role(name=Roles.ADMIN)
    role1.insert()
    role2 = Role(name=Roles.STUDENT)
    role2.insert()

    role = db.session.query(Role).filter_by(name=Roles.ADMIN).first()
    new_user = User(name="laiba", email="l", password="admin", role=role)
    new_user.insert()

    CurrentUser.cuser = new_user
    CurrentUser.role_name = Roles.ADMIN


app = Flask(__name__, static_folder="/static")
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = settings.database_uri
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CORS_HEADERS"] = "Content-Type"

app.register_blueprint(blueprint, url_prefix="/")
db.init_app(app)
CORS(app, max_age=600)

if __name__ == "__main__":
    # add_dummy_data()
    # generate_dummy_data()

    app.run(debug=True, port=5000)
