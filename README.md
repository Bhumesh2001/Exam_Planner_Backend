# 🧭 The Exam Planner & Reminder System — Backend (Python Flask)

A powerful backend API built with **Flask**, **MongoDB**, and **Flask-Session**, designed for managing **exams, notes, reminders, and users**.
This is the Python version of *The Exam Planner & Reminder System* — secure, modular, and easy to extend.

---

## 🚀 Features

* 🔐 **User Authentication** (Register & Login with session)
* 🎓 **Exam Management** (Create, view, delete, sort exams)
* 🗒️ **Notes System** (Parent-child structure support)
* ⏰ **Reminders** (Attach to exams with date/time)
* 🧩 **MongoDB Models** for Exams, Notes, and Reminders
* 🧠 **Session-based authentication** for route protection
* 🌙 Modern JSON-based API responses
* 🧭 Clean modular structure (models, routes, utils)

---

## 🏗️ Tech Stack

* **Python 3.10+**
* **Flask** — Web framework
* **Flask-Session** — For session-based login
* **PyMongo** — MongoDB connector
* **Werkzeug** — Password hashing utilities
* **dotenv** — For managing environment variables

---

## 📁 Folder Structure

```
backend/
├── app.py
├── routes/
│   ├── auth_routes.py
│   ├── exam_routes.py
│   ├── note_routes.py
│   └── reminder_routes.py
├── models/
│   ├── exam_model.py
│   ├── note_model.py
│   └── reminder_model.py
├── utils/
│   └── db.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/exam-planner-flask.git
cd exam-planner-flask
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, create one with:

```bash
Flask
Flask-Session
pymongo
python-dotenv
Werkzeug
```

---

### 4. Setup Environment Variables

Create a `.env` file in the backend folder:

```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
MONGO_URI=mongodb://localhost:27017/exam_planner
SESSION_TYPE=filesystem
```

---

### 5. Run the Server

```bash
python app.py
```

Your API will run on:
👉 `http://127.0.0.1:5000`

---

## 🧩 API Endpoints Overview

### 🔑 Authentication

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| POST   | `/api/auth/register` | Register a new user       |
| POST   | `/api/auth/login`    | Login and start a session |
| GET    | `/api/auth/logout`   | Logout and clear session  |

---

### 🎓 Exams

| Method | Endpoint          | Description                           |
| ------ | ----------------- | ------------------------------------- |
| GET    | `/api/exams`      | Get all exams (supports sortBy param) |
| POST   | `/api/exams`      | Create a new exam                     |
| DELETE | `/api/exams/<id>` | Delete an exam by ID                  |

---

### 🗒️ Notes

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| GET    | `/api/notes`      | Get all notes       |
| POST   | `/api/notes`      | Create new note     |
| DELETE | `/api/notes/<id>` | Delete a note by ID |

---

### ⏰ Reminders

| Method | Endpoint              | Description                          |
| ------ | --------------------- | ------------------------------------ |
| GET    | `/api/reminders`      | Get all reminders for logged-in user |
| POST   | `/api/reminders`      | Create reminder (linked to an exam)  |
| DELETE | `/api/reminders/<id>` | Delete reminder by ID                |

---

## 🧱 Sample JSON Data

### 📘 Example Exam Record

```json
{
  "title": "Data Structures Final Exam",
  "subject": "Computer Science",
  "date": "2025-12-10T09:30:00Z",
  "priority": 2
}
```

### 🗒️ Example Note Record

```json
{
  "title": "Linked List Notes",
  "content": "Study about singly and doubly linked lists.",
  "parentNote": ""
}
```

### ⏰ Example Reminder Record

```json
{
  "message": "Prepare for OS midterm",
  "remindAt": "2025-11-24T18:00:00Z",
  "examId": "6730846f91f41023cc1a9df7"
}
```

---

## 🧩 Database Models

| Model        | Fields                                              | Description                 |
| ------------ | --------------------------------------------------- | --------------------------- |
| **Exam**     | `title`, `subject`, `date`, `priority`, `userEmail` | Stores exam details         |
| **Note**     | `title`, `content`, `parentNote`, `userEmail`       | Stores notes with hierarchy |
| **Reminder** | `message`, `remindAt`, `examId`, `userEmail`        | Linked to an exam           |

---

## 🧠 Authentication Flow

1. User registers using `/api/auth/register`
2. Logs in with `/api/auth/login` → session stored on server
3. Routes check for `session['user']` to validate access
4. `/api/auth/logout` clears the session

---

## 🌍 Deployment

You can deploy this Flask backend on:

* **Render**
* **Railway**
* **PythonAnywhere**
* **Heroku (Buildpack)**
  Make sure to:
* Set up MongoDB Atlas URI in `.env`
* Enable CORS for your frontend origin

---

## 👨‍💻 Author

**Bhumesh Kewat**
Software Engineer | Full Stack Developer
📧 [bhumesh21@navgurukul.org](mailto:bhumesh21@navgurukul.org)

---

## 🪪 License

This project is open source and available under the **MIT License**.

---

**✨ Built with Flask, MongoDB, and Python — powering The Exam Planner & Reminder System.**
