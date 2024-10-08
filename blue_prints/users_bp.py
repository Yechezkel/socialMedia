from flask import Blueprint, jsonify
from data.db import get_db

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/users/', methods=['GET'])
def get_users():
    client, db = get_db()
    users = list(db.users.find({}, {'_id': False}))
    client.close()
    return jsonify(users)