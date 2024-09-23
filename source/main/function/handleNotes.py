import math
import os.path
from datetime import datetime
from sqlalchemy import desc
import asyncio

from flask_cors import cross_origin

from source.main.model.comments import Comments
from source.main.model.datas import Datas
from source.main.model.favorite import Favorites
from source.main.model.nbnotes import Nbnotes
from source.main.model.notes import Notes
from source.main.model.images import Images
from source.main.model.colors import Colors
from source.main.model.notes import *

PATH_IMAGE = r"/home/thinkdiff/Documents/ImageNote"
from source import app

from flask import jsonify, make_response, request, url_for, send_from_directory, session
from passlib.hash import pbkdf2_sha256
from sqlalchemy import text

from source import db
from source.main.function.middleware import *
from source.main.model import *
from source.main.model.users import Users
from PIL import Image
from io import BytesIO

import random

# from pyfcm import FCMNotification

import uuid


def getNotes(notes):
    try:
        dataAllNote = []
        # print("________________________getnotes___________________________________________")
        for note in notes:
            # print(note)
            note_parse = {}
            # print(note.Notes.type)
            if note.Notes.type == "checklist" or note.Notes.type == "checkList":
                flag = False
                # print("checklist if len(data) > 0:")
                if len(dataAllNote) > 0:
                    for item in dataAllNote:
                        if (
                            item["type"] == str(note.Notes.type)
                            and item["idNote"] == note.Notes.idNote
                        ):
                            flag = True
                            # print("checklist item")
                            item["data"].append(
                                {
                                    "content": note.Datas.content,
                                    "status": note.Datas.doneContent,
                                    "id": note.Datas.idData,
                                }
                            )
                if not flag:
                    note_parse["idNote"] = note.Notes.idNote
                    note_parse["type"] = note.Notes.type
                    note_parse["data"] = [
                        {
                            "content": note.Datas.content,
                            "status": note.Datas.doneContent,
                            "id": note.Datas.idData,
                        }
                    ]
                    # note_parse["data"] = note.Datas.content
                    # print("if not flag:")
                    note_parse["title"] = note.Notes.title
                    note_parse["doneNote"] = note.Notes.doneNote
                    note_parse["createAt"] = str(note.Notes.createAt)
                    note_parse["idFolder"] = note.Notes.idFolder
                    note_parse["dueAt"] = (
                        str(note.Notes.dueAt) if note.Notes.dueAt else note.Notes.dueAt
                    )
                    note_parse["remindAt"] = (
                        str(note.Notes.remindAt)
                        if note.Notes.remindAt
                        else note.Notes.remindAt
                    )
                    note_parse["view"] = note.Notes.view
                    note_parse["lock"] = note.Notes.lock
                    note_parse["pinned"] = note.Notes.pinned
                    note_parse["notePublic"] = note.Notes.notePublic
                    note_parse["inArchived"] = note.Notes.inArchived
                    note_parse["linkNoteShare"] = note.Notes.linkNoteShare
                    note_parse["idUser"] = note.Notes.idUser
                    note_parse["image"] = note.Datas.image
                    note_parse["updateAt"] = note.Notes.updateAt
                    note_parse["color"] = {
                        "r": note.Notes.r,
                        "g": note.Notes.g,
                        "b": note.Notes.b,
                        "a": note.Notes.a,
                    }
            if (
                note.Notes.type == "text"
                or note.Notes.type == "scan"
                or note.Notes.type == "Text"
            ):
                # print("____________________" + str(note.Notes.idNote))
                #  print(note.Datas.content)
                note_parse["view"] = note.Notes.view
                note_parse["idNote"] = note.Notes.idNote
                note_parse["type"] = note.Notes.type
                note_parse["data"] = note.Datas.content
                note_parse["title"] = note.Notes.title
                note_parse["inArchived"] = note.Notes.inArchived
                note_parse["doneNote"] = note.Notes.doneNote
                images = Images.query.filter(Images.idNote == note.Notes.idNote)
                link_image = []
                for image in images:
                    link_image.append({"id": image.idImage, "link": image.link})
                note_parse["image"] = link_image
                note_parse["createAt"] = str(note.Notes.createAt)
                note_parse["idFolder"] = note.Notes.idFolder
                note_parse["dueAt"] = (
                    str(note.Notes.dueAt) if note.Notes.dueAt else note.Notes.dueAt
                )
                note_parse["remindAt"] = (
                    str(note.Notes.remindAt)
                    if note.Notes.remindAt
                    else note.Notes.remindAt
                )
                note_parse["lock"] = note.Notes.lock
                note_parse["pinned"] = note.Notes.pinned
                note_parse["idUser"] = note.Notes.idUser
                note_parse["notePublic"] = note.Notes.notePublic
                note_parse["linkNoteShare"] = note.Notes.linkNoteShare
                note_parse["updateAt"] = note.Notes.updateAt
                note_parse["color"] = {
                    "r": note.Notes.r,
                    "g": note.Notes.g,
                    "b": note.Notes.b,
                    "a": note.Notes.a,
                }

            if note.Notes.type == "image" or note.Notes.type == "screenshot":
                # print("note.Notes.type == image")
                note_parse["view"] = note.Notes.view
                note_parse["idNote"] = note.Notes.idNote
                note_parse["type"] = note.Notes.type
                note_parse["data"] = note.Datas.content
                note_parse["title"] = note.Notes.title
                note_parse["inArchived"] = note.Notes.inArchived
                note_parse["doneNote"] = note.Notes.doneNote
                note_parse["createAt"] = str(note.Notes.createAt)
                note_parse["idFolder"] = note.Notes.idFolder
                note_parse["dueAt"] = (
                    str(note.Notes.dueAt) if note.Notes.dueAt else note.Notes.dueAt
                )
                note_parse["remindAt"] = (
                    str(note.Notes.remindAt)
                    if note.Notes.remindAt
                    else note.Notes.remindAt
                )
                note_parse["lock"] = note.Notes.lock
                note_parse["metaData"] = note.Notes.metaData
                note_parse["notePublic"] = note.Notes.notePublic
                note_parse["linkNoteShare"] = note.Notes.linkNoteShare
                note_parse["pinned"] = note.Notes.pinned
                note_parse["idUser"] = note.Notes.idUser

                images = Images.query.filter(Images.idNote == note.Notes.idNote)
                link_image = []
                for image in images:
                    link_image.append({"id": image.idImage, "link": image.link})
                note_parse["image"] = link_image
                note_parse["updateAt"] = note.Notes.updateAt
                note_parse["color"] = {
                    "r": note.Notes.r,
                    "g": note.Notes.g,
                    "b": note.Notes.b,
                    "a": note.Notes.a,
                }
            if note_parse:
                dataAllNote.append(note_parse)
        # freshData = []
        # for note_parse in dataAllNote:
        #     # print(note_parse)
        #     if note_parse["lock"]:
        #         note_parse["lock"] = "*******"
        #         note_parse["data"] = "Your Data Locked, Please Input Password For Open It"
        #     freshData.append(note_parse)
        return dataAllNote
    except Exception as e:
        print(note)
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}),
            400,
        )


