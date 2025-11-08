from utils.db import db

notes = db["notes"]

def create_note(data):
    return notes.insert_one(data)

def get_all_notes():
    return list(notes.find())

def delete_note(id):
    return notes.delete_one({"_id": id})
