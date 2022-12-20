# from flask_login import UserMixin

# from app import db
import mongoengine as me

# from apps.authentication.util import hash_pass
# from flask_login import UserMixin
import datetime
from bson import SON, DBRef, ObjectId


class BaseModel(me.Document):
    meta = {'allow_inheritance': True, 'abstract': True}

    def _is_string_convertible(self, dataobj):
        stringConvertibleClassTypes = [ObjectId, datetime.datetime, datetime.date]
        ll = list(map(lambda x: isinstance(dataobj, x), stringConvertibleClassTypes))
        return any(ll)

    def to_dict_resp(self):

        finalDict = {}
        for flds in self._fields:
            if str(flds).startswith('_'):
                pass
            else:
                if hasattr(self, flds):
                    fieldValue = getattr(self, flds)
                    if self._is_string_convertible(fieldValue):
                        finalDict[flds] = str(fieldValue)
                    else:
                        finalDict[flds] = fieldValue
                else:
                    pass
        return finalDict