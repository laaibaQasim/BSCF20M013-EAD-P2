from flask_restx.fields import Date, Integer, List, Nested, String
from ..department.schemas import department_model
from ..interest.schemas import interest_model

from . import api

user_model = api.model(
    "user_model",
    {
        "name": String(description="Department name"),
        "email": String(description="Email address"),
    },
)

student_model = api.model(
    "student_model",
    {
        "id": Integer(description="Student ID"),
        "user": Nested(user_model, description="Student name"),
        "roll_number": String(description="Student roll number"),
        "department": Nested(department_model, description="Student department"),
        "degree": String(description="Student degree"),
        "dob": Date(description="Student date of birth"),
        "city": String(description="Student city"),
        "interest": Nested(interest_model, description="Student interest"),
        "gender": String(description="Student gender"),
        "start_date": Date(description="Student start date"),
        "end_date": Date(description="Student end date"),
    },
)

student_response = api.model(
    "student_response",
    {
        "status": String(description="ok|nok"),
        "object": Nested(student_model, skip_none=True, allow_null=True),
        "total_rows": Integer(),
        "errors": List(String),
    },
)
