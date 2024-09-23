from flask_socketio import emit, join_room, leave_room, socketio
from flask import request
from source import socketIo, db, connected_clients
from source.main.model.ChatGroupModel import ChatGroupModel
from source.main.model.chat1vs1 import Chat1vs1
from source.main.model.relationship import Relationship
from datetime import datetime
from sqlalchemy import and_
from source.main.function.middleware import *
from source.main.function.handlenotification import *
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
import base64

from source.main.model.groups import Groups

# chat = db.session.execute(text(
#                             'Select * from users inner join chat1vs1 on users.id= chat1vs1.idReceive'))


def byteToString(byte):
    if byte:
        try:
            base64_string = base64.b64encode(byte).decode("utf-8")
            return str(base64_string)
        except Exception as e:
            print("Error encoding byte to string:", str(e))
            return None
    return None


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


@socketIo.on("online")
def online(data):
    try:
        fl = True
        # print('client connect')
        for obj in connected_clients:
            if obj.get("id") == data["user"]["id"]:
                fl = False
                break
        if fl == True:
            connected_clients.append(data["user"])
        print(connected_clients)
        # Gửi danh sách client đang kết nối cho client vừa kết nối thành công
        emit("online", {"online": connected_clients})
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}),
            400,
        )


@socketIo.on("offline")
def offline(client_id):
    try:
        # print(f"user :{client_id}")
        # print("client offline")
        for obj in connected_clients:
            if obj.get("id") == client_id:
                connected_clients.remove(obj)
                print(connected_clients)
                break

        # Gửi danh sách client đang kết nối cho client vừa kết nối thành công
        emit("offline", {"online": connected_clients})
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}),
            400,
        )


@socketIo.on("connect")
def connected(data):

    # client_id = request.sid

    # #  print(connected_clients)
    # emit("connect", {"online": connected_clients})
    try:
        emit("connected", {"message": "Connected Sucessfully"})
    except Exception as e:
        emit("connected", {"message": "Error"})


@socketIo.on("disconnected")
def disconnected():
    try:
        # print("User disconnected")
        emit("disconnected", f"User {request.sid} is connected", broadcast=True)
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}),
            400,
        )


@socketIo.on("join")
def on_join(data):
    room = data["room"]
    join_room(room)


# print("join")


@socketIo.on("leave")
def on_leave(data):
    room = data["room"]
    leave_room(room)


#  print("leave")


@socketIo.on("join_group")
def handle_join_group(data):
    try:
        room = data["room"]
        join_room(room)
        # print(" ")
        # Truy vấn tin nhắn từ cơ sở dữ liệu và gửi chúng đến người dùng
        messages = ChatGroupModel.query.filter(ChatGroupModel.idGroup == room).all()
        for message in messages:
            if message.type == "text":
                emit(
                    "message",
                    {
                        "sender": message.idSend,
                        "content": message.text,
                        "type": message.type,
                    },
                )
            elif message.type in ["image", "icon-image"]:
                emit(
                    "message",
                    {
                        "sender": message.idSend,
                        "content": message.img,
                        "type": message.type,
                    },
                )
            # elif message.type == "gif":
            #     emit(
            #         "message",
            #         {
            #             "sender": message.idSend,
            #             "content": message.gif,
            #             "type": message.type,
            #         },
            #     )

        emit("join_room", {"message": "Join Successful"}, room=room)
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        emit("send_message", {"message": "Error"})


@socketIo.on("chat_group")
def chat_group(data):
    try:
        print("_____CHAT_GROUP_____" + str(data))
        PATH_IMAGE = "/var/www/samnote-build/image"
        room = data["room"]
        message = data["data"]
        newChat = ChatGroupModel(
            idGroup=room,
            sendAt=datetime.now(),
            idSend=message["idSend"],
            type=message["type"],
        )
        group = Groups.query.filter(Groups.idGroup == room).first()
        if group != None:
            group.last_time_chat = datetime.now()
            db.session.add(group)
            db.session.commit()
        newChat.listIdUserReaded = message[
            "idSend"
        ]  # user dau tien doc no chinh la user tao ra no
        userFind = Users.query.filter(Users.id == message["idSend"]).first()
        if userFind == None:
            print("_____USERFINDER_____ERROR___")
        if (
            message["type"] == "image"
            or message["type"] == "icon-image"
            or message["type"] == "muti-image"
        ):
            # print("________TYPE:_____" + str(message["type"]))
            # print("____IMAGE_BASE64___" + str(message["metaData"]))
            link_image = make_url_image_base64(
                message["idSend"],
                PATH_IMAGE,
                base64ToByte(message["metaData"]),
                "chat_group",
            )
            newChat.image = link_image
        elif newChat.type == "gif":
            newChat.gif = message["metaData"]
        else:
            newChat.text = message["content"]
        db.session.add(newChat)
        db.session.commit()
        sendAt = newChat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
        result = {
            "idGroup": newChat.idGroup,
            "idMes": newChat.idMes,
            "text": newChat.text,
            "image": newChat.image,
            "gif": newChat.gif,
            "type": newChat.type,
            "idSend": newChat.idSend,
            "sendAt": sendAt,
            "avatarLink": userFind.linkAvatar,
            "userName": userFind.user_name,
        }
        # print("______KETQUA________" + str(result))
        emit("chat_group", {"data": result}, room=room)
    except Exception as e:
        # Log the error message
        print("Exception :____", str(e))
        emit("send_message", {"message": "Error____" + str(e)})


# chat 1vs1


