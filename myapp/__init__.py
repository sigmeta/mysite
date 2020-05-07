import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'myapp.sqlite'),
        SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(app.instance_path, 'myapp.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(os.path.join(app.root_path,'config.py'), silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from myapp.views.auth import login_required
    # a simple page that says hello
    @app.route('/hello')
    @login_required
    def hello():
        return 'Hello, World!'

    from myapp.views import auth
    app.register_blueprint(auth.bp)

    db = SQLAlchemy()
    db.init_app(app)

    # Initialize database with SQLAlchemy
    from myapp.database import db_orm
    db_orm.init_app(app)

    return app