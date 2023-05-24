from flask import Flask
from pony.flask import Pony
from .models._base import db
import re,os
from flask_jwt_extended import JWTManager
import cloudinary
from flask_mail import Mail
from flask_cors import CORS
import os
from flask_wtf import CSRFProtect
from app.prefixMiddleware import PrefixMiddleware

from flask_cors import CORS

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api/blog')
CORS(app)
# CSRFProtect(app)
CSRF_TOKEN_SECRET_KEY = os.urandom(32)
JWTManager(app)


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")

#UPLOAD
app.config['UPLOAD_FOLDER_BOOKS'] = os.getenv("UPLOAD_FOLDER_BOOKS")
app.config['UPLOAD_FOLDER_USERS'] = os.getenv("UPLOAD_FOLDER_USERS")
app.config['MAX_CONTENT_LENGHT'] = os.getenv("MAX_CONTENT_LENGHT")
app.config['ALLOWED_EXTENSIONS'] = os.getenv("ALLOWED_EXTENSION")
app.config['UPLOAD_FOLDER_ARTICLES'] = os.getenv("UPLOAD_FOLDER_ARTICLES")
allowedextensions = app.config['ALLOWED_EXTENSIONS']
uploadFolderBooks = app.config['UPLOAD_FOLDER_BOOKS']
uploadFolderUsers = app.config['UPLOAD_FOLDER_USERS']
uploadFolderContents = app.config['UPLOAD_FOLDER_ARTICLES']

cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "upgradelvel@gmail.com"
app.config['MAIL_PASSWORD'] = "ftokyweuyhcgkyia"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



Pony(app)
CORS(app)
mail = Mail(app)


from app import routes
if __name__ == "__main__":
    app.run()