from ._base import Optional,Required,PrimaryKey,Set,db,uuid, date


class User(db.Entity):
    _table_ = "tbl_user"
    idUser = PrimaryKey(uuid.UUID,default = uuid.uuid4 ,column = 'id_user')
    username = Required(str, unique = True)
    email = Required(str, unique = True)
    # if registered with google,
    # username will be random uuid,
    # and password will be empty string
    password = Required(str)
    # if linked with google,
    # the linked email will be here
    googleEmail = Optional(str)
    name = Optional(str,nullable = True)
    gender = Optional(str, nullable = True)
    address = Optional(str,nullable = True)
    birth = Optional(date, nullable = True)
    phoneNumber = Optional(str, column = "phone_number",nullable = True)
    dateRegister = Required(date,column = 'date_register')
    picture = Optional(str, nullable = True)
    isActivated = Required(bool)
    article = Set('Article')
    comment = Set('Comment')
    like = Set('Like')
    friendUserOne = Set('Friend', reverse="userOne")
    friendUserTwo = Set('Friend', reverse="userTwo")
    friendRequestSender = Set('FriendRequest', reverse="sender")
    friendRequestRecipient = Set('FriendRequest', reverse="recipient")
    followSource = Set("Follow", reverse="source")
    followTarget = Set("Follow", reverse="target")
    notificationReceiver = Set("Notification", reverse="receiver")