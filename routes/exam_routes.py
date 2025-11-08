from flask import Blueprint, jsonify, request
from utils.db import db
from utils.auth_middleware import token_required
from bson import ObjectId

exam_bp = Blueprint("exam_bp", __name__)
exams = db["exams"]

@exam_bp.route("/", methods=["GET"])
@token_required
def get_exams(user):
    sort_by = request.args.get("sortBy", "date")
    data = list(exams.find().sort(sort_by))
    for d in data:
        d["_id"] = str(d["_id"])
    return jsonify(data)

@exam_bp.route("/", methods=["POST"])
@token_required
def create_exam(user):
    data = request.get_json()
    exam = {
        "title": data["title"],
        "subject": data["subject"],
        "date": data["date"],
        "priority": data["priority"],
        "userEmail": user["email"],
    }
    exams.insert_one(exam)
    return jsonify({"message": "Exam added"}), 201

@exam_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_exam(user, id):
    exams.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Exam deleted"})
