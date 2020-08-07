import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "data.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
# get notified before and after changes are committed to the database
# models_committed and before_models_committed
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/signals/
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
