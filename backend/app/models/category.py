from ._base import Required,uuid,Set,db,PrimaryKey

class Category(db.Entity):
    _table_ = "tbl_category"
    idCategory = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_category')
    articleCategory = Set('ArticleCategory')
    name = Required(str,unique = True)
    