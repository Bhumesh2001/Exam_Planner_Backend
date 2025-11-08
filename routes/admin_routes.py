from flask import Blueprint, jsonify
from utils.db import db
from utils.auth_middleware import token_required

admin_bp = Blueprint("admin_bp", __name__)
users = db["users"]
exams = db["exams"]

@admin_bp.route("/users", methods=["GET"])
@token_required
def get_users(user):
    if user["role"] != "admin":
        return jsonify({"message": "Access denied"}), 403
    data = list(users.find({}, {"password": 0}))
    for u in data:
        u["_id"] = str(u["_id"])
    return jsonify(data)

@admin_bp.route("/exams", methods=["GET"])
@token_required
def get_all_exams(user):
    if user["role"] != "admin":
        return jsonify({"message": "Access denied"}), 403
    data = list(exams.find())
    for e in data:
        e["_id"] = str(e["_id"])
    return jsonify(data)
