from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def get_id(self):
        return str(self.user_id)



class Bookmark(db.Model):
    bookmark_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)

    creation_datetime = db.Column(db.DateTime)

