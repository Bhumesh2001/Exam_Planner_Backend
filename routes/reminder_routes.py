from flask import Blueprint, jsonify, request
from utils.db import db
from utils.auth_middleware import token_required
from bson import ObjectId

reminder_bp = Blueprint("reminder_bp", __name__)
reminders = db["reminders"]

@reminder_bp.route("/", methods=["GET"])
@token_required
def get_reminders(user):
    data = list(reminders.find({"userEmail": user["email"]}))
    for r in data:
        r["_id"] = str(r["_id"])
    return jsonify(data)

@reminder_bp.route("/", methods=["POST"])
@token_required
def create_reminder(user):
    data = request.get_json()
    reminder = {
        "message": data["message"],
        "remindAt": data["remindAt"],
        "examId": data["examId"],
        "userEmail": user["email"],
    }
    reminders.insert_one(reminder)
    return jsonify({"message": "Reminder added"}), 201

@reminder_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_reminder(user, id):
    reminders.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Reminder deleted"})
