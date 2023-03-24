from ._base import Required,uuid,Set,db

class Category(db.Entity):
    _table_ = "tbl_categoy"
    idCategory = Required(uuid.UUID,default = uuid.uuid4 ,column = 'id_category')
    articleCategory = Set('ArticleCategory')
    name = Required(str)
    