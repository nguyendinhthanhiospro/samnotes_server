from source import db
from flask import request, make_response, jsonify
from source.main.model.chat1vs1 import Chat1vs1
from source.main.model.relationship import Relationship
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label, text
from source.main.model.users import Users
from socket import *
import base64
from source.main.model.ChatGroupModel import ChatGroupModel


def base64ToByte(base64data):
    if base64data:
        try:
            missing_padding = 4 - len(base64data) % 4
            if missing_padding:
                base64data += "=" * missing_padding
            image = base64.b64decode(base64data)
            return image
        except base64.binascii.Error as e:
            print("Base64 decoding error:", str(e))
            return None
        except Exception as e:
            print("Error decoding base64 to byte:", str(e))
            return None
    return None


def byteToString(byte):
    if byte:
        try:
            base64_string = base64.b64encode(byte).decode("utf-8")
            return str(base64_string)
        except Exception as e:
            print("Error encoding byte to string:", str(e))
            return None
    return None


def handleSearch1Chat1(id, text, page):
    try:
        txt = text
        chats11Tong1 = (
            Chat1vs1.query.filter(
                Chat1vs1.text.ilike(f"%{txt}%"),
                Chat1vs1.idSend == id,
            )
            .order_by(Chat1vs1.sendAt.desc())
            .all()
        )
        chats11Tong2 = (
            Chat1vs1.query.filter(
                Chat1vs1.text.ilike(f"%{txt}%"),
                Chat1vs1.idReceive == id,
            )
            .order_by(Chat1vs1.sendAt.desc())
            .all()
        )
        limit = 50
        tongsopage1 = len(chats11Tong1) / limit
        tongsopage2 = len(chats11Tong2) / limit
        print(
            "_________tongsopage______",
            str(tongsopage1)
            + "____chats11Tong2____"
            + str(len(chats11Tong2) / limit)
            + "____chats11Tong1____"
            + str(len(chats11Tong1) / limit),
        )
        offset1 = 0
        offset2 = 0
        if tongsopage1 > 0 and tongsopage1 < 1:
            offset1 = (1 - page) * limit
            print("______OFFSET___" + str(offset1))
        if tongsopage1 == 0 and tongsopage2 == 0:
            return jsonify(
                {
                    "status": 200,
                    "data": {},
                    "message": "No data search chat",
                    "numberPage": 0,
                }
            )
        if tongsopage1 >= 1:
            offset1 = (tongsopage1 - int(page)) * limit
        data = []

        if offset1 >= 0:
            chat11_1trang_a = (
                Chat1vs1.query.filter(
                    Chat1vs1.text.ilike(f"%{txt}%"), Chat1vs1.idSend == id
                )
                .order_by(Chat1vs1.sendAt.desc())
                .offset(offset1)
                .limit(limit)
            )
            if chat11_1trang_a:
                for chat_a in chat11_1trang_a:
                    if chat_a.state == "not seen":
                        IsSeen = 0
                    else:
                        IsSeen = 1
                    Image = ""
                    if chat_a.type == "image":
                        Image = chat_a.linkImage
                    if chat_a.type in ["icon-image", "muti-image"]:
                        Image = chat_a.linkImage
                    Gif = ""
                    if chat_a.type == "gif":
                        Gif = chat_a.gif
                    userSend = Users.query.filter(Users.id == chat_a.idSend).first()
                    userReceive = Users.query.filter(
                        Users.id == chat_a.idReceive
                    ).first()
                    result = {
                        "MessageID": chat_a.id,
                        "SenderID": chat_a.idSend,
                        "UserNameSender": userSend.user_name,
                        "UserNameReceive": userReceive.user_name,
                        "linkAvatarSender": userSend.linkAvatar,
                        "linkAvatarReceive": userReceive.linkAvatar,
                        "GroupName": str(userSend.user_name)
                        + " - "
                        + str(userReceive.user_name),
                        "ReceivedID": chat_a.idReceive,
                        "Content": chat_a.text,
                        "MessageTime": chat_a.sendAt.strftime(
                            "%a, %d %b %Y %H:%M:%S GMT"
                        ),
                        "IsSeen": IsSeen,
                        "Image": Image,
                        "Gif": Gif,
                        "Type": chat_a.type,
                    }
                    data.append(result)
        if offset2 >= 0:
            chat11_1trang_b = (
                Chat1vs1.query.filter(
                    Chat1vs1.text.ilike(f"%{txt}%"), Chat1vs1.idReceive == id
                )
                .order_by(Chat1vs1.sendAt.desc())
                .offset(offset2)
                .limit(limit)
            )
            if chat11_1trang_b:
                for chat_b in chat11_1trang_b:
                    print("________chat11_1trang_b_________" + str(chat_b.idSend))
                    if chat_b.state == "not seen":
                        IsSeen = 0
                    else:
                        IsSeen = 1
                    Image = ""
                    if chat_b.type == "image":
                        Image = chat_b.linkImage
                    if chat_b.type in ["icon-image", "muti-image"]:
                        Image = chat_b.linkImage
                    Gif = ""
                    if chat_b.type == "gif":
                        Gif = chat_b.gif
                    userSend = Users.query.filter(Users.id == chat_b.idSend).first()
                    userReceive = Users.query.filter(
                        Users.id == chat_b.idReceive
                    ).first()
                    result = {
                        "MessageID": chat_b.id,
                        "SenderID": chat_b.idSend,
                        "UserNameSender": userSend.user_name,
                        "UserNameReceive": userReceive.user_name,
                        "linkAvatarSender": userSend.linkAvatar,
                        "linkAvatarReceive": userReceive.linkAvatar,
                        "GroupName": str(userSend.user_name)
                        + " - "
                        + str(userReceive.user_name),
                        "ReceivedID": chat_b.idReceive,
                        "Content": chat_b.text,
                        "MessageTime": chat_b.sendAt.strftime(
                            "%a, %d %b %Y %H:%M:%S GMT"
                        ),
                        "IsSeen": IsSeen,
                        "Image": Image,
                        "Gif": Gif,
                        "Type": chat_b.type,
                    }
                    data.append(result)

        if len(data) == 0:
            return {
                "status": 300,
                "data": [],
                "numberPage": 0,
                "message": "No Data Search",
            }
        tongsopageTrungBinh = 0
        if tongsopage1 >= tongsopage2:
            tongsopageTrungBinh = tongsopage1
        else:
            tongsopageTrungBinh = tongsopage2
        return {
            "status": 200,
            "data": data,
            "numberPage": tongsopageTrungBinh,
            "numberItem": len(data),
            "message": "Done Search Chat",
        }
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        return {
            "status": 500,
            "data": [],
            "numberPage": 0,
            "message": "Exception " + str(e),
        }