def specific_string(length):
    sample_string = "pqrstuvwxy"  # define the specific string
    # define the condition for random string
    result = "".join((random.choice(sample_string)) for x in range(length))
    print(" Randomly generated string is: ", result)


def getNote(param, lock=False, babel=False):
    try:
        notes = db.session.execute(
            text(
                "Select * from (select * from notes where notes.idNote={}) as b inner join datas on b.idNote=datas.idNote".format(
                    param
                )
            )
        )
        note_parse = {}

        flag = False

        for note in notes:
            if note.type == "checklist" or note.type == "checkList":
                if flag == False:
                    flag = True
                    note_parse["view"] = note.view
                    note_parse["idNote"] = note.idNote
                    note_parse["type"] = note.type
                    note_parse["data"] = []
                    if note.inArchived == 0:
                        note_parse["inArchived"] = False
                    else:
                        note_parse["inArchived"] = True

                    print(note.doneNote)
                    if note.doneNote == 0:
                        note_parse["doneNote"] = False
                    else:
                        note_parse["doneNote"] = True

                    print("list")
                    note_parse["createAt"] = str(note.createAt)
                    note_parse["dueAt"] = (
                        str(note.dueAt) if (note.dueAt) else note.dueAt
                    )
                    note_parse["remindAt"] = (
                        str(note.remindAt) if (note.remindAt) else note.remindAt
                    )
                    note_parse["lock"] = None
                    if note.pinned == 0:
                        note_parse["pinned"] = False
                    else:
                        note_parse["pinned"] = True
                    note_parse["notePublic"] = note.notePublic  # ___SONPIPI____
                    note_parse["linkNoteShare"] = note.linkNoteShare  # ___SONPIPI____
                    note_parse["idUser"] = note.idUser
                    note_parse["updateAt"] = note.updateAt
                    note_parse["color"] = {
                        "r": note.r,
                        "g": note.g,
                        "b": note.b,
                        "a": note.a,
                    }
                if flag == True:
                    doneContent = None
                    if note.doneContent == 0:
                        doneContent = False
                    else:
                        doneContent = True
                    note_parse["data"].append(
                        {
                            "content": note.content,
                            "status": doneContent,
                            "id": note.idData,
                        }
                    )

            if note.type == "text" or note.type == "scan" or note.type == "Text":
                note_parse["view"] = note.view
                note_parse["idNote"] = note.idNote
                note_parse["type"] = note.type
                note_parse["data"] = note.content
                note_parse["title"] = note.title
                if note.doneNote == 0:
                    note_parse["doneNote"] = False
                else:
                    note_parse["doneNote"] = True
                print("text")
                note_parse["createAt"] = str(note.createAt)
                note_parse["notePublic"] = note.notePublic  # ___SONPIPI____
                note_parse["linkNoteShare"] = note.linkNoteShare  # ___SONPIPI____
                note_parse["dueAt"] = str(note.dueAt) if (note.dueAt) else note.dueAt
                note_parse["remindAt"] = (
                    str(note.remindAt) if (note.remindAt) else note.remindAt
                )
                note_parse["lock"] = None
                if note.pinned == 0:
                    note_parse["pinned"] = False
                else:
                    note_parse["pinned"] = True
                note_parse["idUser"] = note.idUser
                note_parse["updateAt"] = note.updateAt
                note_parse["color"] = {
                    "r": note.r,
                    "g": note.g,
                    "b": note.b,
                    "a": note.a,
                }
                list_img = []
                image_note = Images.query.filter(
                    Images.idNote == note_parse["idNote"]
                ).all()
                for img in image_note:
                    data = {"id": img.idImage, "link": img.link}
                    list_img.append(data)
                note_parse["image"] = list_img

            if note.type == "image" or note.type == "screenshot":
                note_parse["view"] = note.view
                note_parse["idNote"] = note.idNote
                note_parse["type"] = note.type
                note_parse["data"] = note.content
                note_parse["title"] = note.title
                note_parse["notePublic"] = note.notePublic  # ___SONPIPI____
                note_parse["linkNoteShare"] = note.linkNoteShare  # ___SONPIPI____
                if note.doneNote == 0:
                    note_parse["doneNote"] = False
                else:
                    note_parse["doneNote"] = True
                print("img")
                note_parse["createAt"] = str(note.createAt)
                note_parse["dueAt"] = str(note.dueAt) if (note.dueAt) else note.dueAt
                note_parse["remindAt"] = (
                    str(note.remindAt) if (note.remindAt) else note.remindAt
                )
                note_parse["lock"] = None
                note_parse["metaData"] = note.metaData
                if note.pinned == 0:
                    note_parse["pinned"] = False
                else:
                    note_parse["pinned"] = True
                note_parse["idUser"] = note.idUser
                note_parse["updateAt"] = note.updateAt
                note_parse["color"] = {
                    "r": note.r,
                    "g": note.g,
                    "b": note.b,
                    "a": note.a,
                }

                list_img = []
                image_note = Images.query.filter(
                    Images.idNote == note_parse["idNote"]
                ).all()
                for img in image_note:
                    data = {"id": img.idImage, "link": img.link}
                    list_img.append(data)
                note_parse["image"] = list_img

        if note.lock:
            if lock == True or babel == True:
                note_parse["data"] = "Locked"
            note_parse["lock"] = "*******"
        return note_parse
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}),
            400,
        )


