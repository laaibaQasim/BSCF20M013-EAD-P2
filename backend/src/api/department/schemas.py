from flask_restx.fields import Integer, List, Nested, String
from . import api

department_model = api.model(
    "department_model",
    {
        "name": String(required=True, description="Department name"),
    },
    strict=True,
)

department_response = api.model(
    "department_response",
    {
        "status": String(description="ok|nok"),
        "object": Nested(department_model, skip_none=True, allow_null=True),
        "total_rows": Integer(),
        "errors": List(String),
    },
    strict=True,
)