def chat1vs1(id):
    if request.method == "GET":
        try:
            chat = db.session.execute(
                text(
                    "Select * from users inner join chat1vs1 on users.id= chat1vs1.idReceive"
                )
            )
            data = []

            for row in chat:
                view_chat = {}
                view_chat["idSend"] = row.idSend
                view_chat["idReceive"] = row.idReceive
                view_chat["name"] = row.name
                view_chat["text"] = row.text
                view_chat["img"] = row.linkImage
                view_chat["gif"] = row.gif
                view_chat["state"] = row.state
                view_chat["sendAt"] = row.sendAt
                data.append(view_chat)
            return {"state": 200, "data": data}
        except Exception as e:
            print(e)
            return make_response(jsonify({"status": 400, "message": str(e)}), 400)
    if request.method == "POST":
        json = request.json
        print(json)
        print(json["sendAt"])
        try:
            sentAt_time = datetime.strptime(json["sendAt"], "%d/%m/%Y %H:%M %p %z")
            print(json["content"])
            if json["type"] in ["image", "icon-image", "muti-image"]:
                newchat1vs1 = Chat1vs1(
                    sendAt=sentAt_time, idReceive=id, img=json["content"]
                )
            else:
                newchat1vs1 = Chat1vs1(
                    sendAt=sentAt_time, idReceive=id, text=json["content"]
                )
            print("loi o ghep su kien")
            userFind = Users.query.filter(Users.user_name == json["user_name"]).first()
            userFind.last_activity_time = datetime.now()
            db.session.add(userFind)
            db.session.commit()
            if json["idSend"]:
                newchat1vs1.idSend = json["idSend"]
            db.session.add(newchat1vs1)
            db.session.commit()
            chat_parse = {}
            chat_parse["id"] = newchat1vs1.id
            chat_parse["idSend"] = newchat1vs1.idSend
            chat_parse["idReceive"] = newchat1vs1.idReceive
            chat_parse["content"] = newchat1vs1.text
            chat_parse["img"] = newchat1vs1.linkImage
            chat_parse["gif"] = newchat1vs1.gif
            chat_parse["sendAt"] = str(newchat1vs1.sendAt)
            return {"status": 200, "message": chat_parse}
        except:
            return make_response(
                jsonify(
                    {"status": 300, "message": "Sonpipi Request fail. Please try again"}
                ),
                300,
            )
    if request.method == "DELETE":
        pass


