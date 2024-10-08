from flask import Blueprint, jsonify
from data.db import get_db

posts_bp = Blueprint('posts_bp', __name__)

@posts_bp.route('/posts/', methods=['GET'])
def get_posts():
    client, db = get_db()
    posts = list(db.posts.find({}, {'_id': False}))
    client.close()
    return jsonify(posts)

@posts_bp.route('/posts/<int:user_id>/', methods=['GET'])
def get_posts_by_user_id(user_id):
    client, db = get_db()
    posts = list(db.posts.find({'userId': user_id}, {'_id': False}))
    client.close()
    return jsonify(posts)