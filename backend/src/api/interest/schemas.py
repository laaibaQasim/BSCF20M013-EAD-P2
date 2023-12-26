from flask_restx.fields import Integer, List, Nested, String

from . import api

interest_model = api.model(
    "interest_model",
    {
        "name": String(required=True, description="Interest name"),
    },
    strict=True,
)
interest_response = api.model(
    "interest_response",
    {
        "status": String(description="ok|nok"),
        "object": Nested(interest_model, skip_none=True, allow_null=True),
        "total_rows": Integer(),
        "errors": List(String),
    },
    strict=True,
)
