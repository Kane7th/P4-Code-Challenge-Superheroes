# P4-Code-Challenge-Superheroes

# 🤸‍♀️ Superheroes API

A Flask-based RESTful API for managing Superheroes and their Powers, with support for many-to-many relationships using a join model (`HeroPower`). This project includes validation, serialization, and full CRUD functionality.

---

## 📦 Tech Stack

* Python 3.10+
* Flask
* SQLAlchemy
* Flask-Migrate
* SQLite (for local development)
* sqlalchemy-serializer

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Kane7th/P4-Code-Challenge-Superheroes.git
cd P4-Code-Challenge-Superheroes
```

### 2. Create Virtual Environment

Using pipenv:

```bash
pipenv install
pipenv shell
```

Or using venv:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

If using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or if using `Pipfile`:

```bash
pipenv install
```

---

## 🛠️ Setup the Database

### Initialize Migrations

```bash
flask db init
```

### Create Migration Script

```bash
flask db migrate -m "Initial migration"
```

### Apply Migrations

```bash
flask db upgrade
```

### Optional: Seed the Database

You can run the provided seed script:

```bash
python seed.py
```

---

## ▶️ Running the Server

```bash
flask run
```

The server will start at: [http://localhost:5555](http://localhost:5555)

---

## 🧪 API Endpoints

### 📅 `GET /heroes`

Returns a list of all heroes:

```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  ...
]
```

### 📅 `GET /heroes/<id>`

Returns detailed hero info, including their powers:

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "strength": "Strong",
      "hero_id": 1,
      "power_id": 2,
      "power": {
        "id": 2,
        "name": "flight",
        "description": "Allows flying at supersonic speed."
      }
    }
  ]
}
```

404 if hero not found:

```json
{ "error": "Hero not found" }
```

---

### 📅 `GET /powers`

Returns all powers:

```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
```

### 📅 `GET /powers/<id>`

Returns a specific power:

```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

404 if not found:

```json
{ "error": "Power not found" }
```

---

### 🛠 PATCH /powers/<id>

Update a power's description:

**Request Body:**

```json
{
  "description": "Updated power description"
}
```

**Success Response:**

```json
{
  "id": 1,
  "name": "super strength",
  "description": "Updated power description"
}
```

**Error Response:**

```json
{ "errors": ["Description must be at least 20 characters long"] }
```

---

### 🆕 POST /hero\_powers

Creates a new power-to-hero assignment.

**Request Body:**

```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

**Success Response:**

```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
```

**Error Response:**

```json
{ "errors": ["Strength must be 'Strong', 'Weak', or 'Average'"] }
```

---

## ✅ Validations

| Model     | Field       | Rule                                              |
| --------- | ----------- | ------------------------------------------------- |
| HeroPower | strength    | Must be one of: `'Strong'`, `'Weak'`, `'Average'` |
| Power     | description | Must be present and at least 20 characters long   |

---

## 🚹 Linting & Testing (Optional)

```bash
pytest
```

Or if using pipenv:

```bash
pipenv run pytest
```

---

## 📁 Project Structure

```
superheroes/
├── app.py
├── seed.py
├── models/
│   └── models.py
├── migrations/
├── Pipfile / requirements.txt
└── README.md
```

---

## 🧠 Author Notes

This project is part of a backend engineering bootcamp capstone for managing many-to-many relationships using Flask and SQLAlchemy.

---

