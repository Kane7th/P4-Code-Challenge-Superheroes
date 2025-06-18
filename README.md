# P4-Code-Challenge-Superheroes
# 🦸‍♀️ Superheroes API

A Flask-based RESTful API for managing Superheroes and their Powers, with support for many-to-many relationships using a join model (`HeroPower`). This project includes validation, serialization, and full CRUD functionality.

---

## 📦 Tech Stack

- Python 3.10+
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite (for local development)
- sqlalchemy-serializer

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone Kane7th/P4-Code-Challenge-Superheroes 
cd superheroes
run python 'seed.py' to seed data


2. Create Virtual Environment
Using pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
Or use python -m venv venv and source venv/bin/activate if you prefer pip.

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or if you're using Pipfile:

bash
Copy
Edit
pipenv install
🛠️ Setup the Database
Initialize Migrations
bash
Copy
Edit
flask db init
Create Migration Script
bash
Copy
Edit
flask db migrate -m "Initial migration"
Apply Migrations
bash
Copy
Edit
flask db upgrade
Optional: Seed the Database
You can create a seed function or script to add initial data. Example:

python
Copy
Edit
from app import create_app
from models.models import db, Hero, Power, HeroPower

app = create_app()
with app.app_context():
    # Add heroes, powers, hero_powers here
    db.session.commit()
▶️ Running the Server
bash
Copy
Edit
flask run
The server will start at: http://localhost:5555

🧪 API Endpoints
📥 GET /heroes
Returns a list of all heroes:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  ...
]
📥 GET /heroes/<id>
Returns detailed hero info, including their powers:

json
Copy
Edit
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
404 if hero not found:

json
Copy
Edit
{ "error": "Hero not found" }
📥 GET /powers
Returns all powers:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
📥 GET /powers/<id>
Returns a specific power:

json
Copy
Edit
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
404 if not found:

json
Copy
Edit
{ "error": "Power not found" }
🛠 PATCH /powers/<id>
Update a power's description:

Request Body:
json
Copy
Edit
{
  "description": "Updated power description"
}
Success Response:

json
Copy
Edit
{
  "id": 1,
  "name": "super strength",
  "description": "Updated power description"
}
Error Response:

json
Copy
Edit
{ "errors": ["Description must be at least 20 characters long"] }
🆕 POST /hero_powers
Creates a new power-to-hero assignment.

Request Body:
json
Copy
Edit
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
Success Response:
json
Copy
Edit
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
Error Response:
json
Copy
Edit
{ "errors": ["Strength must be 'Strong', 'Weak', or 'Average'"] }
✅ Validations
Model	Field	Rule
HeroPower	strength	Must be one of: 'Strong', 'Weak', 'Average'
Power	description	Must be present and at least 20 characters long

🧹 Linting & Testing (Optional)
bash
Copy
Edit
pytest
Or if using pipenv:

bash
Copy
Edit
pipenv run pytest
📁 Project Structure
Copy
Edit
superheroes/
├── app.py
├── models/
│   └── models.py
├── migrations/
├── Pipfile / requirements.txt
└── README.md
🧠 Author Notes
This project is part of a backend engineering bootcamp capstone for managing many-to-many relationships using Flask and SQLAlchemy.