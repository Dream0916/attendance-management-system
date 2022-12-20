from flask_restful import Resource, Api, request, ResponseBase
from model.User import Users, OrgAdminUser, SuperAdminUser, OrgUser
from flask import Response, jsonify, make_response
from flask_jwt_extended import create_access_token
import json
from bson import SON, DBRef, ObjectId

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


def accountExists(accountId):
    usr = Users.objects(id=accountId)
    if usr.count() > 0:
        return usr
    else:
        return False

class UserResource(Resource):

    def delete(self):
        request_data = request.get_json()
        userId = request_data.get("userId",None)
        if userId:
            usrqs = Users.objects(id=userId)
            if usrqs.count() >0:
                usr = usrqs.first()
                usr.isDeleted = True
                usr.save()
                resp = jsonify(
                    {
                        "status": "OK",
                        "message": "User Deleted."
                    }
                )
                return make_response(resp)
            else:
                resp = jsonify(
                    {
                        "status":"ERROR",
                        "message": "No such User id exists"
                    }
                )
                return make_response(
                    resp,
                    422
                )
        else:
            resp = jsonify(
                {
                    "status": "ERROR",
                    "message": "userId is must mandatory field"
                }
            )
            return make_response(
                resp,
                422
            )


        pass


    def get(self):
        getarguments  = request.args
        # filterDict = {"email":'email@email.com','password':'password'}
        filterDict = {"isDeleted":False}

        if getarguments.get('isDeleted',None):
            filterDict['isDeleted'] = True if getarguments.get('isDeleted') == 'true' else False
            pass


        if getarguments.get('userType',None):
            filterDict['userType'] = getarguments.get('userType')
            pass

        userList = Users.objects.filter(**filterDict) #.no_dereference()

        usrLListSerralied = []

        for us in userList:
            dd = us.to_dict_resp()
            usrLListSerralied.append(dd)

        resp = {
            "status":"ok",
            "data": usrLListSerralied
        }
        return make_response(resp)


    def post(self):
        request_data = request.get_json()
        email = str(request_data.get("email")).strip() if request_data.get('email',None) else None
        password = str(request_data.get("password")).strip()
        username = str(request_data.get("username")).strip() if request_data.get('username',None) else None

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


class OrgUserResource(Resource):



    def post(self):
        request_data = request.get_json()
        email = str(request_data.get("email")).strip() if request_data.get('email',None) else None
        password = str(request_data.get("password")).strip()
        username = str(request_data.get("username")).strip() if request_data.get('username',None) else None
        accountId = str(request_data.get("accountId")).strip() if request_data.get('accountId', None) else None

        acntData = accountExists(accountId=accountId)

        if not acntData:
            resp = jsonify(
                {
                    "status":"ERROR",
                    "message": "parent Account does not exist for this user"
                }
            )
            return make_response(
                resp,
                422
            )



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
            s = OrgUser(email=email, password=password,accountId=acntData.first()).save()
            print(s.id)
            return make_response(jsonify({"status":"OK","message":"User add succesfull"}))
            # return Response(response="registration successfull")





class AdminDebugUserResource(Resource):
    def post(self):
        request_data = request.get_json()
        email = str(request_data.get("email")).strip() if request_data.get('email',None) else None
        password = str(request_data.get("password")).strip()
        username = str(request_data.get("username")).strip() if request_data.get('username',None) else None
        userType = str(request_data.get("userType")).strip() if request_data.get('userType', None) else None

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
            if userType == 'SUPER-ADMIN':
                s = SuperAdminUser(email=email, password=password).save()
                print(s.id)
                return make_response(jsonify({"status": "OK","message": "registration succesfull"}))
            elif userType == "ORG-USER":
                s = OrgUser(email=email, password=password).save()
                print(s.id)
                return make_response(jsonify({"status": "OK", "message": "registration succesfull"}))
            else:
                s = OrgAdminUser(email=email, password=password).save()
                print(s.id)
                return make_response(jsonify({"status": "OK", "message": "registration succesfull"}))

            # return Response(response="registration successfull")