def getOnlyNote(idNote):
    if request.method == "GET":
        try:
            note = Notes.query.filter(Notes.idNote == idNote).first()
            if note:
                # note.view = int(note.view) + 1
                # db.session.commit()
                return {"note": getNote(idNote, babel=True)}
            else:
                return "Note does not exist"  # Return an appropriate message when the note is not found
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    else:
        return {"status": 400, "message": "Invalid request method"}


def genLinkWebNotes(idNote):
    if request.method == "GET":
        return {"note": getNote(idNote, babel=True)}
    else:
        return {"status": 400, "message": "Invalid request method"}


def changePrivateNotes(idNote):
    if request.method == "PATCH":
        try:
            note = Notes.query.filter(Notes.idNote == idNote).first()
            data = request.json

            private = data.get("notePublic", "0")
            note.notePublic = private
            db.session.add(note)
            db.session.commit()
            return jsonify({"status": 200, "message": "Note is private"})
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


def getPublicNotes():
    try:
        notes = (
            db.session.query(Notes, Datas, Users)
            .join(Users, Users.id == Notes.idUser)
            .join(Datas, Datas.idNote == Notes.idNote)
            .filter(Notes.notePublic == 1 and Notes.inArchived == 1)
            .order_by(desc(Notes.idNote))
            .limit(10)
        )

        list_public_notes = []
        for note in notes:
            dataImage = []
            if note.Notes.type == "image":
                images = Images.query.filter(Images.idNote == note.Notes.idNote).all()
                for image in images:
                    dataImage.append({"id": image.idImage, "link": image.link})

            public_note = {
                "idNote": note.Notes.idNote,
                "title": note.Notes.title,
                "type": note.Notes.type,
                "content": note.Datas.content,
                "update_at": note.Notes.createAt,
                "author": note.Users.user_name,
                "images": dataImage,
            }
            list_public_notes.append(public_note)

        return (
            jsonify(
                {"status": 200, "message": "success", "public_note": list_public_notes}
            ),
            200,
        )

    except Exception as e:
        return (
            jsonify(
                {"status": 500, "message": f"Something went wrong!", "error": str(e)}
            ),
            500,
        )
    # if (request.method == "GET"):
    #     notes = db.session.execute(text(
    #         'Select * from (select * from notes where notes.notePublic=1 and notes.inArchived=1) as b inner join datas on b.idNote=datas.idNote'))
    #     return {"notes": getNotes(notes)}


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


