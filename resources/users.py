from flask_restful import Resource, reqparse
from models.user_model import UserModel

class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email is a required field")
    parser.add_argument("password", type=str, required=True, help="Password is a required field")
    
    def get(self):
        data = RegisterUser.parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if (user):
            return user.json()
        else:
            return {"message" :  "user not found"}
    def post(self):
        data = RegisterUser.parser.parse_args()
        print(data)
        if(UserModel.find_by_email(data["email"])==None):
            print(**data)
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User created successfully"}, 201
        else:
            return {"message": "User with that email already exists"}, 400
