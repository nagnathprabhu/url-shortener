import os
from flask import Flask
from flask_restful import Api
import redis
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from dotenv import load_dotenv


load_dotenv()
# Initialize Redis
r = redis.Redis(host='localhost', port = 6379, db=0)

# Initialize Flask app
app = Flask(__name__)

# # Set JSON_AS_ASCII configuration variable to False
# app.config['JSON_AS_ASCII'] = False

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)