@cross_origin()
def handleNotes(param):

    try:
        if request.method == "GET":
            page = request.args.get("page")
            if page:
                limit = 5
                offset = (int(page) - 1) * limit

                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1, Notes.idUser == param
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )

                data_length = len(notes)
                total_page = math.ceil(data_length / limit)

                get_notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1, Notes.idUser == param
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .offset(offset)
                    .limit(limit)
                )

                return {"notes": getNotes(get_notes), "total_page": total_page}
            else:
                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1, Notes.idUser == param
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )
                return {"notes": getNotes(notes)}

        if request.method == "POST":
            print("SONPRO_PHAN_POST___handleNotes___" + str(request.json))
            try:
                json = request.json
                nbnote = Nbnotes.query.filter(Nbnotes.idUser == param).first()
                note_lock = False
                # print(json)/note
                color = json["color"]
                date_dueAt = None
                if json["dueAt"]:
                    date_dueAt = datetime.strptime(
                        json["dueAt"], "%d/%m/%Y %H:%M %p %z"
                    )
                date_rmAt = None
                if json["remindAt"]:
                    date_rmAt = datetime.strptime(
                        json["remindAt"], "%d/%m/%Y %H:%M %p %z"
                    )
                lockPass = None

                if json["lock"]:
                    lockPass = pbkdf2_sha256.hash(json["lock"])

                if lockPass:
                    note_lock = True
                #   linkNoteShare
                note = {}
                if "metaData" in json:
                    if "notePublic" in json:
                        linkNoteShare = my_random_string(6)
                        note = Notes(
                            idUser=param,
                            idFolder=json["idFolder"],
                            type=json["type"],
                            title=json["title"],
                            pinned=json["pinned"],
                            dueAt=date_dueAt,
                            remindAt=date_rmAt,
                            lock=lockPass,
                            r=color["r"],
                            g=color["g"],
                            b=color["b"],
                            a=color["a"],
                            metaData=json["metaData"],
                            linkNoteShare=json["linkNoteShare"],
                            notePublic=json["notePublic"],
                        )
                    else:
                        note = Notes(
                            idUser=param,
                            idFolder=json["idFolder"],
                            type=json["type"],
                            title=json["title"],
                            pinned=json["pinned"],
                            dueAt=date_dueAt,
                            remindAt=date_rmAt,
                            lock=lockPass,
                            r=color["r"],
                            g=color["g"],
                            b=color["b"],
                            a=color["a"],
                            metaData=json["metaData"],
                            linkNoteShare=json["linkNoteShare"],
                            notePublic=0,
                        )
                else:
                    if "notePublic" in json:
                        linkNoteShare = my_random_string(6)
                        note = Notes(
                            idUser=param,
                            idFolder=json["idFolder"],
                            type=json["type"],
                            title=json["title"],
                            pinned=json["pinned"],
                            dueAt=date_dueAt,
                            remindAt=date_rmAt,
                            lock=lockPass,
                            r=color["r"],
                            g=color["g"],
                            b=color["b"],
                            a=color["a"],
                            notePublic=json["notePublic"],
                            linkNoteShare=json["linkNoteShare"],
                        )
                    else:
                        note = Notes(
                            idUser=param,
                            idFolder=json["idFolder"],
                            type=json["type"],
                            title=json["title"],
                            pinned=json["pinned"],
                            dueAt=date_dueAt,
                            remindAt=date_rmAt,
                            lock=lockPass,
                            r=color["r"],
                            g=color["g"],
                            b=color["b"],
                            a=color["a"],
                            linkNoteShare=json["linkNoteShare"],
                            notePublic=0,
                        )
                db.session.add(note)
                if nbnote:
                    if note.notePublic == 1:
                        nbnote.nbnotes = int(nbnote.nbnotes) + 1
                else:
                    if note.notePublic == 1:
                        nbnote = Nbnotes(
                            idUser=param, nbnotes=1
                        )  # Create a new Nbnotes record if it doesn't exist
                        db.session.add(nbnote)
                print("SONPIPI_POST_NOTES_", str(note))
                # print("1")
                # if nbnote.nbnotes:
                #     nbnote.nbnotes = (int(nbnote.nbnotes) + 1)
                db.session.commit()
                if json["type"] == "checklist" or json["type"] == "checkList":
                    for each in json["data"]:
                        data = Datas(
                            idNote=note.idNote,
                            content=each["content"],
                            doneContent=each["status"],
                        )
                        db.session.add(data)
                else:
                    data = Datas(idNote=note.idNote, content=json["data"])
                    db.session.add(data)
                db.session.commit()
                return {
                    "status": 200,
                    "message": "Note was created successfully",
                    "note": getNote(note.idNote, note_lock),
                }
            except Exception as e:
                print(e)
                return make_response(
                    jsonify({"status": 400, "message": str(e)}),
                    400,
                )
        if request.method == "PATCH":
            try:
                json = request.json
                # print("______PHAN PATCH_______")
                # print(json)
                note_query = Notes.query.filter(Notes.idNote == param).first()
                # print(note_querys)
                for key in list(json.keys()):
                    # print(str(key))
                    if key == "dueAt":
                        date_dueAt = None
                        if json["dueAt"]:
                            date_dueAt = datetime.strptime(
                                json["dueAt"], "%d/%m/%Y %H:%M %p %z"
                            )
                            # formatted_dueAt = date_dueAt.strftime(
                            #     "%Y-%m-%d %H:%M %p %z"
                            # )
                        note_query.dueAt = date_dueAt
                        # note_query.dueAt = str(formatted_dueAt)
                        # print(str(formatted_dueAt))
                        # print(date_dueAt)
                    if key == "notePublic":
                        notePublic = json["notePublic"]
                        note_query.notePublic = notePublic
                        linkNoteShare = my_random_string(6)
                        note_query.linkNoteShare = linkNoteShare
                    if key == "remindAt":
                        date_rmAt = None
                        if json["remindAt"]:
                            date_rmAt = datetime.strptime(
                                json["remindAt"], "%d/%m/%Y %H:%M %p %z"
                            )
                        note_query.remindAt = date_rmAt
                    if key == "color":
                        color = json["color"]
                        note_query.r = color["r"]
                        note_query.g = color["g"]
                        note_query.b = color["b"]
                        note_query.a = color["a"]
                    if key == "title":
                        note_query.title = json["title"]

                    if key == "idFolder":
                        # print(json["idFolder"])
                        note_query.idFolder = json["idFolder"]

                    if key == "data":

                        if json["type"] == "text" or json["type"] == "Text":
                            note_data = Datas.query.filter(
                                Datas.idNote == param
                            ).first()
                            # print("____DAY_DATA_LEN_____idNote: " + str(param))
                            # print(json["data"])
                            note_data.content = json["data"]
                            db.session.add(note_data)

                        if json["type"] == "checklist" or json["type"] == "checkList":

                            trunc_data = Datas.query.filter(Datas.idNote == param).all()
                            for item in trunc_data:
                                db.session.delete(item)
                            db.session.commit()

                            for edit in json["data"]:
                                data = Datas(
                                    idNote=param,
                                    content=edit["content"],
                                    doneContent=edit["status"],
                                )
                                db.session.add(data)

                    if key == "pinned":
                        note_query.pinned = json["pinned"]
                    if key == "lock":
                        lockPass = None

                        if json["lock"]:
                            lockPass = pbkdf2_sha256.hash(json["lock"])
                        note_query.lock = lockPass
                # print(note_query.idFolder)
                note_query.updateAt = datetime.now()
                db.session.add(note_query)
                db.session.commit()
                # print("passs")
                # print(notes)
                return {
                    "status": 200,
                    "message": "Note was updated successfully",
                    "note": getNote(note_query.idNote, False),
                }
            except Exception as e:
                print(e)
                return make_response(
                    jsonify({"status": 400, "message": str(e)}),
                    400,
                )
        if request.method == "DELETE":
            try:

                note_query = db.session.query(Notes).filter_by(idNote=param).first()
                note_query.inArchived = False
                note_lock = False
                if note_query.lock:
                    note_lock = True
                note_query.updateAt = datetime.now()
                db.session.add(note_query)
                db.session.commit()
                return {
                    "status": 200,
                    "message": "Note was deleted successfully",
                    "note": getNote(note_query.idNote, note_lock),
                }
            except Exception as e:
                return make_response(
                    jsonify({"status": 400, "message": str(e)}),
                    400,
                )
    except Exception as e:
        return (
            jsonify(
                {"status": 500, "message": "Something went wrong!", "error": str(e)}
            ),
            500,
        )


@cross_origin()
def handlePublicNotes(param):

    try:
        if request.method == "GET":
            page = request.args.get("page")
            if page:
                limit = 5
                offset = (int(page) - 1) * limit

                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 1,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )

                data_length = len(notes)
                total_page = math.ceil(data_length / limit)

                get_notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 1,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .offset(offset)
                    .limit(limit)
                )

                return {"notes": getNotes(get_notes), "total_page": total_page}
            else:
                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 1,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )
                return {"notes": getNotes(notes)}

    except Exception as e:
        return (
            jsonify(
                {"status": 500, "message": "Something went wrong!", "error": str(e)}
            ),
            500,
        )


