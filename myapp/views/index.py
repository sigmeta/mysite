from myapp.models import *
from myapp.views.auth import login_required
from app import app

# a simple page that says hello
@app.route('/')
@login_required
def hello():
    return 'Hello, World!'