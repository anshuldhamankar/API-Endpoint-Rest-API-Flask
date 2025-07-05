from flask import Flask
from .routes import bp as api_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_routes)
    return app
