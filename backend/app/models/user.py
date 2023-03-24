from ._base import Required,PrimaryKey,Set,db,uuid

class User(db.Entity):
    _table_ = "tbl_user"
    idUser = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_user')
    name = Required(str)
    article = Set('Article')
    comment = Set('Comment')
    like = Set('Like')