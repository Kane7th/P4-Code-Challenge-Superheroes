from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models.models import db, Hero, Power, HeroPower  # Adjust this import if needed


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    # Home route
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    # GET /heroes
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([
            {"id": h.id, "name": h.name, "super_name": h.super_name}
            for h in heroes
        ])

    # GET /heroes/<id>
    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "strength": hp.strength,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "power": {
                        "id": hp.power.id,
                        "name": hp.power.name,
                        "description": hp.power.description
                    }
                } for hp in hero.hero_powers
            ]
        })

    # GET /powers
    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([
            {"id": p.id, "name": p.name, "description": p.description}
            for p in powers
        ])

    # GET /powers/<id>
    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        return jsonify({"id": power.id, "name": power.name, "description": power.description})

    # PATCH /powers/<id>
    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404

        data = request.get_json()
        try:
            power.description = data.get("description", power.description)
            db.session.commit()
            return jsonify({
                "id": power.id,
                "name": power.name,
                "description": power.description
            })
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

    # POST /hero_powers
    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.get_json()

        try:
            hero_power = HeroPower(
                strength=data["strength"],
                hero_id=data["hero_id"],
                power_id=data["power_id"]
            )
            db.session.add(hero_power)
            db.session.commit()

            return jsonify({
                "id": hero_power.id,
                "hero_id": hero_power.hero_id,
                "power_id": hero_power.power_id,
                "strength": hero_power.strength,
                "hero": {
                    "id": hero_power.hero.id,
                    "name": hero_power.hero.name,
                    "super_name": hero_power.hero.super_name
                },
                "power": {
                    "id": hero_power.power.id,
                    "name": hero_power.power.name,
                    "description": hero_power.power.description
                }
            }), 201

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)
