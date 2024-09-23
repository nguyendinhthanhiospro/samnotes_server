import os
from source import db
from flask import request, make_response, jsonify, send_from_directory
from source.main.extend import base64ToByte
from source.main.function.middleware import *
from source.main.model.chatUnknowns import ChatUnknowns
from source.main.model.users import Users
from source.main.model.chat1vs1 import Chat1vs1
from sqlalchemy import func, or_, and_
from datetime import datetime
from sqlalchemy.sql import label
import base64
from sqlalchemy.sql import text
import mysql.connector
import json
import io, base64
from PIL import Image
from source.main.model.block_unknow import block_unknow
from source.main.model.ChatGroupModel import ChatGroupModel
from source.main.model.members import Members
from source.main.model.images import Images

config = {
    "user": "sonpro",
    "password": "Ratiendi89",
    "host": "localhost",
    "port": 3306,
    "database": "colornote",
    # 'auth_plugin': 'mysql_native_password'
}


def handleChatUnknowns():
    try:
        if request.method == "GET":

            # Truy vấn để lấy tin nhắn cuối cùng cho mỗi idSend của idReceiver cụ thể
            # subquery = (
            #     db.session.query(
            #         ChatUnknowns.idSend, func.max(ChatUnknowns.sendAt).label("max_sendAt")
            #     )
            #     .filter(ChatUnknowns.idReceive == param)
            #     .group_by(ChatUnknowns.idSend)
            #     .subquery()
            # )
            # query = db.session.query(ChatUnknowns).join(
            #     subquery,
            #     (ChatUnknowns.idSend == subquery.c.idSend)
            #     & (ChatUnknowns.sendAt == subquery.c.max_sendAt),
            # )

            # Lấy kết quả của truy vấn
            # latest_messages = query.all()
            json = request.json
            idRoom = json["idRoom"]
            chat = (
                ChatUnknowns.query.filter(ChatUnknowns.idRoom == idRoom)
                .order_by(ChatUnknowns.idMes.desc())
                .first()
            )
            res = {}
            chat_parse = {}
            chat_parse["id"] = chat.idMes
            chat_parse["idSend"] = chat.idSend
            chat_parse["idReceive"] = chat.idReceive
            chat_parse["status"] = chat.status
            chat_parse["lastest_text"] = chat.text
            chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
            res["data"] = chat_parse
            return res
        if request.method == "DELETE":
            pass
    except Exception as e:
        return {"status": 500, "message": str(e)}


