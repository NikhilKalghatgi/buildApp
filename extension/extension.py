from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from flask_restful import Api
# from flask.ext.login import LoginManager

cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy(session_options={"expire_on_commit": False})
mongo_db = MongoEngine()
api = Api()
# login_manager = LoginManager()


