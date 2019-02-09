from flask_restful import Resource, reqparse
from models.user_model import UserModel

class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email is a required field")
    parser.add_argument("password", type=str, required=True, help="Password is a required field")
    def get(self):
        data = RegisterUser.parser.parse_args()
        user = UserModel.find_by_email(data["email"])
        if user:
            return user.json()
        else:
            return {"message":"no user with that email exists"}, 404

    def post(self):
        data = RegisterUser.parser.parse_args()
        user = UserModel(**data)
        if(UserModel.find_by_email(data["email"])==None):
            try:
                user.save_to_db()
                return user.json(), 201
            except:
                return {"message" :"An error occurred while creating the user"}, 500
        else:
            return {"message": "User with that email already exists"}, 400


class GetAllUsers(Resource):
    def get(self):
        return {"users" : [user.json() for user in UserModel.query.all()]}