def handleMessages_sendfile(id):
    # 28-6-2024: Nhat sua form get tra ve
    if request.method == "GET":
        try:
            chats = (
                ChatUnknowns.query.filter_by(idSend=id)
                .order_by(ChatUnknowns.sendAt.desc())
                .all()
            )
            user = Users.query.filter(Users.id == id).first()
            data = []
            for chat in chats:
                chat_parse = {}
                chat_parse["id"] = chat.idMes
                chat_parse["username"] = user.name
                chat_parse["avatar"] = user.linkAvatar
                chat_parse["idSend"] = chat.idSend
                chat_parse["idReceive"] = chat.idReceive
                chat_parse["content"] = chat.text
                chat_parse["img"] = chat.img
                chat_parse["gif"] = chat.gif
                chat_parse["type"] = chat.type
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)

            return {"status": 200, "data": data}
        except Exception as e:
            print(str(e))
            return {"status": 500, "message": str(e)}
    if request.method == "POST":
        PATH_IMAGE = "/var/www/samnote-build/image"
        try:
            input_data_json = request.form
            fileImage = request.files.get("img")
            sentAt_time = datetime.now()
            imgLink = make_url_apache_image(id, PATH_IMAGE, fileImage, "note")
            if input_data_json["idReceive"] == None:
                return {"status": 414, "message": "Please input idReceive in body"}
            list_block_unknow = block_unknow.query.filter(
                block_unknow.idUserOwner == input_data_json["idReceive"],
                block_unknow.idUserBlock == int(id),
            ).first()
            print("_____ctai sao crash o day____")
            if list_block_unknow != None:
                return {
                    "status": 405,
                    "message": "Account "
                    + str(input_data_json["idReceive"])
                    + " Block "
                    + str(id)
                    + " , Please Recheck",
                }
            print("________list_block_unknow________")
            user = Users.query.filter(Users.id == input_data_json["idReceive"]).first()
            if user == None:
                return {
                    "status": 209,
                    "message": "cant find user have id: "
                    + str(input_data_json["idReceive"]),
                }
            if user.isBlockAllUnknow == 1:
                return {
                    "status": 406,
                    "message": "Account "
                    + str(json["idReceive"])
                    + " Disable Receive Any Unknowns Message",
                }
            if input_data_json["type"] in ["image", "icon-image", "multi-image"]:
                print("______SONPRO_input_data_json____________________")
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(input_data_json["idReceive"]),
                    img=imgLink,
                    type=input_data_json["type"],
                    idSend=int(id),
                    idRoom=input_data_json["idRoom"],
                )
                print(
                    "_____________chatUnknowns_____________"
                    + str(chatUnknowns.idReceive)
                )
            elif input_data_json["type"] == "text":
                print("_____TYPE_CHUA_KIP_VAO____")
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(input_data_json["idReceive"]),
                    text=input_data_json["content"],
                    type=input_data_json["type"],
                    idSend=int(id),
                    idRoom=input_data_json["idRoom"],
                )
                print("______chatUnknowns_______" + str(chatUnknowns))
            elif input_data_json["type"] == "gif":
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(input_data_json["idReceive"]),
                    gif=input_data_json["gif"],
                    type=input_data_json["type"],
                    idSend=int(id),
                    idRoom=input_data_json["idRoom"],
                )
            print("__________chatUnknowns______________" + str(chatUnknowns))
            db.session.add(chatUnknowns)
            db.session.commit()
            chat_parse = {}
            chat_parse["id"] = int(chatUnknowns.idMes)
            chat_parse["idSend"] = int(chatUnknowns.idSend)
            chat_parse["idReceive"] = int(chatUnknowns.idReceive)
            chat_parse["content"] = chatUnknowns.text
            chat_parse["type"] = chatUnknowns.type

            chat_parse["img"] = chatUnknowns.img
            chat_parse["gif"] = chatUnknowns.gif
            if chatUnknowns.img != None:
                chat_parse["img"] = chatUnknowns.img
            if chatUnknowns.gif != None:
                chat_parse["gif"] = chatUnknowns.gif
            # chat_parse["gif"] = chatUnknowns.gif
            # chat_parse["type"] = chatUnknowns.type
            chat_parse["sendAt"] = chatUnknowns.sendAt.strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )
            chat_parse["idRoom"] = chatUnknowns.idRoom
            return {"status": 200, "message": chat_parse}
        except Exception as e:
            # Log the error message
            print("SQL Error:", str(e))
            return {"status": 500, "message": str(e)}


def DisableUnknownAccount(idUser):
    if request.method == "POST":
        try:
            userFind = Users.query.filter(Users.id == idUser).first()
            if userFind == None:
                return {
                    "status": 300,
                    "message": "Account " + str(userFind.user_name) + " cant find",
                }
            messagePro = ""
            if userFind.isBlockAllUnknow == 0:
                userFind.isBlockAllUnknow = 1
                messagePro = "Disable all user sent message unknowns"
            else:
                userFind.isBlockAllUnknow = 0
                messagePro = "Enable all user sent message unknowns"
            db.session.add(userFind)
            db.session.commit()
            return {"status": 200, "message": messagePro}
        except Exception as e:
            print(str(e))
            return {"status": 500, "message": str(e)}


