from ._base import Required,PrimaryKey,db,uuid, datetime
from .user import User
from .article import Article

class Comment(db.Entity):
    _table_ = "tbl_comment"
    idComment = PrimaryKey(uuid.UUID,default = uuid.uuid4,column = 'id_comment')
    user = Required(User, column = 'id_user')
    article = Required(Article, column = 'id_article')
    commentBody =  Required(str, column = "comment_body")
    dateComment = Required(datetime, column = "date_comment")