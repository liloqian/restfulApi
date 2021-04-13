from datetime import datetime as dt

from restfulApi import db


class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    author = db.Column(db.String(4), default="Unknown")
    publish_time = db.Column(db.DateTime, default=dt.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publish_time': self.publish_time.__str__()
        }
