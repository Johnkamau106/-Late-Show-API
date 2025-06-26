# 🌙 Late Show API — Flask Code Challenge

## 🎯 Overview
A Flask REST API for managing a Late Night TV show system, built with:
- MVC architecture
- PostgreSQL
- JWT authentication
- Postman for API testing
- Full documentation

---

## 🗂 Folder Structure
```
late-show-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## 🛠 Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install dependencies
```
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Database Setup
- Create a PostgreSQL database:
```
CREATE DATABASE late_show_db;
```
- Set your database URI in `server/config.py`:
```
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

### 4. Run Database Migrations & Seed Data
```
export FLASK_APP=server.app
cd late-show-api-challenge
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 5. Run the Server
```
export FLASK_APP=server.app
cd late-show-api-challenge
flask run
```

---

## 🔐 Authentication Flow
- Register a user: `POST /register`
- Login: `POST /login` (returns JWT token)
- For protected routes, include:
```
Authorization: Bearer <token>
```

---

## 🛠 Routes
| Route                          | Method | Auth Required | Description                        |
|--------------------------------|--------|---------------|------------------------------------|
| `/register`                    | POST   | No            | Register a user                    |
| `/login`                       | POST   | No            | Log in, get JWT token              |
| `/users`                       | GET    | No            | List all users (no passwords)      |
| `/episodes`                    | GET    | No            | List episodes                      |
| `/episodes/<int:id>`           | GET    | No            | Get episode + appearances          |
| `/episodes/<int:id>`           | DELETE | Yes           | Delete episode + appearances       |
| `/guests`                      | GET    | No            | List guests                        |
| `/guests`                      | POST   | No            | Create guest                       |
| `/guests/<int:guest_id>`       | GET    | No            | Get guest by ID                    |
| `/guests/<int:guest_id>`       | PUT    | No            | Update guest                       |
| `/guests/<int:guest_id>`       | DELETE | No            | Delete guest                       |
| `/appearances`                 | GET    | No            | List appearances                   |
| `/appearances`                 | POST   | Yes           | Create appearance                  |

### Sample Request/Response
**Register:**
```
POST /register
{
  "username": "admin",
  "password": "password"
}
```
**Login:**
```
POST /login
{
  "username": "admin",
  "password": "password"
}
Response: { "access_token": "..." }
```
**Protected Example:**
```
POST /appearances
Headers: Authorization: Bearer <token>
Body: { "rating": 5, "guest_id": 1, "episode_id": 1 }
```

---

## 🧪 Postman Usage
- Import `challenge-4-lateshow.postman_collection.json` into Postman.
- Test all endpoints, including registration, login, and protected routes.
- Use the JWT token from `/login` for protected requests.

---

## ✅ Submission Checklist
- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and tested in Postman
- [x] Clean, complete README.md
- [x] GitHub repo pushed and shared
