from source import db, app
from source.main.model.users import Users
from source.main.model.notes import Notes
from source.main.model.nbnotes import Nbnotes
from source.main.model.datas import Datas
from source.main.model.images import Images
from source.main.function.middleware import *

from source.main.function.handleNotes import searchNote
from .handleNotes import getNotes
from flask import request, make_response, jsonify, json
from sqlalchemy import text, and_
from flask_jwt_extended.utils import decode_token
from flask_jwt_extended import jwt_required
from passlib.hash import pbkdf2_sha256
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from flask import flash
import base64
from datetime import datetime, timedelta

api_key = "ff41ea3fd3e48ce0970823376a104d8a"
PATH_IMAGE = "/var/www/samnote-build/image"


def handleUsers(param):
    if request.method == "POST":
        try:
            json = request.json
            user = Users.query.get(param)
            if pbkdf2_sha256.verify(json["password"], user.password_hash):
                db.session.delete(user)
                db.session.commit()
                return {"status": 200, "message": "User was deleted successfully"}
            else:
                return make_response(
                    jsonify({"status": 400, "message": "Password has some wrong"}), 400
                )
        except:
            return {"status": 400, "message": "Request failed. Please try again"}
    if request.method == "PATCH":
        try:
            user = Users.query.get(param)
            json = request.json
            print(json)
            for key in list(json.keys()):
                if key == "name":
                    user.name = json["name"]
                if key == "color":
                    color = json["color"]
                    user.r = color["r"]
                    user.g = color["g"]
                    user.b = color["b"]
                    user.a = color["a"]
                if key == "screen":
                    user.df_screen = json["screen"]
                if key == "avt":
                    user.linkAvatar = json["avt"]
            db.session.add(user)
            db.session.commit()
            return {"status": 200, "message": "User was updated successfully"}
        except:
            return {"status": 400, "message": "Request fail. Please try again"}


def getAllUser(who):
    if request.method == "GET":

        users = db.session.execute(
            text(
                "select u.gmail, u.id , u.linkAvatar from users as u where u.id != {}".format(
                    who
                )
            )
        )
        data = []
        for user in users:
            user_config = {}
            user_config["gmail"] = user.gmail
            user_config["id"] = user.id
            user_config["linkAvatar"] = user.linkAvatar
            user_config["role"] = "Member"
            data.append(user_config)
        return {"status": 200, "data": data}


def get20LastestUser():
    if request.method == "GET":
        try:
            users = db.session.execute(
                text(
                    "select  users.gmail ,users.id, users.user_name , users.name ,users.createAt, users.linkAvatar from users Order By users.id   DESC"
                )
            )
            index = 0
            data = []
            for user in users:
                if index >= 20:
                    break
                index = index + 1
                user_config = {}
                user_config["gmail"] = user.gmail
                user_config["id"] = user.id
                user_config["user_name"] = user.user_name
                user_config["name"] = user.name
                user_config["createAt"] = user.createAt
                user_config["linkAvatar"] = user.linkAvatar
                user_config["role"] = "Member"
                data.append(user_config)
            return {"status": 200, "data": data}

        except Exception as e:
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": str(e) + "Request fail. Please try again",
                    }
                ),
                400,
            )


def createPass2(who):
    try:
        json = request.json
        User = Users.query.filter_by(id=who).first()
        User.password_hash_2 = pbkdf2_sha256.hash(json["password_2"])
        db.session.add(User)
        db.session.commit()
        return {
            "status": 200,
            "message": "Create password 2 done!",
            "password_2": User.password_hash_2,
        }
    except:
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}), 400
        )


