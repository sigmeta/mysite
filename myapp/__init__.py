import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,login_required,current_user

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
        app.config.from_pyfile('../config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from myapp.auth import login_required
    # a simple page that says hello
    @app.route('/hello')
    @login_required
    def hello():
        return 'Hello, World!'

    from . import auth
    app.register_blueprint(auth.bp)

    db = SQLAlchemy()
    db.init_app(app)

    from . import db_orm
    db_orm.init_app(app)

    return app