def handleMessages(id):
    # 28-6-2024: Nhat sua form get tra ve
    if request.method == "GET":
        try:
            chats = (
                ChatUnknowns.query.filter_by(idSend=id)
                .order_by(ChatUnknowns.sendAt.desc())
                .all()
            )
            user = Users.query.filter(Users.id == id).first()
            data = []
            for chat in chats:
                chat_parse = {}
                chat_parse["id"] = chat.idMes
                chat_parse["username"] = user.name
                chat_parse["avatar"] = user.linkAvatar
                chat_parse["idSend"] = chat.idSend
                chat_parse["idReceive"] = chat.idReceive
                chat_parse["content"] = chat.text
                chat_parse["img"] = chat.img
                chat_parse["gif"] = chat.gif
                chat_parse["type"] = chat.type
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)

            return {"status": 200, "data": data}
        except Exception as e:
            print(str(e))
            return {"status": 500, "message": str(e)}
    if request.method == "POST":
        if json["idReceive"] == None:
            return {
                "status": 205,
                "message": "Please input body idReceive is owner user id",
            }
        list_block_unknow = block_unknow.query.filter(
            block_unknow.idUserOwner == json["idReceive"],
            block_unknow.idUserBlock == int(id),
        ).first()
        if list_block_unknow != None:
            return {
                "status": 405,
                "message": "Account "
                + str(json["idReceive"])
                + " Block "
                + str(id)
                + " , Please Recheck",
            }
        user = Users.query.filter(Users.id == json["idReceive"]).first()
        if user == None:
            return {
                "status": 209,
                "message": "cant find user have id: " + str(json["idReceive"]),
            }
        if user.isBlockAllUnknow == 1:
            return {
                "status": 406,
                "message": "Account "
                + str(json["idReceive"])
                + " Disable Receive Any Unknowns Message",
            }

        PATH_IMAGE = "/var/www/samnote-build/image"
        json = request.json
        try:
            print("__________" + str(request.json))
            sentAt_time = datetime.now()
            if "img" in json:
                print("______VAO____IMAGE___")
                if json["img"] != None and json["img"] != "":
                    img = make_url_image_base64(
                        id, PATH_IMAGE, base64.b64decode(json["img"]), "chat"
                    )
            if json["type"] in ["image", "icon-image", "multi-image"]:
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(json["idReceive"]),
                    img=img,
                    type=json["type"],
                    idSend=int(id),
                    idRoom=json["idRoom"],
                )
            elif json["type"] == "text":
                print("_____TYPE_CHUA_KIP_VAO____")
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(json["idReceive"]),
                    text=json["content"],
                    type=json["type"],
                    idSend=int(id),
                    idRoom=json["idRoom"],
                )
                print("______chatUnknowns_______" + str(chatUnknowns))
            elif json["type"] == "gif":
                chatUnknowns = ChatUnknowns(
                    sendAt=sentAt_time,
                    idReceive=int(json["idReceive"]),
                    gif=json["gif"],
                    type=json["type"],
                    idSend=int(id),
                    idRoom=json["idRoom"],
                )
                # if json["idSend"]:
                #     chatUnknowns.idSend = int(json["idSend"])
            print("________________________" + str(chatUnknowns))
            db.session.add(chatUnknowns)
            db.session.commit()
            chat_parse = {}
            chat_parse["id"] = int(chatUnknowns.idMes)
            chat_parse["idSend"] = int(chatUnknowns.idSend)
            chat_parse["idReceive"] = int(chatUnknowns.idReceive)
            chat_parse["content"] = chatUnknowns.text
            chat_parse["type"] = chatUnknowns.type

            chat_parse["img"] = chatUnknowns.img
            chat_parse["gif"] = chatUnknowns.gif
            if chatUnknowns.img != None:
                chat_parse["img"] = chatUnknowns.img
            if chatUnknowns.gif != None:
                chat_parse["gif"] = chatUnknowns.gif
            # chat_parse["gif"] = chatUnknowns.gif
            # chat_parse["type"] = chatUnknowns.type
            chat_parse["sendAt"] = chatUnknowns.sendAt.strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )
            chat_parse["idRoom"] = chatUnknowns.idRoom
            return {"status": 200, "message": chat_parse}
        except Exception as e:
            # Log the error message
            print("SQL Error:", str(e))
            return {"status": 500, "message": str(e)}