@cross_origin()
def handlePrivateNotes(param):

    try:
        if request.method == "GET":
            page = request.args.get("page")
            if page:
                limit = 5
                offset = (int(page) - 1) * limit

                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 0,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )

                data_length = len(notes)
                total_page = math.ceil(data_length / limit)

                get_notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 0,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .offset(offset)
                    .limit(limit)
                )

                return {"notes": getNotes(get_notes), "total_page": total_page}
            else:
                notes = (
                    db.session.query(Notes, Datas)
                    .join(Datas, Datas.idNote == Notes.idNote)
                    .filter(
                        Notes.inArchived == 1,
                        Notes.idUser == param,
                        Notes.notePublic == 0,
                    )  # khong nhận and mà dùng bằng dấu ,
                    .order_by(desc(Notes.updateAt))
                    .all()
                )
                return {"notes": getNotes(notes)}

    except Exception as e:
        return (
            jsonify(
                {"status": 500, "message": "Something went wrong!", "error": str(e)}
            ),
            500,
        )


def tickerBox(idData):
    if request.method == "PATCH":
        try:
            data = Datas.query.filter(Datas.idData == idData).first()
            data.doneContent = not data.doneContent
            db.session.add(data)
            db.session.commit()
            return {"status": 200, "message": "Note was update successfully"}
        except Exception as e:
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


def delTruncNote(id):
    if request.method == "DELETE":
        try:
            note_query = db.session.query(Notes).filter_by(idNote=id).first()
            print(note_query)
            db.session.delete(note_query)
            db.session.commit()
            return {
                "status": 200,
                "message": "Note was deleted successfully",
            }
        except Exception as e:
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


@cross_origin()
def trashGet(idUser):
    if request.method == "GET":

        notes = (
            db.session.query(Notes, Datas)
            .join(Datas, Datas.idNote == Notes.idNote)
            .filter(
                Notes.inArchived == 0, Notes.idUser == idUser
            )  # khong nhận and mà dùng bằng dấu ,
            .order_by(desc(Notes.updateAt))
            .all()
        )

        return {"notes": getNotes(notes)}


def getAllNotes_images(idUser):
    print("______________getAllNotes_images_______")
    if request.method == "GET":
        # notes = db.session.execute(
        #     text(
        #         "Select * from (select * from notes where notes.idUser={} ) as b inner join datas on b.idNote=datas.idNote and LENGTH(datas.image) > 1".format(
        #             idUser
        #         )
        #     )
        # )
        notes = (
            db.session.query(Notes, Datas)
            .join(Datas, Datas.idNote == Notes.idNote)
            .filter(
                Datas.image != None, Notes.idUser == idUser
            )  # khong nhận and mà dùng bằng dấu ,
            .order_by(desc(Notes.updateAt))
            .all()
        )
        noteHaveImage = []
        for itemNote in notes:
            if len(itemNote.Datas.image) > 1:
                noteHaveImage.append(itemNote)
        return {"notes": getNotes(noteHaveImage)}


def trashRestore(id):
    if request.method == "POST":
        try:
            note_query = db.session.query(Notes).filter_by(idNote=id).first()
            note_query.inArchived = True
            db.session.add(note_query)
            db.session.commit()
            return {
                "status": 200,
                "message": "Note was restore successfully",
                "note": getNote(note_query.idNote),
            }
        except Exception as e:
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


def getLastNote():
    try:
        if request.method == "GET":

            sql = db.session.execute(text("select max(idNote) as MaxId  from notes"))
            for note in sql:
                return {"status": 200, "idNoteLast": note.MaxId}
    except Exception as e:
        return make_response(jsonify({"status": 400, "message": str(e)}), 400)


# ________________________SONPIPI____________________4_SEP_2024___SONPIPI___________
async def unlocknote(idNote):
    try:
        if request.method == "POST":
            json = request.json
            pass2Check = json["pass2Check"]
            if pass2Check == None:
                return {
                    "status": 303,
                    "message": "body is json must have: pass2Check, please pass2Check have C upper",
                    "note": None,
                }
            NoteFind = Notes.query.filter(Notes.idNote == idNote).first()
            if NoteFind == None:
                return {
                    "status": 307,
                    "message": "wrong idnote " + str(idNote),
                    "note": None,
                }
            if NoteFind.lock == None:
                return {
                    "status": 309,
                    "message": "Note is Not Lock "
                    + str(idNote)
                    + " Please recheck note and choose note lock for unlock it !",
                    "note": getNote(idNote, False),
                }
            userFind = Users.query.filter(Users.id == NoteFind.idUser).first()
            if userFind.password_hash_2 == None:
                return {
                    "status": 311,
                    "message": "Cant Find password_2 of iduser:"
                    + str(userFind.id)
                    + " this app use password_2 of user for unlock security note, if you loss password_2, please login account and reset password2",
                    "note": None,
                }
            password_matched = pbkdf2_sha256.verify(
                pass2Check, userFind.password_hash_2
            )
            if userFind != None:
                if password_matched:
                    NoteFind.lock = None
                    db.session.add(NoteFind)
                    db.session.commit()
                    return {
                        "status": 200,
                        "note": getNote(idNote, False),
                        "message": "unlock notes okie done, this note will note view okie",
                    }
                else:
                    return {
                        "status": 300,
                        "message": "Wrong password_2 of iduser:"
                        + str(userFind.id)
                        + " this app use password_2 of user for unlock security note, if you loss password_2, please login account and reset password2",
                        "note": None,
                    }
            return {"status": 301, "message": "wrong userid"}
        return {"status": 304, "message": "wrong method, please use method post"}
    except Exception as e:
        return make_response(
            jsonify(
                {
                    "status": 400,
                    "message": "Request fail. Please try again" + str(e),
                    "note": None,
                }
            ),
            400,
        )


