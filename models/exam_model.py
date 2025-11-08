from utils.db import db

exams = db["exams"]

def create_exam(data):
    return exams.insert_one(data)

def get_all_exams(sort_by="date"):
    return list(exams.find().sort(sort_by))

def delete_exam(id):
    return exams.delete_one({"_id": id})
