from .. import mdb

GENDER = ('MALE', 'FEMALE')
STATUS = ('VERIFIED', 'UNVERIFIED')


class Users(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    name = mdb.StringField()
    email = mdb.EmailField()
    password = mdb.StringField()
    passwordSalt = mdb.StringField()
    status = mdb.StringField(choices=STATUS, default='UNVERIFIED')
    gender = mdb.StringField(choices=GENDER)
    age = mdb.IntField()
    website = mdb.StringField()
    introduction = mdb.StringField()