def block_chat_unknow():
    try:

        json = request.json
        if json["idUserOwner"] == None:
            return {"status": 201, "message": "body must have idUserOwner"}
        if json["idUserBlock"] == None:
            return {"status": 202, "message": "body must have idUserBlock"}
        if json["Reason"] == None:
            return {"status": 203, "message": "body must have Reason"}
        list_block_unknow = block_unknow.query.filter(
            block_unknow.idUserOwner == json["idUserOwner"],
            block_unknow.idUserBlock == json["idUserBlock"],
        ).first()
        if list_block_unknow != None:
            return {"status": 204, "message": "Account blocked unknown !!!!"}
        user_name = block_unknow(
            idUserOwner=json["idUserOwner"],
            idUserBlock=json["idUserBlock"],
            Reason=json["Reason"],
            createdAt=datetime.now(),
        )
        db.session.add(user_name)
        db.session.commit()
        dataReturn = {}
        dataReturn["idUserOwner"] = json["idUserOwner"]
        dataReturn["idUserBlock"] = json["idUserBlock"]
        dataReturn["Reason"] = json["Reason"]
        return {"status": 200, "message": "okie done", "data": dataReturn}
    except Exception as e:
        print(e)
        return {"status": 500, "message": "Exception___" + str(e)}


def handleMessagesRecevie():
    try:
        if request.method == "POST":
            json = request.json
            idRoom = json["idRoom"]
            print("______ROOM_____" + str(idRoom))
            page = request.args.get("page")
            tong_tin_nhan_unknow = ChatUnknowns.query.filter(
                ChatUnknowns.idRoom == idRoom
            ).all()
            limit = 50
            room2 = ""
            if len(tong_tin_nhan_unknow) == 0:
                room_split_dao_nguoc = idRoom.split("#")
                room2 = room_split_dao_nguoc[1] + "#" + room_split_dao_nguoc[0]
                tong_tin_nhan_unknow = ChatUnknowns.query.filter(
                    ChatUnknowns.idRoom == room2
                ).all()
                print("_______tong_tin_nhan_unknown____" + str(tong_tin_nhan_unknow))
            tongsopage = len(tong_tin_nhan_unknow) / limit
            print("_________tongsopage______", str(tongsopage))
            offset = 0
            if tongsopage == 0:
                return {
                    "status": 200,
                    "data": "id Room "
                    + str(idRoom)
                    + " or "
                    + str(room2)
                    + " - No room, please input room is: idUserSend#idUserRecive Example: 90#71",
                }
            if tongsopage > 0 and tongsopage < 1:
                offset = (1 - int(page)) * limit
                print("______" + str(offset))
            else:
                offset = (tongsopage - int(page)) * limit
            chats = (
                ChatUnknowns.query.filter(ChatUnknowns.idRoom == idRoom)
                .order_by(ChatUnknowns.sendAt.asc())
                .offset(offset)
                .limit(limit)
            )
            data = []
            for chat in chats:
                chat_parse = {}
                chat_parse["id"] = chat.idMes
                chat_parse["idSend"] = chat.idSend
                chat_parse["idReceive"] = chat.idReceive
                chat_parse["content"] = chat.text
                chat_parse["img"] = chat.img
                chat_parse["gif"] = chat.gif
                chat_parse["type"] = chat.type
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)
            return {
                "status": 200,
                "data": data,
                "numberPage": tongsopage,
                "numberItem": len(data),
            }
    except Exception as e:
        return {"status": 500, "message": str(e), "numberPage": 0, "numberItem": 0}


