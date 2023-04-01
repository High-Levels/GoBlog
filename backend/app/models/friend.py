from ._base import uuid,PrimaryKey,db,optional,Required,datetime
from .user import User

class Friend(db.Entity):
    _table_ = "tbl_friend"
    userOne = Required(User, column="id_user")
    userTwo = Required(User, column="id_user")
    dateFriend = Required(datetime, column = "date_friend")