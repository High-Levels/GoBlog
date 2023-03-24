from ._base import Required,PrimaryKey,Set,db,uuid
from .user import User
from .content import Content

class Article(db.Entity):
    _table_ = "tbl_article"
    idArticle = PrimaryKey(uuid.UUID,default=uuid.uuid4,column = 'id_article')
    comment = Set('Comment')
    like = Set('Like')
    articleTag = Set('ArticleTag')
    articleCategory = Set('ArticleCategory')
    user = Required(User,column = 'id_user')
    content = Required(Content,column = 'id_content')
    