def handleListUser(id):
    try:
        if request.method == "GET":
            roomKnows = (
                ChatUnknowns.query.filter(ChatUnknowns.idRoom.ilike(f"{id}#%"))
                .with_entities(ChatUnknowns.idRoom)
                .distinct()
                .all()
            )
            roomUnknows = (
                ChatUnknowns.query.filter(ChatUnknowns.idRoom.ilike(f"%#{id}"))
                .with_entities(ChatUnknowns.idRoom)
                .distinct()
                .all()
            )
            res = []
            for room in roomKnows:
                chat = (
                    ChatUnknowns.query.filter(ChatUnknowns.idRoom == room.idRoom)
                    .order_by(ChatUnknowns.idMes.desc())
                    .first()
                )
                if str(id) == str(chat.idSend):
                    user = Users.query.filter(Users.id == chat.idReceive).first()
                else:
                    user = Users.query.filter(Users.id == chat.idSend).first()
                data_user = {}
                data_user["idUser"] = user.id
                data_user["username"] = user.user_name
                data_user["avatar"] = user.linkAvatar
                if chat.type in ["image", "multi-image", "icon-image", "gif"]:
                    last_text = "sent an image"
                else:
                    last_text = chat.text
                res.append(
                    {
                        "idRoom": chat.idRoom,
                        "idSend": chat.idSend,
                        "idReceive": chat.idReceive,
                        "idMessage": chat.idMes,
                        "last_text": last_text,
                        "send_at": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        "user": data_user,
                    }
                )
            for room in roomUnknows:
                chat = (
                    ChatUnknowns.query.filter(ChatUnknowns.idRoom == room.idRoom)
                    .order_by(ChatUnknowns.idMes.desc())
                    .first()
                )
                if chat.type in ["image", "multi-image", "icon-image", "gif"]:
                    last_text = "sent an image"
                else:
                    last_text = chat.text
                data_user = {}
                data_user["idUser"] = 0
                data_user["username"] = "Anonymous"
                data_user["avatar"] = (
                    "http://samnote.mangasocial.online/get-image-chat/0/anonymous.png"
                )
                res.append(
                    {
                        "idRoom": chat.idRoom,
                        "idSend": chat.idSend,
                        "idReceive": chat.idReceive,
                        "idMessage": chat.idMes,
                        "last_text": last_text,
                        "send_at": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        "user": data_user,
                    }
                )
            result = sorted(res, key=lambda x: x["idMessage"], reverse=True)
            return {"status": 200, "data": result}
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        return {"status": 500, "message": str(e)}


def handleListUserChat1vs1(id):
    try:
        if request.method == "GET":
            # print("pass1")
            latest_in_room = (
                db.session.query(
                    Chat1vs1.room, func.max(Chat1vs1.sendAt).label("latestSend")
                )
                .filter(or_(Chat1vs1.idSend == id, Chat1vs1.idReceive == id))
                .group_by(Chat1vs1.room)
                .subquery()
            )
            # print("pass2")
            chats = (
                db.session.query(Chat1vs1)
                .join(
                    latest_in_room,
                    and_(
                        Chat1vs1.room == latest_in_room.c.room,
                        Chat1vs1.sendAt == latest_in_room.c.latestSend,
                    ),
                )
                .all()
            )
            result_data = []
            for chat in chats:
                if str(chat.idSend) == str(id):
                    User = Users.query.filter(Users.id == chat.idReceive).first()
                else:
                    User = Users.query.filter(Users.id == chat.idSend).first()
                if chat.state == "not seen":
                    isSeen = 0
                else:
                    isSeen = 1
                last_text = ""
                if chat.type in ["image", "multi-image", "icon-image", "gif"]:
                    last_text = "sent an image"
                else:
                    last_text = chat.text

                result_data.append(
                    {
                        "idReceive": chat.idReceive,
                        "idSend": chat.idSend,
                        "idMessage": chat.id,
                        "idRoom": chat.room,
                        "last_text": last_text,
                        "sendAt": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        "is_seen": isSeen,
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
                            "df_color": {
                                "r": User.r,
                                "g": User.g,
                                "b": User.b,
                                "a": User.a,
                            },
                        },
                    }
                )
            data = sorted(result_data, key=lambda x: x["idMessage"], reverse=True)
            print("pass4")
            return {"status": 200, "data": data}
    except Exception as e:
        return {"status": 500, "message": str(e)}


