from server.app import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primarykey=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)