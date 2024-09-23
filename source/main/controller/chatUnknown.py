from source import app

from source.main.function.handleChatUnknowns import *

app.add_url_rule(
    "/chat-unknown",
    methods=["GET", "POST", "PATCH", "DELETE"],
    view_func=handleChatUnknowns,
)

app.add_url_rule(
    "/message/chat-unknown/<string:id>",
    methods=["GET", "POST"],
    view_func=handleMessages,
)

app.add_url_rule(
    "/message/chat-unknown-image2/<string:id>",
    methods=["GET", "POST"],
    view_func=handleMessages_sendfile,
)

app.add_url_rule(
    "/message/chat-unknown-id",
    methods=["POST"],
    view_func=handleMessagesRecevie,
)
app.add_url_rule(
    "/message/block_chat_unknown",
    methods=["POST"],
    view_func=block_chat_unknow,
)
app.add_url_rule(
    "/message/disable_unknow_account/<string:idUser>",
    methods=["POST"],
    view_func=DisableUnknownAccount,
)

app.add_url_rule(
    "/message/unknown/<string:id>", methods=["POST"], view_func=handleMessages
)
app.add_url_rule(
    "/message/list_user_unknown/<string:id>",
    methods=["GET"],
    view_func=handleListUser,
)

app.add_url_rule(
    "/message/list_message_chat1vs1/<string:id>/<string:idReceived>",
    methods=["GET"],
    view_func=handleGetMesChat1vs1,
)
app.add_url_rule(
    "/message/list_all_message/<string:idUser>",
    methods=["GET"],
    view_func=get_all_message,
)
app.add_url_rule(
    "/message/list_user_chat1vs1/<string:id>",
    methods=["GET"],
    view_func=handleListUserChat1vs1,
)
app.add_url_rule(
    "/message/search_unknown_by_text/<string:id>/<string:text>",
    methods=["GET"],
    view_func=handleSearchText,
)
app.add_url_rule(
    "/message/delete_chat_unknown",
    methods=["POST"],
    view_func=handleDeleteChatUnknown,
)

app.add_url_rule(
    "/get-image-chat/<string:id_user>/<string:file_name>",
    methods=["GET"],
    view_func=view_image_chat,
)

app.add_url_rule("/unknown/allphoto", methods=["POST"], view_func=getAllPhotoChatUnknow)
