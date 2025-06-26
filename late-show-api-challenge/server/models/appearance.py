from server.app import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    guest = db.relationship('Guest', backref='appearances')

    @staticmethod
    def validate_rating(rating):
        return 1 <= rating <= 5

    def __init__(self, rating, guest_id, episode_id):
        if not self.validate_rating(rating):
            raise ValueError('Rating must be between 1 and 5')
        self.rating = rating
        self.guest_id = guest_id
        self.episode_id = episode_id
    