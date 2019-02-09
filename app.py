import os
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, request
from flask_cors import CORS
from models.tag_model import TagModel
from resources.users import RegisterUser, GetAllUsers
from resources.tag import Tag, TagList


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Bob'
api = Api(app)
@app.before_first_request
def create_tables():
    db.create_all()  

@app.route('/')
def index():
    return render_template("test.html")

api.add_resource(RegisterUser, "/register")
api.add_resource(GetAllUsers,"/users")
api.add_resource(Tag, "/tag/<name>")
api.add_resource(TagList, "/tags")
if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