def checkPasssword2(who):
    if request.method == "POST":
        try:
            json = request.json

            User = Users.query.filter_by(id=who).first()
            if pbkdf2_sha256.verify(json["password_2"], User.password_hash_2):
                return {"status": 200, "message": "Opening screenshot successfully!"}
            else:
                return make_response(
                    jsonify({"status": 400, "message": "Opening screenshot failed!"}),
                    400,
                )
        except:
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def getProfile(who):
    if request.method == "GET":
        try:
            User = Users.query.filter_by(id=who).first()

            notes = (
                db.session.query(Notes, Datas)
                .join(Datas, Datas.idNote == Notes.idNote)
                .filter(Notes.idUser == who)
                .all()
            )
            noteRecent = []
            noteMost = []
            sodem = 0
            for item in reversed(notes):
                if sodem <= 10:
                    noteRecent.append(item)
                if sodem >= len(notes) - 11:
                    noteMost.append(item)
            return {
                "status": 200,
                "note": getNotes(notes),
                "note_recent": getNotes(noteRecent),
                "note_most": getNotes(noteMost),
                "user": {
                    "id": User.id,
                    "name": User.name,
                    "gmail": User.gmail,
                    "password_2": User.password_hash_2,
                    "createAccount": User.createAt,
                    "user_Name": User.user_name,
                    "status_Login": User.statesLogin,
                    "Avarta": User.linkAvatar,
                    "AvtProfile": User.linkAvtprofile,
                    "df_color": {"r": User.r, "g": User.g, "b": User.b, "a": User.a},
                },
            }
        except Exception as e:
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": "Request fail. Please try again",
                        "error": str(e),
                    }
                ),
                400,
            )


def upload_image_to_imgbb(image_path, api_key):
    # Tải dữ liệu ảnh
    with open(image_path, "rb") as file:
        payload = {
            "key": api_key,
            "image": base64.b64encode(file.read()),
        }
    # Gửi yêu cầu POST tải lên ảnh đến API của ImgBB
    response = request.post("https://api.imgbb.com/1/upload", payload)

    # Trích xuất đường dẫn trực tiếp đến ảnh từ JSON response
    json_data = json.loads(response.text)
    direct_link = json_data["data"]["url"]

    # Trả về đường dẫn trực tiếp đến ảnh
    return direct_link


def changeProfile(id):
    if request.method == "PATCH":
        user = Users.query.filter(Users.id == id).first()
        data = request.json
        new_link_avt = data.get("AvtProfile")
        avatar = data.get("Avarta")
        name = data.get("name")
        print("_________CHANGE PROFILE____" + name)
        try:
            if new_link_avt:
                user.linkAvtprofile = data.get("AvtProfile")
            if avatar:
                user.linkAvatar = data.get("Avarta")
                print(avatar)
            if name:
                user.name = data.get("name")
            db.session.add(user)
            db.session.commit()
            user_config = {}
            user_config["name"] = user.name
            user_config["AvtProfile"] = user.linkAvtprofile
            user_config["Avarta"] = user.linkAvatar
            user_config["id"] = user.id
            user_config["createAccount"] = user.createAt
            user_config["gmail"] = user.gmail
            user_config["user_Name"] = user.user_name
            user_config["status_Login"] = user.statesLogin
            user_config["password_2"] = user.password_hash_2
            user_config["df_color"] = {
                "r": user.r,
                "g": user.g,
                "b": user.b,
                "a": user.a,
            }
            return user_config
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def patch_profile(id_user):
    try:
        if request.method == "PATCH":
            user = Users.query.filter_by(id=id_user).first()
            image = request.files.get("avatar")
            image_profile = request.files.get("profile")
            input_data = request.form
            if user is None:
                res = {"status": 404, "message": "User not found"}
                return jsonify(res), 404
            # Remove image when changed
            if "git" in user.linkAvatar and image:
                user.linkAvatar = ""
                db.session.commit()
            else:
                if image:
                    print(
                        "____PATH_IMAGE__image__"
                        + str(PATH_IMAGE)
                        + "____"
                        + str(user.linkAvatar)
                    )
                # os.remove(make_image_local_path(PATH_IMAGE, user.linkAvatar))

            if "git" in user.linkAvtprofile and image_profile:
                user.linkAvtprofile = ""
                db.session.commit()
            else:
                if image_profile:
                    print("____PATH_IMAGE___image_profile_" + str(PATH_IMAGE))
                # os.remove(make_image_local_path(PATH_IMAGE, user.linkAvtprofile))

            # Change information user
            user.name = input_data["name"]
            user.linkAvatar = make_url_image(id_user, PATH_IMAGE, image, "avatar")
            user.linkAvtprofile = make_url_nginx_image(
                id_user, PATH_IMAGE, image_profile, "profile"
            )
            user.gmail = input_data["gmail"]
            user.user_name = input_data["username"]
            # user.statesLogin = input_data['state_login']
            user.password_hash = pbkdf2_sha256.hash(input_data["password"])
            db.session.add(user)
            db.session.commit()

            patch_user = {
                "id_user": id_user,
                "url_avatar": user.linkAvatar,
                "url_profile": user.linkAvtprofile,
                "gmail": user.gmail,
                "username": user.user_name,
                "password": user.password_hash,
                "state": user.statesLogin,
            }

            res = {
                "status": 200,
                "message": "Update profile successfully!",
                "data": patch_user,
            }
            return jsonify(res), 200
    except Exception as e:
        return make_response(jsonify(message="Something went wrong!" + str(e)), 500)


