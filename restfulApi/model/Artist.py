from datetime import datetime

from restfulApi import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birth = db.Column(db.DateTime, default=datetime.utcnow)
    city = db.Column(db.String(20))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth': self.birth.__str__(),
            'city': self.city
        }
