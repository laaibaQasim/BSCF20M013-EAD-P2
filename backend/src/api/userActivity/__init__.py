from flask_restx import Namespace

api = Namespace("Log", description="Log User Activity", path="/log")