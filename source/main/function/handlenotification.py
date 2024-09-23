from source import db, app
from flask import request, make_response, jsonify
from source.main.model.chat1vs1 import Chat1vs1
from source.main.model.relationship import Relationship
from source.main.model.token_device import Token_device
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label, text
from source.main.function.notification import *
import time
from postmarker.core import PostmarkClient
from source.main.model.users import Users

push_notifications = IOSPushNotifications(
    privatekey_filepath="/etc/ssl/notification/private_key.pem",
    certificate_filepath="/etc/ssl/notification/Apple-Development-Nguyen-Xuan-Phuc-RMKQQY53K6.pem",
    sandbox=True,
)
client = PostmarkClient(server_token=app.config["POSTMARK_API"])
androidNotificator = AndroidPushNotifications(
    api_key="AIzaSyBp_s0l81pK2DQ7ZG3br4MrERvqR9o_d9U"
)


def IOSpush_notifications():
    if request.method == "POST":

        try:
            # Lấy dữ liệu từ yêu cầu POST
            data = request.get_json()

            # Kiểm tra xem dữ liệu có chứa message và token_device không
            if "message" not in data or "token_device" not in data:
                return jsonify({"status": "failed", "response": "missing_data"})

            # Gửi thông báo đẩy
            while True:
                result = push_notifications.send_push_notification(
                    message=data["message"], token_device=data["token_device"], badge=1
                )
                # time.sleep(1)
                return jsonify(result)
        except Exception as e:
            return jsonify(
                {
                    "status": "failed",
                    "response": "push_notification_error",
                    "description": str(e),
                }
            )
    if request.method == "GET":
        try:
            result = push_notifications.send_push_notification(
                message="hello", token_device="12346", badge=1
            )
            data = []
            message = {}
            message["message"] = "hello"
            message["title"] = "notice"
            data.append(result)
            return {"state": 200, "data": data}
        except Exception as e:
            return jsonify(
                {
                    "status": "failed",
                    "response": "push_notification_error",
                    "description": str(e),
                }
            )


def sendemail(gmail):
    response = client.emails.send(
        From="admin@samnotes.online",  # Địa chỉ email gửi
        To=gmail,
        Subject="Notification email",
        TextBody="you have message!!!",
    )
    return "check your email"


def pushemail(id):
    # if(request.method=="POST"):
    chat = db.session.execute(
        text(
            "SELECT * FROM users INNER JOIN chat1vs1 ON users.id = chat1vs1.idReceive WHERE chat1vs1.id = :id"
        ),
        {"id": id},
    )
    for row in chat:
        gmail = row.gmail
        state = row.state
        if state == "seen":
            return "you seen message"
        else:
            sendemail(gmail)
            return "check your gmail"


def Androidpush_notifications():
    if request.method == "POST":
        try:
            your_message = "Hi, I am sending a message!"
            your_token_device = "klaklsjdbflkasjdbflksadjb"
            result = androidNotificator.send_push_notification(
                message=your_message, token_device=your_token_device
            )
            return jsonify(result)
        except Exception as e:
            return jsonify(
                {
                    "status": "failed",
                    "response": "push_notification_error",
                    "description": str(e),
                }
            )


def posttoken(id):
    if request.method == "POST":
        try:
            json = request.get_json()
            data = Token_device(
                idUser=id, device=json["name_device"], tokenid=json["token"]
            )
            db.session.add(data)
            db.session.commit()
            return {"status": 200, "message": "success"}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    if request.method == "GET":
        try:
            user = db.session.execute(
                text("SELECT * FROM token_device WHERE token_device.idUser = :id"),
                {"id": id},
            )
            data = []

            for row in user:
                devicetoken = {
                    "id": row.id,
                    "idUser": row.idUser,
                    "device": row.device,
                    "token": row.tokenid,
                }
                data.append(devicetoken)
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


# def checkmessage(id):
#     chat = db.session.execute(text(
#             'SELECT * FROM users INNER JOIN chat1vs1 ON users.id = chat1vs1.idReceive WHERE chat1vs1.id = :id'
#         ), {'id': id})
#     if (datetime.now() - chat.sendAt) >= timedelta(minutes=15):
#         sendemail()
#         return ""
