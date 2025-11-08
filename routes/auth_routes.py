from flask import Blueprint, request, jsonify
import bcrypt, jwt, os
from datetime import datetime, timedelta
from utils.db import db
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

auth_bp = Blueprint("auth_bp", __name__)
users = db["users"]

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"message": "Missing fields"}), 400

    if users.find_one({"email": data["email"]}):
        return jsonify({"message": "Email already exists"}), 400

    hashed_pw = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    
    user_doc = {
        "name": data["name"],
        "email": data["email"],
        "password": hashed_pw,
        "role": data.get("role", "user")  # ✅ dynamic role with default fallback
    }

    users.insert_one(user_doc)

    token = jwt.encode(
        {"email": data["email"], "exp": datetime.utcnow() + timedelta(days=7)},
        JWT_SECRET,
        algorithm="HS256",
    )

    # ✅ Use the actual role from data (not hardcoded)
    return jsonify({
        "token": token,
        "user": {
            "name": data["name"],
            "email": data["email"],
            "role": user_doc["role"]
        }
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = users.find_one({"email": data["email"]})
    if not user or not bcrypt.checkpw(data["password"].encode("utf-8"), user["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode(
        {"email": user["email"], "role": user["role"], "exp": datetime.utcnow() + timedelta(days=7)},
        JWT_SECRET,
        algorithm="HS256",
    )
    user["_id"] = str(user["_id"])
    return jsonify({"token": token, "user": {"name": user["name"], "email": user["email"], "role": user["role"]}})
