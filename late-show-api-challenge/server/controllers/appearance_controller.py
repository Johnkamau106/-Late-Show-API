from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.app import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([
        {
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id,
            "episode_id": a.episode_id
        } for a in appearances
    ])

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    try:
        appearance = Appearance(rating=int(rating), guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400