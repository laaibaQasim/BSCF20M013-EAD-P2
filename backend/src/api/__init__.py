from flask import Blueprint
from flask_restx import Api

from .dashboard.endpoints import api as dashboard_api
from .department.endpoints import api as department_api
from .interest.endpoints import api as interest_api
from .login.endpoints import api as login_api
from .student.endpoints import api as student_api
from .logout.endpoints import api as logout_api
from .userActivity.endpoints import api as user_activity_api

blueprint = Blueprint("api", __name__)

authorizations = {
    "Authorization": {
        "description": "",
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

api = Api(
    blueprint,
    title="SIS API",
    version="0.1",
    description="Student Interest System APIs",
    authorizations=authorizations,
    security="Authorization",
)

api.add_namespace(login_api)
api.add_namespace(student_api)
api.add_namespace(department_api)
api.add_namespace(interest_api)
api.add_namespace(dashboard_api)
api.add_namespace(logout_api)
api.add_namespace(user_activity_api)
