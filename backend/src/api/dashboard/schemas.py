from flask_restx.fields import Integer, List, Nested, String

from . import api

activity_model = api.model(
    'Activity',
    {
    'date': String(required=True, description='Date of activity'),
    'count': Integer(required=True, description='Number of actions'),
    },
    strict=True,
)