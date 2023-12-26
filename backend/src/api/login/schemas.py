from flask_restx.fields import Integer, List, Nested, String

from . import api

login_model = api.model(
    "login_model",
    {
        "email": String(required=True, description="User email"),
        "password": String(required=True, description="User password"),
    },
    strict=True,
)

login_response = api.model(
    "login_response",
    {
        "status": String(description="ok|nok"),
        "object": Nested(login_model, skip_none=True, allow_null=True),
        "total_rows": Integer(),
        "errors": List(String),
    },
    strict=True,
)
