from ._base import Required,PrimaryKey,db,uuid,datetime
from .user import User
from pony.converting import str2datetime

class FriendRequest(db.Entity):
    _table_ = "tbl_friend_request"
    sender = Required(User,column='id_user_sender')
    recipient = Required(User,column='id_user_recipient')
    dateFriendRequest = Required(datetime,column="date_friend_request")