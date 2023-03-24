from ._base import Required,PrimaryKey,db,uuid
from .user import User
from .article import Article

class Like(db.Entity):
    _table_ = "tbl_like"
    idLike = PrimaryKey(uuid.UUID,default = uuid.uuid4,column = 'id_like')
    user = Required(User, column = 'id_user')
    article = Required(Article, column = 'id_article')
    like =  Required(bool)