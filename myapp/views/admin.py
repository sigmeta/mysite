from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from myapp.models import *

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.username == "admin":
            return True
        return False

admin = Admin(app, name='MyApp', index_view=AdminIndexView(
    name='Home',
    template='admin/welcome.html',
    url='/admin',),template_mode='bootstrap3')
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Post, db.session))