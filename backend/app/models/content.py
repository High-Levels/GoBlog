from ._base import Required,uuid,Set,db, Optional

class Content(db.Entity):
    _table_ = "tbl_content"
    id_content = Required(uuid.UUID,default = uuid.uuid4 ,column = 'id_content')
    article = Set('Article')
    title = Required(str)
    subtitle = Optional(str)
    img = Optional(str)
    captions = Optional(str)
    contentBody = Required(str, column = "content_body")