from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLALchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.confir["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLALchemy(app)
ma = Marshmallow(app)

class Movie(db.model):
    __moviename__ = "Movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
