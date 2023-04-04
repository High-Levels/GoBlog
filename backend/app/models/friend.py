from ._base import uuid,PrimaryKey,db,Required,datetime
from .user import User

class Friend(db.Entity):
    _table_ = "tbl_friend"
    userOne = Required(User,column="id_user_one")
    userTwo = Required(User,column="id_user_two")
    dateFriend = Required(datetime,column="date_friend")