def openLock(idNote):
    try:
        if request.method == "POST":
            json = request.json
            pass2Check = json["pass2Check"]
            if pass2Check == None:
                return {
                    "status": 303,
                    "message": "body is json must have: pass2Check, please pass2Check have C upper",
                    "note": None,
                }
            NoteFind = Notes.query.filter(Notes.idNote == idNote).first()
            if NoteFind == None:
                return {
                    "status": 307,
                    "message": "wrong idnote " + str(idNote),
                    "note": None,
                }
            if NoteFind.lock == None:
                return {
                    "status": 309,
                    "message": "Note is Not Lock " + str(idNote),
                    "note": getNote(idNote, False),
                }
            userFind = Users.query.filter(Users.id == NoteFind.idUser).first()
            if userFind.password_hash_2 == None:
                return {
                    "status": 311,
                    "message": "Cant Find password_2 of iduser:"
                    + str(userFind.id)
                    + " this app use password_2 of user for unlock security note, if you loss password_2, please login account and reset password2",
                    "note": None,
                }
            password_matched = pbkdf2_sha256.verify(
                pass2Check, userFind.password_hash_2
            )
            if userFind:
                if password_matched:
                    return {
                        "status": 200,
                        "note": getNote(idNote, False),
                        "message": "open lock for view note",
                    }
                else:
                    return {
                        "status": 300,
                        "message": "wrong password 2",
                        "note": None,
                    }
            return {"status": 301, "message": "wrong userid"}
        return {"status": 304, "message": "wrong method, please use method post"}
    except Exception as e:
        return make_response(
            jsonify(
                {
                    "status": 400,
                    "message": "Request fail. Please try again" + str(e),
                    "note": None,
                }
            ),
            400,
        )


def getNotesShare(nid):
    if request.method == "GET":
        # note = Notes.query.filter(
        #         Notes.idNote == nid).first()
        return {"status": 200, "message": "Note get successfully", "note": getNote(nid)}


def searchNoteOfUser(idUser, keysearch):
    if request.method == "GET":
        try:
            notesDataFind = (
                db.session.query(Notes, Datas)
                .join(Datas, Datas.idNote == Notes.idNote)
                .filter(
                    Datas.content.ilike(f"%{keysearch}%"),
                    Notes.inArchived == 1,
                    Notes.idUser == idUser,
                )  # khong nhận and mà dùng bằng dấu ,
                .order_by(desc(Notes.updateAt))
                .all()
            )
            print("_______________PHAN2____")
            NoteTitleFind = (
                db.session.query(Notes, Datas)
                .join(Datas, Datas.idNote == Notes.idNote)
                .filter(
                    Notes.title.ilike(
                        f"%{keysearch}%",
                    ),
                    Notes.inArchived == 1,
                    Notes.idUser == idUser,
                )  # khong nhận and mà dùng bằng dấu ,
                .order_by(desc(Notes.updateAt))
                .all()
            )
            print("_+-________TAISAOLAN2LOI____")
            if notesDataFind == None and NoteTitleFind == None:
                return {
                    "status": 202,
                    "search_note": {},
                    "message": "No Notes Search keysearch = " + str(keysearch),
                }

            notes_data = []
            for rowData in notesDataFind:
                notes_data.append(rowData)

            for NoteUserFind in NoteTitleFind:
                notes_data.append(NoteUserFind)
            if len(notes_data) == 0:
                return {
                    "status": 201,
                    "search_note": [],
                    "message": "No Data In Title And Content Text keysearch = "
                    + str(keysearch)
                    + " of idUser = "
                    + str(idUser),
                }
            return {
                "status": 200,
                "search_note": getNotes(notes_data),
                "message": "Okie Done keysearch = "
                + str(keysearch)
                + " of idUser = "
                + str(idUser),
            }
        except Exception as e:
            print(e)
            return make_response(
                jsonify(
                    {"status": 500, "search_note": [], "message": "EXPTION " + str(e)}
                ),
                500,
            )


