from ._base import Required,PrimaryKey,db,uuid
from .user import User
from .article import Article

class Comment(db.Entity):
    _table_ = "tbl_comment"
    idComment = PrimaryKey(uuid.UUID,default = uuid.uuid4,column = 'id_comment')
    user = Required(User, column = 'id_user')
    article = Required(Article, column = 'id_article')
    comment =  Required(str)