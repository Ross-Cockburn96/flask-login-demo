import os
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite://data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Bob'
api = Api(app)

if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)