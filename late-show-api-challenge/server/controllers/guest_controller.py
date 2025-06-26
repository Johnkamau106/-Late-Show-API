from flask import Blueprint, jsonify, request
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests])

@guest_bp.route('/guests/<int:guest_id>', methods=['GET'])
def get_guest_by_id(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    return jsonify({"id": guest.id, "name": guest.name, "occupation": guest.occupation})

@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    guest = Guest(name=data.get('name'), occupation=data.get('occupation'))
    db.session.add(guest)
    db.session.commit()
    return jsonify({"id": guest.id, "name": guest.name, "occupation": guest.occupation}), 201

@guest_bp.route('/guests/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    data = request.get_json()
    guest.name = data.get('name', guest.name)
    guest.occupation = data.get('occupation', guest.occupation)
    db.session.commit()
    return jsonify({"id": guest.id, "name": guest.name, "occupation": guest.occupation})

@guest_bp.route('/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    db.session.delete(guest)
    db.session.commit()
    return jsonify({"message": "Guest deleted"})
