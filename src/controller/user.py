from flask import request
from src.model.user import User
from main import db, app


@app.route("/login", methods=["GET", "POST"])
def sign_up():
    body = request.json
    if request.method == 'POST':
        return sign_user(body["name"], body["email"])


def sign_user(name: str, email: str):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()