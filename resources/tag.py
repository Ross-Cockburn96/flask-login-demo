from flask_restful import Resource
from models.tag_model import TagModel


class Tag(Resource):
    def get(self, name):
        tag = TagModel.find_by_tagName(name)
        if tag:
            return tag.json()
        else:
            return {"message":"item not found"}, 404
    
    def post(self, name):
        if TagModel.find_by_tagName(name):
            return {"Message": f"An tag with name {name} already exists"}, 404
        tag = TagModel(name)
        try: 
            tag.save_to_db()
        except:
            return {"message" : "An error occurred inserting the item"}, 500
        return tag.json()

class TagList(Resource):
    def get(self):
        return {"tags":[tag.json() for tag in TagModel.query.all()]}
