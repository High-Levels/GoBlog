from ._base import Required,PrimaryKey,db,uuid,datetime
from .user import User
from datetime import datetime

class Notification(db.Entity):
    idNotification = PrimaryKey(uuid.UUID, column="id_notification")
    receiver = Required(User, column="receiver")
    notificationType = Required(str, column="notification_type")
    alreadyRead = Required(bool, column="already_read", default=False)
    # each different type of notification might have different data
    # for example in friend request notification, there is data about who send it and when
    # in new article notification, there is data about who created the article and the title of the new article
    # ect...
    # store the data required by the notification type in json format (string)
    notificationJson = Required(str, column="notification_json")
    notificationDate = Required(datetime, default=datetime.now(), column="notification_datetime")