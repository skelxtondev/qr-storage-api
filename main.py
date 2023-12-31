import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

from db import db


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "QR Code Storage REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app)

    @app.before_request
    def create_tables():
        db.create_all()

    # api.register_blueprint(EventBlueprint)
    # api.register_blueprint(HabitBlueprint)
    # api.register_blueprint(HabitTagBlueprint)

    return app
