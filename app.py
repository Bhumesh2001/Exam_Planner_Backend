from flask import Flask, jsonify
from flask_cors import CORS
import threading, time, schedule, os
from routes.auth_routes import auth_bp
from routes.exam_routes import exam_bp
from routes.note_routes import note_bp
from routes.reminder_routes import reminder_bp
from routes.admin_routes import admin_bp
from utils.db import db
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(exam_bp, url_prefix="/api/exams")
app.register_blueprint(note_bp, url_prefix="/api/notes")
app.register_blueprint(reminder_bp, url_prefix="/api/reminders")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

@app.route("/")
def home():
    return jsonify({"message": "Exam Planner Backend Running ✅"})

def check_reminders():
    print("Checking reminders...")
    reminders = db["reminders"].find()
    for r in reminders:
        print(f"Reminder: {r.get('message')} at {r.get('remindAt')}")

def run_scheduler():
    schedule.every(int(os.getenv("REMINDER_INTERVAL_MINUTES", 5))).minutes.do(check_reminders)
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)), debug=False)
