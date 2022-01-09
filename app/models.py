from app import db

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    content = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return 'Message {}'.format(self.title)