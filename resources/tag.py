from flask_restful import Resource, reqparse
from models.tag_model import TagModel


class Tag(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("user_id", type=int, required=True, help= "Every item needs a user id.")

    def get(self, name):
        tag = TagModel.find_by_tagName(name)
        if tag:
            return tag.json()
        else:
            return {"message":"item not found"}, 404

    def post(self, name):
        data = Tag.parser.parse_args()
        if TagModel.find_by_tagName(name):
            return {"Message": f"An tag with name {name} already exists"}, 404
        tag = TagModel(name, data["user_id"])
        try: 
            tag.save_to_db()
        except:
            return {"message" : "An error occurred inserting the item"}, 500
        return tag.json()

class TagList(Resource):
    def get(self):
        return {"tags":[tag.json() for tag in TagModel.query.all()]}
