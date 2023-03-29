from ._base import Required,uuid,Set,db

class Tag(db.Entity):
    _table_ = "tbl_tag"
    idTag = Required(uuid.UUID,default = uuid.uuid4 ,column = 'id_tag')
    articleTag = Set('ArticleTag')
    name = Required(str,unique = True)
    