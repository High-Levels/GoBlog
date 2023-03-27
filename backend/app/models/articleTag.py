from ._base import Required,uuid,db,PrimaryKey
from .tag import Tag
from .article import Article


class ArticleTag(db.Entity):
    _table_ = "tbl_article_tag"
    idArticleTag = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_article_tag')
    tag = Required(Tag,column='id_tag')
    article = Required(Article,column='id_article')