def blockchat(id):
    if request.method == "GET":
        try:
            chat = db.session.execute(
                text(
                    "Select * from users inner join relationship on users.id= relationship.idReceive"
                )
            )
            data = []
            userFind = Users.query.filter(Users.user_name == json["idReceive"]).first()
            userFind.last_activity_time = datetime.now()
            db.session.add(userFind)
            db.session.commit()
            for row in chat:
                view_chat = {}
                view_chat["idSend"] = row.idSend
                view_chat["idReceive"] = row.idReceive
                view_chat["relationship"] = row.relation
                data.append(view_chat)
            return {"state": 200, "data": data}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    if request.method == "POST":
        json = request.json  # Get JSON data from the request
        try:
            # Try to find an existing relationship in the database based on certain conditions
            user1 = Relationship.query.filter(
                (Relationship.idSend == id)
                & (Relationship.idReceive == json["idReceive"])
            ).first()
            user2 = Relationship.query.filter(
                (Relationship.idReceive == id)
                & (Relationship.idSend == json["idReceive"])
            ).first()
            if user1 or user2:
                # If a relationship exists, return its status
                return {"status": 200, "relation is": user1.relation}
            else:
                # If no relationship exists, create a new one with relation set to True
                new_relation1 = Relationship(
                    idSend=id, idReceive=json["idReceive"], relation=True
                )
                new_relation2 = Relationship(
                    idReceive=id, idSend=json["idReceive"], relation=True
                )
                db.session.add(new_relation1)
                db.session.add(new_relation2)
                db.session.commit()

                # Prepare a response message
                chat_parse = {
                    "id": new_relation1.id,
                    "idSend": new_relation1.idSend,
                    "idReceive": new_relation1.idReceive,
                    "relation": new_relation1.relation,
                }

                # Return a JSON response with the newly created relationship data
                return {"status": 200, "message": chat_parse}
        except Exception as e:
            # Handle exceptions, e.g., database errors
            print(e)
            return make_response(
                jsonify(
                    {"status": 300, "message": "Sonpipi Request fail. Please try again"}
                ),
                300,
            )
    if request.method == "PATCH":
        json = request.json  # Get JSON data from the request
        try:
            # Try to find an existing relationship in the database based on certain conditions
            user = Relationship.query.filter(
                (Relationship.idSend == id)
                & (Relationship.idReceive == json["idReceive"])
            ).first()
            if user:
                # If a relationship exists, return its status
                user.relation = json["relation"]
                db.session.commit()
                chat_parse = {
                    "id": user.id,
                    "idSend": user.idSend,
                    "idReceive": user.idReceive,
                    "relation": user.relation,
                }
                return {"status": 200, "message": chat_parse}
            else:
                return {"status": 200, "message": "no relationship"}
        except Exception as e:
            # Handle exceptions, e.g., database errors
            print(e)
            return make_response(
                jsonify(
                    {"status": 300, "message": "Sonpipi Request fail. Please try again"}
                ),
                300,
            )


def statemessage(id):
    try:
        if request.method == "POST":
            message = Chat1vs1.query.filter(Chat1vs1.id == id).first()
            if message == None:
                return make_response(
                    jsonify(
                        {"status": 202, "message": "Cant find id message: " + str(id)}
                    ),
                    202,
                )
            message.state = "seen"
            db.session.commit()
            return make_response(
                jsonify({"status": 200, "message": "state message change 'seen'"}),
                200,
            )
    except Exception as e:
        print(e)
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "message": "___Exception___" + str(e),
                }
            ),
            500,
        )