def searchNote():
    if request.method == "GET":
        try:
            notes = db.session.execute(
                text(
                    "Select * from (select * from notes where notes.notePublic=1 and notes.inArchived=1) as b inner join datas on b.idNote=datas.idNote"
                )
            )
            search_query = request.args.get("key", "")
            notes_data = []
            for row in notes:
                search = {}
                search["idNote"] = row.idNote
                search["title"] = row.title
                search["content"] = row.content
                search["type"] = row.type
                if search_query and row.title and row.content:
                    if (
                        search_query.lower() in row.title.lower()
                        or search_query.lower() in row.content.lower()
                    ):
                        notes_data.append(search)
            return {"status": 200, "search_note": notes_data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


# def subscription():
#     """
#         POST creates a subscription
#         GET returns vapid public key which clients uses to send around push notification
#     """

#     if request.method == "GET":
#         return Response(response=json.dumps({"public_key": VAPID_PUBLIC_KEY}),
#             headers={"Access-Control-Allow-Origin": "*"}, content_type="application/json")

#     subscription_token = request.get_json("subscription_token")
#     return Response(status=201, mimetype="application/json")
# def push_v1():
#     message = "Push Test v1"
#     print("is_json",request.is_json)

#     if not request.json or not request.json.get('sub_token'):
#         return jsonify({'failed':1})

#     print("request.json",request.json)

#     token = request.json.get('sub_token')
#     try:
#         token = json.loads(token)
#         send_web_push(token, message)
#         return jsonify({'success':1})
#     except Exception as e:
#         print("error",e)
#         return jsonify({'failed':str(e)})


def numberNotes():
    if request.method == "GET":
        try:
            notes = db.session.execute(
                text(
                    "Select * from users inner join nbnotes on users.id= nbnotes.idUser ORDER BY nbnotes.nbnotes DESC "
                )
            )
            index = 0
            data = []
            for user in notes:
                if index > 10:
                    break
                index += 1
                nbnote = {}
                nbnote["id"] = user.id
                nbnote["idUser"] = user.idUser
                nbnote["name"] = user.name
                nbnote["nbnote"] = user.nbnotes
                nbnote["Avatar"] = user.linkAvatar

                data.append(nbnote)
            return {"status": 200, "data": data}
        except Exception as e:
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


def getview():
    if request.method == "GET":  # Use parentheses for the condition
        try:
            notes = db.session.execute(text("Select * from notes"))
            data = []
            for row in notes:
                view_note = {}
                view_note["idNote"] = row.idNote
                view_note["idUser"] = row.idUser
                view_note["view"] = row.view
                data.append(view_note)
            return {"state": 200, "data": data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": str(e)}),
                400,
            )


def share_link():
    if request.method == "POST":
        try:
            json = request.json

            if "url" not in json:
                return jsonify({"error": "URL is missing in the request"}), 400

            shared_url = json["url"]
            message = f"Shared the link: {shared_url}"

            return jsonify({"message": message})
            # with app.test_request_context():
            #     profile_url = url_for('profile', username='john')
            #     print(f'Dường dẫn URL cho profile: {profile_url}')
            #     return {'state': 200, 'data': profile_url}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )


async def create_new_note_image(id_user):
    try:
        data = request.form
        image_note = request.files.get("image_note")
        if image_note == None:
            return make_response(
                jsonify(
                    {
                        "message": "please input file image_note in body post request like:    https://github.com/ngdtuankiet/anh28/blob/main/448112635_1150540716179419_6091427834101329441_n.png?raw=true",
                        "status": 210,
                    }
                ),
                210,
            )
        print("______jsdfjsd____")
        titleStr = data.get("title")
        print("_______hehehee____")
        print("______titleStr___" + str(titleStr))
        checkStringTitle = isinstance(titleStr, str)
        if titleStr == None:
            return (
                jsonify(
                    {
                        "status": 201,
                        "message": "Please input title in body request"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                201,
            )
        if checkStringTitle == True and len(titleStr) == 0:
            return (
                jsonify(
                    {
                        "status": 201,
                        "message": "Please input title in body request"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                201,
            )
        if data.get("notePublic") == None:
            return (
                jsonify(
                    {
                        "status": 202,
                        "message": "Please input notePublic in body"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                202,
            )
        if data.get("r") == None:
            return (
                jsonify(
                    {
                        "status": 203,
                        "message": "Please input r in rgba in body"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                203,
            )
        if data.get("g") == None:
            return (
                jsonify(
                    {
                        "status": 204,
                        "message": "Please input g in rgba in body"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                204,
            )
        if data.get("b") == None:
            return (
                jsonify(
                    {
                        "status": 205,
                        "message": "Please input b in rgba in body"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                205,
            )
        if data.get("a") == None:
            return (
                jsonify(
                    {
                        "status": 206,
                        "message": "Please input a in rgba in body"
                        + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                        "Info": {},
                    }
                ),
                206,
            )

        noteCreate = (
            db.session.query(Notes, Datas, Users)
            .join(Datas, Datas.idNote == Notes.idNote)
            .join(Users, Users.id == Notes.idUser)
            .first()
        )
        if noteCreate is None:
            return (
                jsonify({"status": 404, "message": "User not found", "Info": {}}),
                404,
            )

        if not noteCreate.Users.statesLogin:
            return (
                jsonify({"status": 401, "message": "User is not login", "Info": {}}),
                401,
            )
        date_rmAt = None

        if data.get("remind"):
            date_rmAt = datetime.strptime(data.get("remind"), "%d/%m/%Y %H:%M %p %z")
        # remind = ''
        # if data['remind']:
        #     remind = data['remind']
        new_note = Notes(
            idUser=id_user,
            type="image",
            title=titleStr,
            dueAt=datetime.now(),
            createAt=datetime.now(),
            r=data.get("r"),
            g=data.get("g"),
            b=data.get("b"),
            a=data.get("a"),
            notePublic=data.get("notePublic"),
            remindAt=date_rmAt,
        )
        new_note.linkNoteShare = "https://samsungnote.store/detail_note/" + str(
            new_note.idNote
        )
        lockStr = data.get("lock")
        checkStringLock = isinstance(lockStr, str)
        if lockStr != None and checkStringLock == True:
            if len(lockStr) > 0:
                lockPassSave = lockStr
                userFind = Users.query.filter(Users.id == id_user).first()
                if userFind == None:
                    return (
                        jsonify(
                            {
                                "status": 301,
                                "message": "Cant Create Note Because lock note but cant find userid = "
                                + str(id_user)
                                + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                                "Info": {},
                            }
                        ),
                        301,
                    )
                if userFind.password_hash_2 == None:
                    return (
                        jsonify(
                            {
                                "status": 308,
                                "message": "User Have userid = "
                                + str()
                                + str(id_user)
                                + " no password 2, please in put password 2 in setting for create lock notes"
                                + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                                "Info": {},
                            }
                        ),
                        308,
                    )
                password_matched = pbkdf2_sha256.verify(
                    lockPassSave, userFind.password_hash_2
                )
                if password_matched != None:
                    new_note.lock = userFind.password_hash_2
                else:
                    return (
                        jsonify(
                            {
                                "status": 302,
                                "message": "Cant Create Note Lock Because user input wrong password2 = "
                                + str(data.get("lock"))
                                + str(id_user)
                                + "  Please see image https://github.com/ngdtuankiet/anh28/blob/main/222.png?raw=true",
                                "Info": {},
                            }
                        ),
                        302,
                    )
        if data.get("notePublic") != None:
            new_note.notePublic = data.get("notePublic")

        db.session.add(new_note)
        db.session.commit()
        linkNoteShare = make_link_share(new_note.idNote)
        print(linkNoteShare)
        new_note.linkNoteShare = linkNoteShare
        db.session.commit()

        URLImage = make_url_image(id_user, PATH_IMAGE, image_note, "note")
        print(URLImage)
        new_data = Datas(
            idNote=new_note.idNote,
            content=data.get("content"),
            image=URLImage,
        )
        db.session.add(new_data)
        db.session.commit()

        new_image = Images(
            idNote=new_note.idNote, link=URLImage, idUserUpload=id_user, idChat1_1=0
        )
        print("save_image________")
        db.session.add(new_image)
        db.session.commit()

        new_note = {
            "id_note": new_note.idNote,
            "type": "image",
            "title": data.get("title"),
            "content": data.get("content"),
            "image_note": URLImage,
        }
        return (
            jsonify(
                {
                    "status": 200,
                    "message": "Note was created successfully",
                    "Info": new_note,
                }
            ),
            200,
        )
    except Exception as e:
        print("____Error from server:______ " + str(e))
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "message": "__________Error EXPTION_______________" + str(e),
                    "Info": {},
                }
            ),
        )


def add_image_note():
    try:
        data = request.form
        id_note = data.get("id_note")
        id_user = data.get("id_user")
        image_notes = request.files.getlist("image_note")

        note = Notes.query.filter(Notes.idNote == id_note).first()

        # for item  = dat
        if str(note.idUser) != str(data.get("id_user")):
            result_data = {
                "error": "This is not your note",
            }
        else:

            for image in image_notes:
                URLImage = make_url_image(id_user, PATH_IMAGE, image, "note")
                new_image = Images(
                    idNote=note.idNote, link=URLImage, idUserUpload=id_user, idChat1_1=0
                )
                print("save_image________")
                db.session.add(new_image)
                db.session.commit()

            images = Images.query.filter(Images.idNote == id_note).all()
            image_link = []
            for image in images:
                image_link.append({"id": image.idImage, "link": image.link})

            result_data = {
                "id_note": data.get("id_note"),
                "list_image": image_link,
            }
        return jsonify({"status": 200, "message": "Success", "data": result_data}), 200

    except Exception as e:
        print("____Error from server:______ " + str(e))
        return make_response(jsonify("____Error from server:______ ", str(e)), 500)


def update_image_note():
    try:
        data = request.form
        id_note = data.get("id_note")
        id_image = data.get("id_image")
        id_user = data.get("id_user")
        update_image = request.files.get("update_image")

        note = Notes.query.filter(Notes.idNote == id_note).first()

        if str(note.idUser) != str(id_user):
            result_data = {
                "error": "This is not your note",
            }
        else:
            image = Images.query.filter(Images.idImage == id_image).first()
            URLImage = make_url_image(id_user, PATH_IMAGE, update_image, "note")
            image.link = URLImage
            db.session.commit()

            image_link = []
            images = Images.query.filter(Images.idNote == id_note).all()
            for im in images:
                image_link.append({"id": im.idImage, "link": im.link})

            result_data = {
                "id_note": data["id_note"],
                "list_image": image_link,
            }

        return jsonify({"status": 200, "message": "Success", "data": result_data}), 200

    except Exception as e:
        print("____Error from server:______ " + str(e))
        return make_response(jsonify("____Error from server:______ ", str(e)), 500)


def delete_image_note():
    try:
        data = request.form
        # print(data)
        id_note = data.get("id_note")
        id_images = request.form.getlist("id_images[]")
        id_user = data.get("id_user")
        note = Notes.query.filter(Notes.idNote == id_note).first()
        # print(id_images)
        if str(note.idUser) != str(id_user):
            result_data = {
                "error": "This is not your note",
            }
        else:
            for id_image in id_images:
                image = Images.query.filter(Images.idImage == id_image).first()
                # print(image)
                db.session.delete(image)
                db.session.commit()
            result_data = {
                "action": "deleted",
            }

        return jsonify({"status": 200, "message": "Success", "data": result_data}), 200

    except Exception as e:
        print("____Error from server:______ " + str(e))
        return make_response(jsonify("____Error from server:______ ", str(e)), 500)


def get_all_color():
    try:
        colors = Colors.query.all()
        result_data = []
        for color in colors:
            result_data.append(
                {
                    "id": color.idColor,
                    "name": color.name,
                    "r": color.r,
                    "g": color.g,
                    "b": color.b,
                }
            )
        return jsonify({"status": 200, "message": "Success", "data": result_data}), 200
    except Exception as e:
        print("____Error from server:______ " + str(e))
        return make_response(jsonify("____Error from server:______ ", str(e)), 500)


def view_image(id_user, file_name):
    try:
        user_path = os.path.join(PATH_IMAGE, str(id_user))
        print(user_path)
        # print(file_name)
        returnPro = send_from_directory(user_path, file_name)
        print("returnPro__" + str(returnPro))
        return returnPro
    except Exception as e:
        user_path = os.path.join("/var/www/samnote-build/image", str(id_user))
        returnPro = send_from_directory(user_path, file_name)
        return returnPro
        return make_response(jsonify("Something went wrong: ", str(e)), 500)


def share_link_note(id_note):
    try:
        note = (
            db.session.query(Notes, Datas)
            .join(Datas, Datas.idNote == Notes.idNote)
            .filter(Notes.idNote == id_note)
            .first()
        )

        if note is None:
            return jsonify({"status": 404, "message": "Note is not valid!"}), 404
        if not note.Notes.notePublic:
            return jsonify({"status": 401, "message": "Note is not public"}), 401
        public_note = {
            "id_note": note.Notes.idNote,
            "id_folder": note.Notes.idFolder,
            "id_user": note.Notes.idUser,
            "id_group": note.Notes.idGroup,
            "type": note.Notes.type,
            "title": note.Notes.title,
            "color": {
                "r": note.Notes.r,
                "g": note.Notes.g,
                "b": note.Notes.b,
                "a": note.Notes.a,
            },
            "create_at": note.Notes.createAt,
            "content": note.Datas.content,
            "image": note.Datas.image,
            "link_note_share": note.Notes.linkNoteShare,
        }
        return jsonify({"status": 200, "message": "Success", "Note": public_note})
    except Exception as e:
        return jsonify({"status": 500, "message": f"Something went wrong! {e}"}), 500


def countView(idNote):
    try:
        note = Notes.query.filter(Notes.idNote == idNote).first()
        view = int(note.view)
        note.view = view + 1
        db.session.commit()
        return jsonify({"status": 200, "message": "Update view successful"})
    except Exception as e:
        return jsonify({"status": 500, "message": f"Something went wrong! {e}"}), 500


def favorite(idComment):
    try:
        json = request.json
        type = json["type"]
        idUser = json["idUser"]
        comment = Comments.query.filter(Comments.id == idComment).first()
        if comment:
            fav = Favorites.query.filter(
                Favorites.idComment == idComment, Favorites.idUser == idUser
            ).first()
            if fav:
                if fav.type == type:
                    db.session.delete(fav)
                    db.session.commit()
                    return jsonify(
                        {"status": 200, "message": "Remove favorite successful"}
                    )
                else:
                    fav.type = type
                    db.session.commit()
                    return jsonify(
                        {"status": 200, "message": "Update favorite successful"}
                    )
            else:
                favorite = Favorites(idComment=idComment, idUser=idUser, type=type)
                db.session.add(favorite)
                db.session.commit()
                return jsonify({"status": 200, "message": "Add favorite successful"})
        else:
            return jsonify({"status": 500, "message": "Comment is not exist"})
    except Exception as e:
        return jsonify({"status": 500, "message": f"Something went wrong! {e}"}), 500