def get_all_message(idUser):
    if request.method == "GET":
        try:
            groups_have_mem = db.session.execute(
                text(
                    "Select * from members as m inner join `groups` as g on m.idGroup=g.idGroup where m.idUser={} ORDER BY g.last_time_chat DESC".format(
                        idUser
                    )
                )
            )

            dataReturn = []

            textCuoiCung_chat = ""
            dem_so_group_member_ben_trong = 0
            for item_group in groups_have_mem:
                print("____________________________item__" + str(item_group))
                dem_so_group_member_ben_trong = dem_so_group_member_ben_trong + 1
                chatLastest = (
                    ChatGroupModel.query.filter(
                        ChatGroupModel.idGroup == item_group.idGroup,
                    )
                    .order_by(ChatGroupModel.sendAt.desc())
                    .first()
                )
                group_if = {}
                listUserReaded = []
                textCuoiCung_chat = ""
                if chatLastest != None:
                    if chatLastest.text != None:
                        textCuoiCung_chat = chatLastest.text
                    else:
                        textCuoiCung_chat = "Sent an image"
                    group_if["id_lastest_message_in_group"] = chatLastest.idMes
                    listIdUserReaded = chatLastest.listIdUserReaded
                    if listIdUserReaded != None:
                        if len(listIdUserReaded) > 0:
                            listID = listIdUserReaded.split("#")
                            for itemID in listID:
                                itemUser = {}
                                userReaded = Users.query.filter(
                                    Users.id == itemID
                                ).first()
                                if userReaded != None:
                                    itemUser["avatar"] = userReaded.linkAvatar
                                    itemUser["idUser"] = itemID
                                    itemUser["username"] = userReaded.user_name
                                    listUserReaded.append(itemUser)
                group_if["listUserReaded"] = listUserReaded

                group_if["idGroup"] = item_group.idGroup
                tv = db.session.execute(
                    text(
                        "select count(idMember) as thanh_vien from members as m where m.idGroup={}".format(
                            item_group.idGroup
                        )
                    )
                )
                for row in tv:
                    group_if["numberMems"] = row.thanh_vien

                members = Members.query.filter(
                    Members.idGroup == item_group.idGroup
                ).all()
                result_members = []
                for member in members:
                    userr = Users.query.filter(Users.id == member.idUser).first()
                    result_members.append(
                        {
                            "idUser": userr.id,
                            "idMem": member.idMember,
                            "userName": userr.user_name,
                            "linkAvatar": userr.linkAvatar,
                        }
                    )
                group_if["text_lastest_message_in_group"] = textCuoiCung_chat
                group_if["member"] = result_members
                group_if["name"] = item_group.name
                group_if["linkAvatar"] = item_group.linkAvatar
                group_if["createAt"] = str(item_group.createAt)
                group_if["idOwner"] = item_group.idOwner
                group_if["describe"] = item_group.describe
                group_if["color"] = {
                    "r": item_group.r,
                    "g": item_group.g,
                    "b": item_group.b,
                    "a": item_group.a,
                }
                nextpro = item_group.last_time_chat.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
                print("__________________nextpro____" + str(nextpro))
                group_if["last_time_chat"] = nextpro
                group_if["type_chat"] = "chatgroup"
                dataReturn.append(group_if)

            if dem_so_group_member_ben_trong == 0:
                return {
                    "status": 204,
                    "data": [],
                    "message": "You must input True idMember: "
                    + str(idUser)
                    + " because cant find idMember in all group",
                }
            # _______________________________________________________________________SO_PHAN_TU_CHAT_1_1_________________________
            latest_in_room = (
                db.session.query(
                    Chat1vs1.room, func.max(Chat1vs1.sendAt).label("latestSend")
                )
                .filter(or_(Chat1vs1.idSend == idUser, Chat1vs1.idReceive == idUser))
                .group_by(Chat1vs1.room)
                .subquery()
            )
            # print("pass2")
            chats = (
                db.session.query(Chat1vs1)
                .join(
                    latest_in_room,
                    and_(
                        Chat1vs1.room == latest_in_room.c.room,
                        Chat1vs1.sendAt == latest_in_room.c.latestSend,
                    ),
                )
                .all()
            )
            result_data = []
            for chat in chats:
                if str(chat.idSend) == str(idUser):
                    User = Users.query.filter(Users.id == chat.idReceive).first()
                else:
                    User = Users.query.filter(Users.id == chat.idSend).first()
                if chat.state == "not seen":
                    isSeen = 0
                else:
                    isSeen = 1
                last_text = ""
                if chat.type in ["image", "multi-image", "icon-image", "gif"]:
                    last_text = "sent an image"
                else:
                    last_text = chat.text

                dataReturn.append(
                    {
                        "type_chat": "1chat1",
                        "idReceive": chat.idReceive,
                        "idSend": chat.idSend,
                        "idMessage": chat.id,
                        "idRoom": chat.room,
                        "last_text": last_text,
                        "sendAt": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        "last_time_chat": chat.sendAt.strftime(
                            "%a, %d %b %Y %H:%M:%S GMT"
                        ),
                        "is_seen": isSeen,
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
                            "df_color": {
                                "r": User.r,
                                "g": User.g,
                                "b": User.b,
                                "a": User.a,
                            },
                        },
                    }
                )

            new_lst = sorted(
                dataReturn,
                key=lambda x: datetime.strptime(
                    x["last_time_chat"], "%a, %d %b %Y %H:%M:%S GMT"
                ),
            )
            proReturn = new_lst[::-1]
            return {"status": 200, "data": proReturn}

        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 500, "message": "EXCEPTION____" + str(e)}),
                500,
            )
    else:
        return {
            "status": 400,
            "message": "Invalid request method, Please use Get Method",
        }


