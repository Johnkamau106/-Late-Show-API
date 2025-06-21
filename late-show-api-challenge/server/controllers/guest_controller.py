from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guest', methods=['GET'])
def get_guest():

    guests = guest.query.all()
    return jsonify({"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests)

#my additional one but i might remove it
@guest_bp.route('/guest/<int:guest_id>', methods=['GET'])
def get_guest_by_id(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    return jsonify({"id": guest.id, "name": guest.name, "occupation": guest.occupation})
