from .. import mdb

# GENDER = ('MALE', 'FEMALE')
STATUS = ('VERIFIED', 'UNVERIFIED', 'INACTIVE')


class Admin(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    name = mdb.StringField()
    email = mdb.EmailField()
    password = mdb.StringField()
    passwordSalt = mdb.StringField()
    status = mdb.StringField(choices=STATUS, default='VERIFIED')
    # gender = mdb.StringField(choices=GENDER)
    # age = mdb.IntField()
    role = mdb.StringField(default='ADMIN')
    # website = mdb.StringField()
    # introduction = mdb.StringField()
