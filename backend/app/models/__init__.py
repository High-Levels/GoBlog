from ._base import db
from . import article,comment,user,articleCategory,articleTag,category,tag,content,like,friend,friendRequest
import os

db_params = {'provider': os.getenv('DB_PROVIDER'),
             'user': os.getenv('DB_USER'),
             'password': os.getenv('DB_PASSWORD'),
             'host': os.getenv('DB_HOST'),
             'database': os.getenv('DB_NAME')}

db.bind(**db_params)
db.generate_mapping(create_tables=True)
