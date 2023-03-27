from ._base import Optional,Required,PrimaryKey,Set,db,uuid, date


class User(db.Entity):
    _table_ = "tbl_user"
    idUser = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_user')
    username = Required(str, unique = True)
    email = Required(str, unique = True)
    password = Required(str)
    name = Optional(str,nullable = True)
    gender = Optional(str, nullable = True)
    address = Optional(str,nullable = True)
    birth = Optional(date, nullable = True)
    phoneNumber = Optional(str, column = "phone_number",nullable = True)
    dateRegister = Required(date,column = 'date_register')
    picture = Optional(str, nullable = True)
    article = Set('Article')
    comment = Set('Comment')
    like = Set('Like')