def statemessage_chatgroup(idMessage, idUser):
    try:
        if request.method == "GET":
            message = ChatGroupModel.query.filter(
                ChatGroupModel.idMes == idMessage
            ).first()
            if message == None:
                return make_response(
                    jsonify(
                        {
                            "status": 202,
                            "message": "Cant find id message: " + str(idMessage),
                        }
                    ),
                    202,
                )
            listIdUserReaded = message.listIdUserReaded
            print("_____listIdUserReaded____" + str(listIdUserReaded))
            if listIdUserReaded != None:
                print("______VAN_VAO_DAY_AH")
                listID = listIdUserReaded.split("#")
                check = 0
                for item in listID:
                    print("___PRO___" + str(listID))
                    if len(item) > 0:
                        print("_____KO VAO")
                        if item == str(idUser):
                            check = 1
                            break
                if check == 0:
                    if len(listIdUserReaded) == 0:
                        listIdUserReaded = str(idUser)
                    else:
                        listIdUserReaded = listIdUserReaded + "#" + str(idUser)
            else:
                listIdUserReaded = str(idUser)
            message.listIdUserReaded = listIdUserReaded
            db.session.commit()
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "message": "state message change 'seen' list id seen message: "
                        + listIdUserReaded,
                    }
                ),
                200,
            )
    except Exception as e:
        print(e)
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "message": "___Exception___" + str(e),
                }
            ),
            500,
        )


def send_multiple_images_send_message(idMes):
    try:
        if request.method == "DELETE":
            message = Chat1vs1.query.filter(Chat1vs1.id == idMes).first()
            db.session.delete(message)
            db.session.commit()
            return make_response(
                jsonify({"message": "Deleted message", "status": 200}), 200
            )
        else:
            return make_response(
                jsonify({"message": "Method is not allowed", "status": 500}), 500
            )
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": f"Error {e}", "status": 500}), 500)


def deleteMessage(idMes):
    try:
        if request.method == "DELETE":
            message = Chat1vs1.query.filter(Chat1vs1.id == idMes).first()
            db.session.delete(message)
            db.session.commit()
            return make_response(
                jsonify({"message": "Deleted message", "status": 200}), 200
            )
        else:
            return make_response(
                jsonify({"message": "Method is not allowed", "status": 500}), 500
            )
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": f"Error {e}", "status": 500}), 500)


def getAllPhoto1Chat1():
    if request.method == "POST":
        json = request.form
        if json["idchat"] == None:
            return make_response(
                jsonify(
                    {
                        "status": 500,
                        "data": "____Method Post Only__and have body idchat",
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
        id1Chat1 = json["idchat"]
        page = json["page"]
        try:
            limit = 50
            toan_bo_tin_nhan_1room = Chat1vs1.query.filter(
                Chat1vs1.room == id1Chat1, Chat1vs1.linkImage != None
            ).all()
            tongsopage = len(toan_bo_tin_nhan_1room)
            if tongsopage == 0:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "message": "No image chat in "
                            + str(id1Chat1)
                            + " in database",
                            "data": [],
                        }
                    ),
                    300,
                )
            print("____TONG_SO_TIN_NHAN_____" + str(tongsopage))
            if tongsopage > 0 and tongsopage < 1:
                offset = (1 - int(page)) * limit
            if tongsopage >= 1:
                truPage = tongsopage - int(page)
                if truPage > -1 and truPage < 0:
                    truPage = 0
                offset = truPage * limit
            if offset < 0:
                return {
                    "status": 200,
                    "data": [],
                    "message": "page not found " + str(page),
                }
            if offset < 0:
                return {
                    "status": 200,
                    "data": [],
                    "message": "page not found " + str(page),
                }
            print("____OFFSET___" + str(offset))
            chat_room = (
                Chat1vs1.query.filter(
                    Chat1vs1.room == id1Chat1, Chat1vs1.linkImage != None
                )
                .order_by(Chat1vs1.sendAt.asc())
                .offset(offset)
                .limit(limit)
                .all()
            )
            data = []
            for chat in chat_room:
                chat_parse = {}
                chat_parse["image"] = chat.linkImage
                chat_parse["id"] = chat.id
                chat_parse["type"] = chat.type
                chat_parse["gif"] = ""
                # print("_________chat.type___________", chat.type)
                chat_parse["idSend"] = chat.idSend
                user = Users.query.filter(Users.id == chat.idSend).first()
                if user:
                    chat_parse["avt"] = user.linkAvatar
                    chat_parse["name"] = user.name
                else:
                    continue
                if (
                    chat.type == "image"
                    or chat.type == "muti-image"
                    or chat.type == "icon-image"
                ):
                    chat_parse["image"] = chat.linkImage
                elif chat.type == "gif":
                    gif = chat.gif
                    chat_parse["gif"] = gif
                else:
                    text = chat.text
                    print("____text chat____" + str(text))
                    chat_parse["content"] = text if text else ""
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "data": data,
                        "number_chat_have_image": len(data),
                        "number_all_page": tongsopage,
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
    return make_response(
        jsonify(
            {
                "status": 500,
                "data": "Data send error____" + str(request.method),
            }
        ),
        500,
    )
