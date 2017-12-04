from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True, unique=False)
    body = db.Column(db.Text, index=False, unique=False)

    def __repr__(self):
        return '<Message # {} by {}>'.format(str(self.id), self.author)
