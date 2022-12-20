# from flask_login import UserMixin

# from app import db
import mongoengine as me

# from apps.authentication.util import hash_pass
# from flask_login import UserMixin
import datetime
from bson import SON, DBRef, ObjectId

from model.base import BaseModel

class Users(BaseModel):
    meta = {'collection': 'User','allow_inheritance': True}
    username = me.StringField()
    email = me.StringField(required=True)
    password = me.StringField(required=True)
    # userType = me.StringField(default="ORG-ADMIN")
    firstName = me.StringField()
    lastName = me.StringField()
    address = me.StringField()
    isDeleted = me.BooleanField(default=False)
    isActive = me.BooleanField(default=False)


class OrgAdminUser(Users):
    # meta = {'collection': 'User'}
    userType = me.StringField(default="ORG-ADMIN")
    companyName = me.StringField()
    companyAddress = me.StringField()
    companyLogo = me.StringField()
    accountId = me.ReferenceField(Users, default=None)

class SuperAdminUser(Users):
    # meta = {'collection': 'User'}
    # meta = {'allow_inheritance': False}
    userType = me.StringField(default="SUPER-ADMIN")

class OrgUser(Users):
    # meta = {'collection': 'User'}

    # meta = {'allow_inheritance': False}
    userType = me.StringField(default="ORG-USER")
    accountId = me.ReferenceField(OrgAdminUser)
