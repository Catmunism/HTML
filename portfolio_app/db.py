from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Base de dados SQLite na mesma pasta
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
