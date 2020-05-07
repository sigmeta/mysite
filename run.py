from myapp import create_app

app = create_app()

from myapp.admin import admin

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
