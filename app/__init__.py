from flask import Flask
from config import Config
from .auth.routes import auth
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from .models import db, User
from .api.routes import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app, db)

# enabling login persistence
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login.init_app(app)

login.login_view = 'auth.login'

from . import routes
from . import models