from source import app

from source.main.function.handleGroups import *

app.add_url_rule(
    "/group", methods=["GET", "POST", "PATCH", "DELETE"], view_func=handleNotesGroup
)
app.add_url_rule(
    "/group/create/<string:owner>", methods=["POST"], view_func=createGroup
)
app.add_url_rule(
    "/upload_image/<string:idUser>",
    methods=["POST", "GET"],
    view_func=upload_image_for_avatar,
)
app.add_url_rule(
    "/list_image_user_upload/<string:idUser>",
    methods=["POST", "GET"],
    view_func=list_image_user_upload,
)

app.add_url_rule(
    "/group/update/<string:idGr>", methods=["PATCH"], view_func=updateGroup
)
app.add_url_rule("/group/all/<string:idMem>", methods=["GET"], view_func=getAllGroup)
app.add_url_rule("/group/only/<string:idGroup>", methods=["GET"], view_func=getGroup)
app.add_url_rule("/group/add/<string:idGr>", methods=["POST"], view_func=addMembers)
app.add_url_rule(
    "/group/quit/<string:idMem>",
    methods=["delete"],
    view_func=quitMembers,
)

app.add_url_rule(
    "/group/messages/<string:idGroup>", methods=["get"], view_func=getMessages
)
app.add_url_rule(
    "/group/allphoto/<string:idgroup>", methods=["get"], view_func=getAllPhotoGroup
)


app.add_url_rule("/group/images/<string:id>", methods=["get"], view_func=getImages)
app.add_url_rule(
    "/group/delete_messages/<string:idGroup>/<int:id>/<int:idMes>",
    methods=["PATCH"],
    view_func=deleteMessages,
)
app.add_url_rule(
    "/group/search_user_by_word",
    methods=["POST"],
    view_func=searchUserByWord,
)
app.add_url_rule(
    "/group/history_add_member/<string:idUser>",
    methods=["GET"],
    view_func=history_search_user,
)
app.add_url_rule(
    "/group/list_message_user/<string:idUser>",
    methods=["GET"],
    view_func=getListMessageUser,
)
