from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app
from myapp.models import *

admin = Admin(app, name='Myapp', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))