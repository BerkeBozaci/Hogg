import click
from flask import Flask, current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hogg_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @click.command("init-db")
    @with_appcontext
    def init_db_command():
        """Initialize the database."""
        db.create_all()
        click.echo("Initialized the database.")
        
    app.cli.add_command(init_db_command)

    from .routes import main
    app.register_blueprint(main)

    return app
