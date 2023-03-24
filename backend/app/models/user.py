from ._base import Required,PrimaryKey,Set,db,uuid, date


class User(db.Entity):
    _table_ = "tbl_user"
    idUser = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_user')
    name = Required(str)
    article = Set('Article')
    comment = Set('Comment')
    like = Set('Like')
    address = Required(str)
    gender = Required(str)
    birth = Required(date)
    phoneNumber = Required(str, column = "phone_number")
    email = Required(str, unique = True)
    username = Required(str, unique = True)
    password = Required(str)

