from ._base import Required,uuid,Set,db

class Content(db.Entity):
    _table_ = "tbl_content"
    id_content = Required(uuid.UUID,default = uuid.uuid4 ,column = 'id_content')
    article = Set('Article')