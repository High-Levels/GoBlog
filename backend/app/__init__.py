from flask import Flask
from pony.flask import Pony
from .models._base import db



app = Flask(__name__)



Pony(app)


from app import routes
if __name__ == "__main__":
    app.run()