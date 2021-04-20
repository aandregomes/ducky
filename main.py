from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql+psycopg2://root:root@localhost:5432/ducky'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "Hello, Mathios!"


if __name__  == "__main__":
    app.run()