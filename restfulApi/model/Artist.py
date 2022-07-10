from datetime import datetime

from restfulApi.app import db


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


# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     # 关系属性, cascade级联操作
#     articles = db.relationShip('Book', back_populates='Author', cascade='save-update, merge, delete')
#
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     edit_time = db.Column(db.Integer, default=0)
#     # 外键
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
#     author = db.relationShip('Author', back_populates='Book')
#
#
# @db.event.listens_for(Book.name, 'set')
# def increase_edit_time(**kwargs):
#     if kwargs['target'].edit_time is not None:
#         kwargs['target'].edit_time += 1
