from flask import Flask, session
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

# from flask_login import LoginManager
# from flask_mongoengine import MongoEngine

# from apscheduler.schedulers.background import BackgroundScheduler
# from batchjobs.bitrix_indiamart_ingestor import indiaMartingestor
# from flask_session import Session


## CONTROLER ROUTES ###
from controller.register import TestResource, RegisterAccountResource, LoginAccountResource
from controller.user import UserResource, AdminDebugUserResource, OrgUserResource
from configuration.database import db



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "ABGBHDGVFHG12343"
api = Api(app)
jwt = JWTManager(app)

# app.config["SESSION_PERMANENT"] = True
# app.config["SESSION_TYPE"] = "filesystem"
# app.config["secret_key"] = "1234321"
# Session(app)
# app.secret_key = '123456789qwertyABCDF'
# Session(app)

api.add_resource(TestResource,'/api/v1/test')
api.add_resource(RegisterAccountResource,'/api/v1/register')
api.add_resource(LoginAccountResource,'/api/v1/login')
api.add_resource(UserResource,'/api/v1/user')
api.add_resource(OrgUserResource,'/api/v1/orguser')
api.add_resource(AdminDebugUserResource,'/api/v1/debug/user')
# app.add_url_rule("/","index",about)
# app.add_url_rule('/', 'index', home , methods=['GET'])
# app.add_url_rule('/health', 'health', health , methods=['GET'])
# app.add_url_rule('/login', 'login', login , methods=['GET','POST'])
# app.add_url_rule('/register', 'register', register , methods=['GET','POST'])
# app.add_url_rule('/buttons', 'buttons', buttons , methods=['GET','POST'])
# app.add_url_rule('/checkloginusername', 'checkloginusername', checkUserlogin , methods=['POST'])
# app.add_url_rule('/checkloginpassword', 'checkloginpassword', checkUserpassword , methods=['POST'])
# app.add_url_rule('/bitrix-indiamart', 'bitrix-indiamart', bitrixIndiaMart , methods=['GET','POST'])
#
#
#
#
# from views import *





def initialiseDb(app):
    app.config['MONGODB_SETTINGS'] = [{
        'db': 'atndmgmnt',
        'host': 'localhost',
        'port': 27017
    }]
    db.init_app(app)


if __name__ == "__main__":

    # sched = BackgroundScheduler(daemon=True)
    # sched.add_job(indiaMartingestor, 'interval', minutes=20)
    # sched.start()
    initialiseDb(app)

    app.run(debug="true",use_reloader=False)