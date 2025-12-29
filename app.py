from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # gera 24 bytes aleatórios


    # Importa as rotas via blueprint
    from routes.auth_routes import main
    app.register_blueprint(main)

    return app
