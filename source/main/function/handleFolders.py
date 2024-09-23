from source import db
from flask import request, make_response, jsonify
from source.main.model.users import Users
from source.main.model.floders import Folder
from source.main.model.comments import Comments
from source.main.model import *
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label
from flask_jwt_extended import jwt_required
from sqlalchemy import text, and_
import jwt


def getfolder(folder):
    try:
        data = []
        for row in folder:
            get_folder = {}
            get_folder["nameFolder"] = row.nameFolder
            get_folder["idUser"] = row.idUser
            get_folder["id"] = row.id
            get_folder["createAt"] = str(row.createAt)
            data.append(get_folder)
        return data
    except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def getfolders(folder):
    try:
        data = []
        for row in folder:
            get_folder = {}
            get_folder["nameFolder"] = row.nameFolder
            get_folder["idUser"] = row.idUser
            get_folder["idNote"] = row.idNote
            get_folder["createAt"] = str(row.createAt)
            data.append(get_folder)
        return data
    except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def allFolder(param):
    if request.method == "GET":
        try:
            print(param)
            query = text("SELECT * FROM folders AS b  WHERE b.idUser = :param")
            notes = db.session.execute(query, {"param": param})
            return jsonify({"folder": getfolder(notes)})
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


#  notes = db.session.execute(text( 'Select * from (select * from notes where notes.idUser={} and notes.inArchived=1) as b inner join datas on b.idNote=datas.idNote'.format(param)))


def handleFolder(param):
    if request.method == "GET":
        try:
            query = text("SELECT * FROM folders AS b  WHERE b.idUser = :param")
            notes = db.session.execute(query, {"param": param})

            # Convert the cursor result to a list of dictionaries

            return jsonify({"folder": getfolder(notes)})
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    if request.method == "POST":
        try:
            json = request.json
            user = Users.query.filter(Users.id == param).first()
            data = []
            if user:
                date = datetime.now()
                data = Folder(
                    nameFolder=json["nameFolder"],
                    idUser=user.id,
                    createAt=date.strftime("%Y-%m-%dT%H:%M:%S.%f%z "),
                )
                db.session.add(data)
                db.session.commit()
                return {
                    "status": 200,
                    "message": "Folder was created successfully",
                    "idFolder": data.id,
                    "nameFolder": data.nameFolder,
                }
            else:
                return {"status": 200, "message": "User was not exit"}
        except Exception as e:
            print(e)
            return make_response(jsonify({"status": 400, "message": str(e)}), 400)


def changeFolder(id):
    if request.method == "PATCH":
        try:
            json = request.json
            user = Folder.query.filter(Folder.id == id).first()

            if user:
                date = datetime.now()
                user.nameFolder = json.get("nameFolder", user.nameFolder)
                user.createAt = date.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
                db.session.commit()
                return {"status": 200, "message": "Folder was changed successfully"}
            else:
                return {"status": 200, "message": "Folder was not exit"}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    if request.method == "DELETE":
        try:
            user = Folder.query.filter(Folder.id == id).first()
            data = []
            if user:
                db.session.delete(user)
                db.session.commit()
            return {"status": 200, "message": "Folder was deleted successfully"}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def getnotesFolder(id):
    if request.method == "GET":
        try:
            query = text(
                "SELECT * FROM folders AS b INNER JOIN notes ON b.id = notes.idFolder WHERE b.idUser = :param"
            )
            notes = db.session.execute(query, {"param": id})
            data = {}
            # Convert the cursor result to a list of dictionaries
            if notes:
                return jsonify({"folder": getfolders(notes)})
            else:
                return {"status": 200, "message": data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
