from source import app

from source.main.function.chat1vs1 import *

app.add_url_rule(
    "/chat/<string:id>", methods=["GET", "POST", "PATCH", "DELETE"], view_func=chat1vs1
)
# relationship  chat
# id User
app.add_url_rule(
    "/chatblock/<string:id>", methods=["GET", "POST", "PATCH"], view_func=blockchat
)
# change state message
# id message
app.add_url_rule(
    "/message/<string:id>", methods=["GET", "POST", "PATCH"], view_func=statemessage
)
app.add_url_rule(
    "/seen_message_group/<int:idMessage>/<int:idUser>",
    methods=["GET", "POST", "PATCH"],
    view_func=statemessage_chatgroup,
)
app.add_url_rule("/message/<string:idMes>", methods=["DELETE"], view_func=deleteMessage)
app.add_url_rule(
    "/send_multiple_image/<string:idMes>",
    methods=["POST"],
    view_func=send_multiple_images_send_message,
)

app.add_url_rule(
    "/chat/search_chat/<string:id>/<string:text>/<int:page>",
    methods=["GET"],
    view_func=handleSearch1Chat1,
)
app.add_url_rule("/chat/allphoto", methods=["POST"], view_func=getAllPhoto1Chat1)
