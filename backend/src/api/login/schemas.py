from flask_restx.fields import Integer, List, Nested, String

from . import api

user_model = api.model(
    "user_model",
    {
        "email": String(required=True, description="User email"),
        "password": String(required=True, description="User password"),
    },
    strict=True,
)

user_response = api.model(
    "user_response",
    {
        "status": String(description="ok|nok"),
        "object": Nested(user_model, skip_none=True, allow_null=True),
        "total_rows": Integer(),
        "errors": List(String),
    },
    strict=True,
)
