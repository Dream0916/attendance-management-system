from flask_restful import Resource, Api, request, ResponseBase
from model.User import Users, OrgAdminUser
from flask import Response, jsonify, make_response
from flask_jwt_extended import create_access_token

class TestResource(Resource):
    def get(self):
        return {'hello': 'world'}

def emailExists(email:str):
    usr = Users.objects(email=email)
    if usr.count() >0:
        return usr
    else:
        return False

def userExists(email:str,password:str):
    usr = Users.objects(email=email)
    if usr.count() >0:
        return usr
    else:
        return False

def getUserWithCred(email, password):
    usr = Users.objects(email=email, password=password).exclude("password")
    if usr.count() > 0:
        return usr
    else:
        return False


class RegisterAccountResource(Resource):
    def post(self):
        request_data = request.get_json()
        email = str(request_data.get("email")).strip()
        password = str(request_data.get("password")).strip()
        if emailExists(email=email):
            resp = jsonify(
                {
                    "status":"ERROR",
                    "message": "User already exists"
                }
            )
            return make_response(
                resp,
                409
            )
        else:
            s = OrgAdminUser(email=email, password=password).save()
            print(s.id)
            return make_response(jsonify({"status":"OK","message":"registration succesfull"}))
            # return Response(response="registration successfull")


class LoginAccountResource(Resource):
    def post(self):
        request_data = request.get_json()
        reqemail = str(request_data.get("email")).strip()
        reqpassword = str(request_data.get("password")).strip()
        ue = getUserWithCred(email=reqemail,password=reqpassword)

        if ue :
            ueobj = ue.first()
            tokenPayLoad = {
                "id": str(ueobj.id),
                "email": ueobj.email,
                "userType": ueobj.userType
            }
            print(tokenPayLoad)
            token = create_access_token(tokenPayLoad)
            resp = jsonify(
                {
                    "status":"OK",
                    "message": "Login Succesfull",
                    "token":token,
                    "userId": str(ueobj.id),
                    "userType": ueobj.userType
                }
            )
            return make_response(resp)
        else:
            return make_response(jsonify({"status":"ERROR","message":"Login Failed, User email or password did not match"}),401)
            # return Response(response="registration successfull")