def handleGetMesChat1vs1(id, idReceived):
    try:
        page = request.args.get("page", default=1, type=int)
        if request.method == "GET":
            chats_toan_bo = (
                Chat1vs1.query.filter(
                    or_(
                        (Chat1vs1.idSend == id) & (Chat1vs1.idReceive == idReceived),
                        (Chat1vs1.idSend == idReceived) & (Chat1vs1.idReceive == id),
                    )
                )
                .order_by(Chat1vs1.sendAt.asc())
                .all()
            )
            list_room = []
            for chat in chats_toan_bo:
                if not chat.room in list_room:
                    print("_______ROOM____" + str(chat.room))
                    list_room.append(chat.room)

            res = []
            for room in list_room:
                all_mess = {}
                all_mess["room"] = room

                # Separate page
                limit = 50
                toan_bo_tin_nhan_1room = Chat1vs1.query.filter(
                    Chat1vs1.room == room
                ).all()

                tongtinnhan = len(toan_bo_tin_nhan_1room)
                print("____TONG_SO_TIN_NHAN_____" + str(tongtinnhan))
                sotrang = tongtinnhan / limit
                if sotrang == 0:
                    return {
                        "status": 200,
                        "message": "error no message " + str(id),
                        "data": [],
                    }
                if sotrang < 1 and sotrang > 0:
                    sotrang = 1
                offset = (sotrang - page) * limit
                if offset < 0:
                    continue

                chat_room = (
                    Chat1vs1.query.filter(Chat1vs1.room == room)
                    .order_by(Chat1vs1.sendAt.asc())
                    .offset(offset)
                    .limit(limit)
                    .all()
                )
                messages = []

                for chat in chat_room:
                    message = {}
                    message["id"] = chat.id
                    message["idSend"] = chat.idSend
                    message["idReceive"] = chat.idReceive
                    message["text"] = chat.text
                    message["type"] = chat.type
                    message["image"] = chat.linkImage
                    message["gif"] = chat.gif
                    message["state"] = chat.state
                    message["sendAt"] = chat.sendAt.strftime(
                        "%a, %d %b %Y %H:%M:%S GMT"
                    )
                    images_send = Images.query.filter(Images.idChat1_1 == chat.id)
                    link_image = []
                    for image_item in images_send:
                        link_image.append(
                            {"id": image_item.idImage, "link": image_item.link}
                        )
                    if len(link_image) > 0:
                        message["list_images"] = link_image
                    messages.append(message)

                all_mess["messages"] = messages
                res.append(all_mess)

            return {"status": 200, "data": res}

    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        return {"status": 500, "message": str(e)}


