from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Init app
app = Flask(__name__)

app.config['SECRET_KEY'] = '0cf4aa52f1791e54ef2e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init bcrypt
bcrypt = Bcrypt(app)
# Init login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from exams import routes
