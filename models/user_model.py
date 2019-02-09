from db import db

class UserModel(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))

    tags = db.relationship("TagModel", lazy="dynamic")
    def json(self):
        return {"user":self.email, "tags" : [tag.json() for tag in self.tags.all()], "id" : self.id}

    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()