def handleSearchText(id, text):
    try:
        txt = text
        chats = (
            ChatUnknowns.query.filter(ChatUnknowns.text.ilike(f"%{txt}%"))
            .order_by(ChatUnknowns.idMes.desc())
            .all()
        )
        if chats:
            data = []
            for chat in chats:
                info = {}
                print("__chat.idRoom___" + str(chat.idRoom) + "______" + str(id))
                if str(chat.idRoom.split("#")[0]) == str(id):
                    user = Users.query.filter(Users.id == chat.idReceive).first()
                    info["idUser"] = user.id
                    info["username"] = user.user_name
                    info["avatar"] = user.linkAvatar
                if str(chat.idRoom.split("#")[1]) == str(id):
                    user = Users.query.filter(Users.id == chat.idReceive).first()
                    info["idUser"] = user.id
                    info["username"] = user.user_name
                    info["avatar"] = user.linkAvatar
                data.append(
                    {
                        "idSend": int(chat.idSend),
                        "idReceive": int(chat.idReceive),
                        "idMessage": chat.idMes,
                        "text": chat.text,
                        "sendAt": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                        "user": info,
                        "idRoom": chat.idRoom,
                    }
                )
            return {"status": 200, "data": data}
        else:
            return {"status": 500, "message": "No result"}

    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        return {"status": 500, "message": str(e)}


def handleDeleteChatUnknown():
    try:
        json = request.json
        idRoom = json["idRoom"]
        print(idRoom)
        chats = ChatUnknowns.query.filter(ChatUnknowns.idRoom == idRoom).all()
        for chat in chats:
            db.session.delete(chat)
        db.session.commit()
        return {"status": 200, "message": "Delete Successful"}
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        return {"status": 500, "message": str(e)}


def getAllPhotoChatUnknow():
    if request.method == "POST":
        json = request.form
        if json["idroom"] == None:
            return make_response(
                jsonify(
                    {
                        "status": 500,
                        "data": "____Method Post Only__and have body idroom",
                    }
                ),
                500,
            )
        if json["page"] == None:
            return make_response(
                jsonify(
                    {
                        "status": 500,
                        "data": "____Method Post Only__and have body page",
                    }
                ),
                500,
            )
        idroom = json["idroom"]
        page = json["page"]
        try:
            res = {}
            limit = 50
            toan_bo_tin_nhan_1room = ChatUnknowns.query.filter(
                ChatUnknowns.idRoom == idroom, ChatUnknowns.img != None
            ).all()
            tongtinnhan = len(toan_bo_tin_nhan_1room)
            if tongtinnhan == 0:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "message": "No image chat in "
                            + str(idroom)
                            + " in database",
                            "data": [],
                        }
                    ),
                    300,
                )
            print("____TONG_SO_TIN_NHAN_____" + str(tongtinnhan))
            sotrang = tongtinnhan / limit
            if sotrang == 0:
                return {
                    "status": 200,
                    "message": "error no message " + str(id),
                    "data": [],
                }
            if sotrang < 1 and sotrang > 0:
                sotrang = 1
            offset = (sotrang - int(page)) * limit
            if offset < 0:
                return {
                    "status": 200,
                    "data": [],
                    "message": "page not found " + str(page),
                }
            print("____OFFSET___" + str(offset))
            chat_room = (
                ChatUnknowns.query.filter(
                    ChatUnknowns.idRoom == idroom, ChatUnknowns.img != None
                )
                .order_by(ChatUnknowns.sendAt.asc())
                .offset(offset)
                .limit(limit)
                .all()
            )
            data = []
            for chat in chat_room:
                chat_parse = {}
                chat_parse["id"] = chat.idMes
                chat_parse["idSend"] = chat.idSend
                chat_parse["idReceive"] = chat.idReceive
                chat_parse["status"] = chat.status
                chat_parse["image"] = chat.img
                chat_parse["lastest_text"] = chat.text
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                res["data"] = chat_parse
                data.append(chat_parse)
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "data": data,
                        "number_chat_have_image": tongtinnhan,
                        "number_all_page": sotrang,
                    }
                ),
                200,
            )
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 500, "data": "____Error___" + str(e)}),
                500,
            )

    else:
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "data": "____Method Post Only___CURRENT_" + str(request.method),
                }
            ),
            500,
        )
