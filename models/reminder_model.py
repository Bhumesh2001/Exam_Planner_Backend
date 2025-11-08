from utils.db import db

reminders = db["reminders"]

def create_reminder(data):
    return reminders.insert_one(data)

def get_user_reminders(email):
    return list(reminders.find({"userEmail": email}))

def delete_reminder(id):
    return reminders.delete_one({"_id": id})
