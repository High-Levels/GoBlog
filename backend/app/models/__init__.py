from ._base import db
from . import article,comment,user,articleCategory,articleTag,category,tag,content,like,friend,friendRequest,follow, notification
import os,uuid
from pony.orm import db_session,commit
from app.models.user import User
from datetime import datetime
db_params = {'provider': os.getenv('DB_PROVIDER'),
             'user': os.getenv('DB_USER'),
             'password': os.getenv('DB_PASSWORD'),
             'host': os.getenv('DB_HOST'),
             'database': os.getenv('DB_NAME')}

db.bind(**db_params)
db.generate_mapping(create_tables=True)

with db_session:
    try:
        
