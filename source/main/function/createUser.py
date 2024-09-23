from source import db
from source.main.model.users import Users
from flask import jsonify, make_response, request, url_for
from passlib.hash import pbkdf2_sha256


def createUser(data):
    try:
        json = data
        user_name = Users(
            user_name=json["user_name"],
            name=json["name"],
            gmail=json["gmail"],
            password_hash=pbkdf2_sha256.hash(json["password"]),
            isBlockAllUnknow=0,
        )
        db.session.add(user_name)
        db.session.commit()
        print("1.5")
    except Exception as e:
        print(e)


# rreset password
def fogot(gmail):
    try:
        json = request.json
        user = Users.query.filter(Users.gmail == gmail).first()
        if not user:
            return "Your account does not exist"
        else:
            user.password_hash = pbkdf2_sha256.hash(json["password"])
            db.session.commit()
            return "Updated password succsess "
    except Exception as e:
        return e


# change password
def change(data):
    try:
        json = data
        print("1")
        user = Users.query.filter(Users.gmail == json["gmail"]).first()
        print("1")
        user.password_hash = pbkdf2_sha256.hash(json["new_password"])
        print("1")
        db.session.commit()
        print("1")
    except Exception as e:
        print(e)
        return "Updated "
