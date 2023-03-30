from flask import Flask
from pony.flask import Pony
from .models._base import db
import re,os
from flask_jwt_extended import JWTManager
import cloudinary
from flask_mail import Mail



app = Flask(__name__)

JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")

#UPLOAD
app.config['UPLOAD_FOLDER_BOOKS'] = os.getenv("UPLOAD_FOLDER_BOOKS")
app.config['UPLOAD_FOLDER_USERS'] = os.getenv("UPLOAD_FOLDER_USERS")
app.config['MAX_CONTENT_LENGHT'] = os.getenv("MAX_CONTENT_LENGHT")
app.config['ALLOWED_EXTENSIONS'] = os.getenv("ALLOWED_EXTENSION")
allowedextensions = app.config['ALLOWED_EXTENSIONS']
uploadFolderBooks = app.config['UPLOAD_FOLDER_BOOKS']
uploadFolderUsers = app.config['UPLOAD_FOLDER_USERS']
uploadFolderContents = app.config['UPLOAD_FOLDER_USERS']

cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "upgradelvel@gmail.com"
app.config['MAIL_PASSWORD'] = "ftokyweuyhcgkyia"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



Pony(app)
mail = Mail(app)


from app import routes
if __name__ == "__main__":
    app.run()