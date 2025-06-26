from server.app import db, create_app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create default user
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Create default guests
    guest1 = Guest(name="Lylla", occupation="Actress")
    guest2 = Guest(name="Bob collymore", occupation="Entrepreneur")
    db.session.add_all([guest1, guest2])
    db.session.commit()

    # Create default episodes
    episode1 = Episode(date="2024-06-12", number=1)
    episode2 = Episode(date="2024-06-13", number=2)
    db.session.add_all([episode1, episode2])
    db.session.commit()

    # Create default appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print("Database seeded successfully.")