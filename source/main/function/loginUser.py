from source import app, db
from source.main.model.users import Users
from flask import jsonify, request, make_response
from passlib.hash import pbkdf2_sha256
from source import app
from flask_jwt_extended import create_access_token
from sqlalchemy import or_, text
import time
import jwt
import requests
import secrets
from datetime import datetime

# def timelogin():
#     if (request.method == 'POST'):
#         try:
#             timelogin = request.form.get("timelogin")
#             # timelogin=int(timelogin) + 1
#             query=("UPDATE users SET timelogin = %s",(timelogin),)
#             db.session.execute(query)
#             db.session.commit()
#         except Exception as e:
#             print(e)
#             data = "error"
#             return {'status': 500, "message": "An error occurred."}

#     # Return a response for other request methods (e.g., GET, PUT, DELETE)
#     return {'status': 405, "message": "Method not allowed."}


# def goi_timeonline():
#     while True:
#         timelogin()
#         time.sleep(60)


def loginUser():
    if request.method == "POST":
        json = request.json
        try:
            if json["user_name"] == None:
                return make_response(
                    jsonify(
                        {
                            "status": 431,
                            "message": "body must have user_name",
                        }
                    ),
                    431,
                )
            User = Users.query.filter(
                or_(
                    Users.user_name == json["user_name"],
                    Users.gmail == json["user_name"],
                )
            ).first()
            if User == None:
                return make_response(
                    jsonify(
                        {
                            "status": 430,
                            "message": "User Not Found",
                        }
                    ),
                    430,
                )
            print(
                "__check_password__",
                pbkdf2_sha256.verify(json["password"], User.password_hash),
            )
            if User:
                if pbkdf2_sha256.verify(json["password"], User.password_hash):
                    User.statesLogin = True
                    User.last_activity_time = datetime.now()
                    db.session.add(User)
                    db.session.commit()
                    return {
                        "status": 200,
                        "message": "Login successfully",
                        "user": {
                            "id": User.id,
                            "name": User.name,
                            "gmail": User.gmail,
                            "df_color": {
                                "r": User.r,
                                "g": User.g,
                                "b": User.b,
                                "a": User.a,
                            },
                            "df_screen": User.df_screen,
                            "Avarta": User.linkAvatar,
                            "AvtProfile": User.linkAvtprofile,
                            "statesLogin": User.statesLogin,
                        },
                        "jwt": create_access_token(
                            identity={"id": User.id, "gmail": User.gmail}
                        ),
                    }, 200

            return make_response(
                jsonify(
                    {"status": 400, "message": "Password or user name has some wrong"}
                ),
                400,
            )
        except Exception as e:
            print(e)
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": "Password or user name has some wrong___" + str(e),
                    }
                ),
                400,
            )


def logout(id):
    if request.method == "POST":
        User = Users.query.filter(Users.id == id).first()
        User.statesLogin = False
        db.session.commit()
    return {"state": User.statesLogin}


def stateLogin():
    if request.method == "GET":
        try:
            data = []
            tv = db.session.execute(text("SELECT * FROM users"))
            for user in tv:
                data.append(
                    {
                        "id": user.id,
                        "name": user.user_name,
                        "Email": user.gmail,
                        "img": user.linkAvatar,
                        "imgProfile": user.linkAvtprofile,
                        "createAt": user.createAt,
                        "statesLogin": user.statesLogin,
                    }
                )
            return {"status": 200, "users": data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "States has some wrong"}), 400
            )


def cofimtoken():
    if request.method == "GET":
        # Token JWT bạn muốn giải mã
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgzOGMwNmM2MjA0NmMyZDk0OGFmZmUxMzdkZDUzMTAxMjlmNGQ1ZDEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI5NDYyNjQ1NzQ2MDAtNDVscGxkMWMyZGlic2tzaGw1NWQ3OWxhdWh0ZWY4cmsuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI5NDYyNjQ1NzQ2MDAtNDVscGxkMWMyZGlic2tzaGw1NWQ3OWxhdWh0ZWY4cmsuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTA0Nzc3OTE0MzgyMzQ0NzA2MzMiLCJlbWFpbCI6InBodWNwaHVjMTkxMjAwMUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmJmIjoxNjkzOTc0MTM1LCJuYW1lIjoiUGjDumMgTmd1eeG7hW4gVsSDbiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQWNIVHRkMGhEemkzb1p6c3Axekl0UG5NeU9fVnViMGZrWEkyVl9zUEYySGZaYzRJZz1zOTYtYyIsImdpdmVuX25hbWUiOiJQaMO6YyIsImZhbWlseV9uYW1lIjoiTmd1eeG7hW4gVsSDbiIsImxvY2FsZSI6InZpIiwiaWF0IjoxNjkzOTc0NDM1LCJleHAiOjE2OTM5NzgwMzUsImp0aSI6IjQzYzYwOTRlZjhiYTg4MzgwNWYxZDhmYjZjOWJhZmE4MWFmMzI5MzMifQ.DvgHH6Wg5I2BIsSjsJ0wjmP52Bdh6yKzF2RC6pM4pPeqq7efuS3QgJ0zgIYYsH4ooLYIZFmizEZ_5m0PmAcmkXvZGBBwzPy3OKDWgcwMh_5un7zm_vZOGRQBneaHEfHCf7kD9n5IC0u7nJMGLarQYlc_s8Bon82A6oO6d--__2f9vKNmHSE1b9zHB8iTvJ899ia8mgKV5vaQFOzbuU0T68fY8-Mw7CcrvuW3uW3e65bXjxX2rQ3u2kUIWvFF5bIzzDme-2FwACVV9HY_Y9ZkCAqLeZ5fptFila41BafsDVd8DMFJ3FCzYItJ28zOJSQ4iQSANPaKzJ5tUkvesr6kAA"
        # Khóa bí mật (secret key) bạn sử dụng để giải mã (cần phải khớp với secret key của bạn)
        print("1")
        secret_key = "devsenior"
        print("1")
        try:
            # Giải mã token JWT
            print("1")
            decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
            print("1")
            # Đã giải mã thành công, bạn có thể truy cập các thông tin trong token
            print(decoded_token)
            return decoded_token
        except jwt.ExpiredSignatureError:
            return "Token hết hạn"
        except jwt.InvalidTokenError:
            return "Token không hợp lệ"


# def change(json_data):

#     json_data
#     user = Users.query.filter(Users.password_hash == json_data["password"]).first()

#     if user:
#         user.password_hash = pbkdf2_sha256.hash(json_data["new_password"])
#         db.session.commit()
#         return "successful"
#     else:
#         return "1"


def logingoogle(token):
    if request.method == "POST":
        secret_key = "devsenior"
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        print(decoded_token)
        user = Users.query.filter(Users.gmail == decoded_token["gmail"]).first()
        if not user:
            user_name = Users(
                user_name=decoded_token["user_name"],
                name=decoded_token["name"],
                gmail=decoded_token["gmail"],
                password_hash=pbkdf2_sha256.hash(0),
                statesLogin=1,
                isBlockAllUnknow=0,
            )
            db.session.add(user_name)
            db.session.commit()
        else:
            return "User login"
        return "successful"
