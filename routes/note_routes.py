from flask import Blueprint, jsonify, request
from utils.db import db
from utils.auth_middleware import token_required
from bson import ObjectId

note_bp = Blueprint("note_bp", __name__)
notes = db["notes"]

@note_bp.route("/", methods=["GET"])
@token_required
def get_notes(user):
    data = list(notes.find())
    for n in data:
        n["_id"] = str(n["_id"])
    return jsonify(data)

@note_bp.route("/", methods=["POST"])
@token_required
def create_note(user):
    data = request.get_json()
    note = {
        "title": data["title"],
        "content": data["content"],
        "parentNote": data.get("parentNote"),
        "userEmail": user["email"],
    }
    notes.insert_one(note)
    return jsonify({"message": "Note added"}), 201

@note_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_note(user, id):
    notes.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Note deleted"})
