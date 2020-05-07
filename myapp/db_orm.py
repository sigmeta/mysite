# Initialize database, connect with ORM (SQLAlchemy)
import click
from flask.cli import with_appcontext
from myapp import db

def init_db():
    db.drop_all()
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)