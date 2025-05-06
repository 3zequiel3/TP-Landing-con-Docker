from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import logging
from flask import session,current_app

db = SQLAlchemy()
from .wait_for_db import wait_for_db
def create_app():
    app = Flask(__name__)

    wait_for_db()  # Espera a que la base de datos esté disponible antes de continuar
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    with app.app_context():
        # Importación explícita de los modelos
        from .models import User, Product
        db.create_all()

    from .routes import routes
    app.register_blueprint(routes)

    @app.context_processor
    def inject_user():
        user = None
        user_id = session.get('user_id')
        if user_id:
            try:
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(f"Error al cargar usuario en context_processor: {e}")
        return dict(current_user=user)

    return app
