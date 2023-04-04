from ._base import Required,PrimaryKey,Set,db,uuid
from .user import User
from datetime import datetime

class Follow(db.Entity):
    _table_ = "tbl_follow"
    source = Required(User, column="source")
    target = Required(User, column="target")
    dateFollow = Required(datetime, column="date_follow")