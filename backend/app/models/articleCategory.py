from ._base import Required,PrimaryKey,Set,db,uuid
from .category import Category
from .article import Article


class ArticleCategory(db.Entity):
    _table_ = "tbl_article_category"
    idArticleCategory = Required(uuid.UUID,default = uuid.uuid4 ,column = 'id_article_category')
    category = Required(Category,column='id_category')
    article = Required(Article,column='id_article')