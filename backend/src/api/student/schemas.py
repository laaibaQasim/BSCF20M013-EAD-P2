from flask_restx.fields import Integer, List, Nested, String, Date

from . import api

student_model = api.model(
    "student_model",
    {
        "ID": Integer(description="Student ID"),
        "name": String(description="Student name"),
        "email": String(description="Student email"),
        "roll_number": String(description="Student roll number"),
        "department": String(description="Student department"),
        "degree": String(description="Student degree"),
        "dob": Date(description="Student date of birth"),
        "city": String(description="Student city"),
        "interest": String(description="Student interest"),
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