def searchUser():
    if request.method == "GET":
        try:
            search_query = request.args.get("key", "")
            notes = db.session.execute(
                text(
                    "Select * from (notes  inner join datas on notes.idNote=datas.idNote and notes.notePublic=1 and notes.inArchived=1)  inner join users on notes.idUser= users.id"
                )
            )

            notes_data = []
            for row in notes:
                search = {}
                note = {}
                search["id"] = row.id
                search["name"] = row.name
                search["idNote"] = row.idNote
                search["title"] = row.title
                search["content"] = row.content
                search["type"] = row.type
                if search_query and row.name:
                    if search_query.lower() in row.name.lower():
                        notes_data.append(search)
            return {"status": 200, "search_user": notes_data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def searchnameUser():
    if request.method == "GET":
        try:
            search_query = request.args.get("key", "")
            notes = db.session.execute(text("Select * from users"))

            notes_data = []
            for row in notes:
                search = {}
                note = {}
                search["id"] = row.id
                search["name"] = row.name
                search["gmail"] = row.gmail
                if search_query and row.name and row.gmail:
                    if (
                        search_query.lower() in row.name.lower()
                        or search_query.lower() in row.gmail.lower()
                    ):
                        notes_data.append(search)
            return {"status": 200, "search_user": notes_data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def deleteuser(param):
    if request.method == "DELETE":
        user = Users.query.filter(Users.gmail == param).first()
        data = []
        if user:
            # Assuming 'idNote' is the primary key of the 'notes' table
            notes_to_delete = Notes.query.filter_by(idUser=user.id).all()
            for note in notes_to_delete:
                datas_to_delete = Datas.query.filter_by(idNote=note.idNote).all()
                for data in datas_to_delete:
                    db.session.delete(data)
                db.session.delete(note)
            nbnotes_to_delete = Nbnotes.query.filter_by(idUser=user.id).first()
            db.session.delete(nbnotes_to_delete)
            db.session.delete(user)
            db.session.commit()
            return {"status": 200, "message": "user was deleted successfully"}
        else:
            return "haven't user account"


def check_status_online(id_user):
    try:
        user = Users.query.filter_by(id=id_user).first()
        if user is None:
            return (
                jsonify({"status": 404, "message": f"User {id_user} not found!"}),
                404,
            )
        if not user.statesLogin:
            return (
                jsonify({"status": 201, "message": f"User {id_user} is not login"}),
                201,
            )

        current_time = datetime.now()
        user.last_activity_time = current_time
        db.session.add(user)
        db.session.commit()

        return jsonify(current_time), 200
    except Exception as e:
        return jsonify({"status": 500, "message": f"Something went wrong! {e}"}), 500


def get_list_user_online():
    try:
        users = Users.query.all()
        current_time = datetime.now()
        print("Time Update: ", current_time)
        inactive_threshold = timedelta(minutes=3)

        users_online = []
        for user in users:

            if (
                user.statesLogin
                and current_time - user.last_activity_time <= inactive_threshold
            ):
                info = {
                    "user_id": user.id,
                    "user_name": user.user_name,
                    "url_avatar": user.linkAvatar,
                    "url_profile": user.linkAvtprofile,
                }
                users_online.append(info)
        return jsonify(
            {"status": 200, "message": "List user online", "users": users_online}
        )
    # except Exception as e:
    #     return jsonify({
    #         'status': 500,
    #         'message': f'Something went wrong! {e}'
    #     }), 500
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


def del_user(id_user: int):
    form_data = request.form()
    password = form_data.get("password")
    try:
        password_hash = pbkdf2_sha256.hash(password)
        userNeedDelete = Users.query.filter(Users.id == id_user).first()
        passINDatabase = userNeedDelete.password_hash
        if passINDatabase == password_hash:
            db.session.delete(userNeedDelete)
            db.session.commit()
    except Exception as e:
        return {"status": 500, "message": str(e)}
    return jsonify({"status": 200, "message": "Delete Account Done"})