@socketIo.on("join_room")
def handle_join_room(data):
    try:
        room = data["room"]
        join_room(room)
        # print(" ")
        # Truy vấn tin nhắn từ cơ sở dữ liệu và gửi chúng đến người dùng
        messages = Chat1vs1.query.filter(Chat1vs1.room == room).all()
        for message in messages:
            if message.type == "text":
                emit(
                    "message",
                    {
                        "sender": message.idSend,
                        "content": message.text,
                        "type": message.type,
                    },
                )
            elif message.type in ["image", "icon-image"]:
                emit(
                    "message",
                    {
                        "sender": message.idSend,
                        "content": message.img,
                        "type": message.type,
                    },
                )
            elif message.type == "gif":
                emit(
                    "message",
                    {
                        "sender": message.idSend,
                        "content": message.gif,
                        "type": message.type,
                    },
                )

        emit("join_room", {"message": "Join Successful"}, room=room)
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        emit("send_message", {"message": "Error"})


# @socketIo.on("private message", ({ content, to }) => {
#   socket.to(to).emit("private message", {
#     content,
#     from: socket.id,
#   });
# });

# join_room_unknown


# @socketIo.on("join_room")
# def handle_join_room(data):
#     try:
#         room = data["room"]
#         join_room(room)
#         print(" ")
#         # Truy vấn tin nhắn từ cơ sở dữ liệu và gửi chúng đến người dùng
#         messages = Chat1vs1.query.filter(Chat1vs1.room == room).all()
#         for message in messages:
#             if message.type == "text":
#                 emit(
#                     "message",
#                     {
#                         "sender": message.idSend,
#                         "content": message.text,
#                         "type": message.type,
#                     },
#                 )
#             else:
#                 emit(
#                     "message",
#                     {
#                         "sender": message.idSend,
#                         "content": message.img,
#                         "type": message.type,
#                     },
#                 )

#         emit("join_room", {"message": "Join Successful"}, room=room)
#     except Exception as e:
#         # Log the error message
#         print("SQL Error:", str(e))
#         emit("send_message", {"message": "Error"})


@socketIo.on("send_message")
def handle_send_message(data):
    try:
        PATH_IMAGE = "/var/www/samnote-build/image"
        # print("_____socket_line137______")
        room = data["room"]
        # print("_____socket_line138______")
        message = data["data"]
        # print("_____socket_line139______", message, data)
        isString_idSend = isinstance(message["idSend"], str)
        isString_idReceive = isinstance(message["idReceive"], str)
        if isString_idSend == False:
            idSend = message["idSend"]
        else:
            idSend = int(message["idSend"])
        if isString_idReceive == False:
            idReceive = message["idReceive"]
        else:
            idReceive = int(message["idReceive"])
        user1 = Relationship.query.filter(
            Relationship.idSend == idSend,
            Relationship.idReceive == idReceive,
        ).first()
        user2 = Relationship.query.filter(
            Relationship.idReceive == int(message["idSend"]),
            Relationship.idSend == int(message["idReceive"]),
        ).first()
        print("_______user2____" + str(user2) + "____user1____" + str(user1))
        print(
            "______idSend__"
            + str(message["idSend"])
            + "__idReceive___"
            + message["idReceive"]
        )
        if user1 == None or user2 == None:
            emit(
                "send_message",
                {
                    "message": "Error __Relationship cant find idsend_____"
                    + str(message["idSend"])
                    + "cant find idRecive__"
                    + str(message["idReceive"])
                },
            )

        if user1.relation == 1 and user2.relation == 1:
            newChat = Chat1vs1(
                sendAt=datetime.now(),
                idSend=message["idSend"],
                idReceive=message["idReceive"],
                room=room,
                type=message["type"],
            )
            if newChat.type in ["image", "icon-image", "muti-image"]:
                if message["data"] != None:
                    link_image = make_url_image_base64(
                        message["idSend"],
                        PATH_IMAGE,
                        base64ToByte(message["data"]),
                        "chat_group",
                    )
                    newChat.linkImage = link_image
            if newChat.type == "gif":
                newChat.gif = message["data"]
            newChat.text = message["content"]
            print("_________NEWCHAT_____" + str(newChat))
            db.session.add(newChat)
            db.session.commit()

            chat = (
                Chat1vs1.query.filter(
                    Chat1vs1.idSend == message["idSend"],
                    Chat1vs1.idReceive == message["idReceive"],
                    Chat1vs1.room == str(room),
                )
                .order_by(Chat1vs1.sendAt.desc())
                .first()
            )
            if chat.state == "not seen":
                IsSeen = 0
            else:
                IsSeen = 1
            Image = ""
            if chat.type == "image":
                Image = chat.linkImage
            if chat.type in ["icon-image", "muti-image"]:
                Image = chat.linkImage
            Gif = ""
            if chat.type == "gif":
                Gif = chat.gif
            result = {
                "MessageID": chat.id,
                "SenderID": chat.idSend,
                "ReceivedID": chat.idReceive,
                "Content": chat.text,
                "MessageTime": chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                "IsSeen": IsSeen,
                "Image": Image,
                "Gif": Gif,
                "Type": chat.type,
            }
            print(result)
            # emit("send_message", {"data":message}, room=room)
            emit("send_message", {"data": result}, room=room)

        else:
            print("you are banned from chatting")
            emit("send_message", f"you are banned from chatting", room=room)
        # ,state=message["state"]
    except Exception as e:
        # Log the error message
        print("SQL Error:", str(e))
        emit("send_message", {"message": "Error _______" + str(e)})
