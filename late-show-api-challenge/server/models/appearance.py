from server.app import db

class Appearance(db.Model):
    __tablename__ = 'apperances'

    id = db.Column(db.Iteger, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.column(db.Integer, db.Foreignkey('guest_id'), nullable=False)
    episode_id = db.Column(db.Integer, db.Foreignkey('episode_id'),     nullable=False)
    