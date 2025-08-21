from flask import Flask
from flask_cors import CORS
from models.db import db
from endpoints import all_blueprints

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Enable CORS for all routes and origins (for development only)
    CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})

    db.init_app(app)
    for blueprint in all_blueprints:
        print(f"Adding {blueprint.name}")
        app.register_blueprint(blueprint)
    with app.app_context():
        db.create_all()
    return app
