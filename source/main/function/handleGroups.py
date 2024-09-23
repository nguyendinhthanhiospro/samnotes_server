from source import db
from source.main.model.groups import Groups
from source.main.model.members import Members
from source.main.model.ChatGroupModel import ChatGroupModel
from source.main.model.users import Users
from source.main.function.middleware import *

from source.main.model.groups import Groups
from source.main.model.images import Images

from flask_jwt_extended import jwt_required
from flask import request, make_response, jsonify
from sqlalchemy import text, and_
import jwt

from source.socket import base64ToByte, byteToString


def handleNotesGroup(idNote):
    pass


def upload_image_for_avatar(idUser):
    try:
        PATH_IMAGE = "/var/www/samnote-build/image"
        fileImage = request.files.get("image")
        imgLink = make_url_apache_image(idUser, PATH_IMAGE, fileImage, "note")
        new_image = Images(idNote=0, link=imgLink, idUserUpload=idUser)
        db.session.add(new_image)
        db.session.commit()
        return make_response(
            jsonify(
                {
                    "status": 200,
                    "message": "upload image to server samnotes okie done",
                    "imagelink": imgLink,
                }
            ),
            200,
        )
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 500, "message": "Exception " + str(e)}),
            400,
        )


def list_image_user_upload(idUser):
    try:
        listImage = Images.query.filter_by(idUserUpload=idUser).all()
        listReturn = []
        for itemImage in listImage:
            dataItem = {}
            dataItem["link"] = itemImage.link
            dataItem["userUpload"] = itemImage.idUserUpload
            listReturn.append(dataItem)
        return make_response(
            jsonify(
                {
                    "status": 200,
                    "message": "list image user upload",
                    "imagelink": listReturn,
                }
            ),
            200,
        )
    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 500, "message": "Exception " + str(e)}),
            400,
        )


def createGroup(owner):
    if request.method == "POST":
        json_data = request.json
        try:
            # Kiểm tra xem tên nhóm đã tồn tại chưa
            group_filter = Groups.query.filter_by(name=json_data["name"]).first()
            if group_filter:
                return make_response(
                    jsonify({"status": 402, "message": "Group name already exists"}),
                    402,
                )
            else:
                # Tạo một nhóm mới
                new_group = Groups(
                    name=json_data["name"],
                    idOwner=owner,
                    describe=json_data["describe"],
                    r=json_data["r"],
                    g=json_data["g"],
                    b=json_data["b"],
                    a=json_data["a"],
                )
                if json_data["linkAvatar"] != None:
                    new_group.linkAvatar = json_data["linkAvatar"]
                db.session.add(new_group)
                db.session.commit()

                # print(json_data["members"])
                # Thêm các thành viên vào nhóm mới
                checkOwerAdded = False
                for member in json_data["members"]:
                    if int(member["id"]) == int(owner):
                        checkOwerAdded = True
                    userFind = Users.query.filter(Users.id == member["id"]).first()
                    if userFind != None:
                        new_member = Members(
                            idGroup=new_group.idGroup,
                            idUser=member["id"],
                            role=member["role"],
                            gmail=userFind.gmail,
                            idUserAddMe=owner,
                        )
                        db.session.add(new_member)
                        db.session.commit()
                if (
                    checkOwerAdded == False
                ):  # neu khong add owner vao list member trong database thi server se tu add
                    new_member = Members(
                        idGroup=new_group.idGroup,
                        idUser=str(owner),
                        role="Owner",
                        idUserAddMe=owner,
                    )
                    new_group.idMemberOf_Owner = new_member.idMember
                    db.session.add(new_group)
                    db.session.add(new_member)
                    db.session.commit()
                # Lấy số lượng thành viên trong nhóm mới
                num_members = Members.query.filter_by(idGroup=new_group.idGroup).count()

                group_info = {
                    "idGroup": new_group.idGroup,
                    "linkAvatar": new_group.linkAvatar,
                    "numberMembers": num_members,
                    "name": new_group.name,
                    # "createdAt": json_data["createAt"],
                    "idOwner": new_group.idOwner,
                    "description": new_group.describe,
                    "r": json_data["r"],
                    "g": json_data["g"],
                    "b": json_data["b"],
                    "a": json_data["a"],
                    "gmail": json_data["members"][0]["gmail"],
                }

                return {
                    "status": 200,
                    "message": "Group created successfully",
                    "group": group_info,
                }
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Exception " + str(e)}),
                400,
            )
    else:
        return {"status": 500, "message": "Invalid request method"}


def updateGroup(idGr):
    if request.method == "PATCH":
        json_data = request.json
        try:
            group = Groups.query.filter(Groups.idGroup == idGr).first()
            if group is None:
                return make_response(
                    jsonify({"status": 400, "message": "Group is not exist"}),
                    400,
                )
            if "groupName" in json_data:
                groupName = json_data["groupName"]
                # Kiểm tra xem tên nhóm đã tồn tại chưa
                group_filter = Groups.query.filter_by(name=groupName).first()
                # print(group_filter)
                if group_filter:
                    return make_response(
                        jsonify(
                            {"status": 400, "message": "Group name already exists"}
                        ),
                        400,
                    )
                else:
                    group.name = groupName
                    db.session.commit()
                    return make_response(
                        jsonify(
                            {
                                "status": 200,
                                "message": "Group name changed successfully",
                            }
                        ),
                        200,
                    )
            if "linkAvatar" in json_data:
                PATH_IMAGE = "/var/www/samnote-build/image"

                link_image = make_url_image_base64(
                    group.idOwner,
                    PATH_IMAGE,
                    base64ToByte(json_data["linkAvatar"]),
                    "chat_group",
                )
                group.linkAvatar = link_image
                db.session.commit()
                return make_response(
                    jsonify(
                        {"status": 200, "message": "Group avatar changed successfully"}
                    ),
                    200,
                )
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request failed. Please try again"}),
                400,
            )
    else:
        return {"status": 400, "message": "Invalid request method"}


def addMembers(idGr):
    try:
        json = request.json
        if json["idUserAddMe"] == None:
            return {
                "status": 202,
                "message": "Please add idUserAddMe In Body Is Person Add User",
            }
        listUserNotFound = []
        listUserAdded = []
        for id in json["idMembers"]:
            print("____ID__dang duoc add__" + str(id))
            user = Users.query.filter(Users.id == id).first()
            member = Members.query.filter(
                Members.idUser == id, Members.idGroup == idGr
            ).all()
            if member != None:
                listUserNotFound.append(id)
                print("___Mem Da Duoc Add Roi___")
                continue
            if user:
                member = Members(
                    idGroup=idGr,
                    idUser=id,
                    role="Member",
                    gmail=user.gmail,
                    idUserAddMe=json["idUserAddMe"],
                )
                print("_______idUserAddMe___________ID_____" + str(json["idUserAddMe"]))
                listUserAdded.append(id)
                db.session.add(member)
            else:
                listUserNotFound.append(id)
                print(f"user {id} is not found")

        db.session.commit()
        print("_____len(listUserNotFound) ____" + str(len(listUserNotFound)))
        print("_____len(idMembers) ____" + str(len(json["idMembers"])))
        if len(listUserNotFound) == 0:
            return {"status": 200, "message": "Member was added successfully"}
        else:
            dataReturnCount = ""
            for item in listUserNotFound:
                dataReturnCount = dataReturnCount + "-" + str(item)
            dataAdded = ""
            for item in listUserAdded:
                dataAdded = dataAdded + "-" + str(item)
            return {
                "status": 205,
                "message": "Add okie But Cant find Userid For add id: "
                + dataReturnCount
                + " list id add okie "
                + dataAdded,
                "data": "List user added " + dataAdded,
            }
    except Exception as e:
        print(e)
        return make_response(
            jsonify(
                {"status": 400, "message": "Request fail. Please try again___" + str(e)}
            ),
            400,
        )


def quitMembers(idMem):
    try:
        if idMem is None:
            return make_response(
                jsonify({"message": "Missing idMem", "status": 201}), 201
            )
        member = Members.query.filter(Members.idMember == idMem).first()
        if member:
            chats = ChatGroupModel.query.filter(
                ChatGroupModel.idSend == member.idUser,
                ChatGroupModel.idGroup == member.idGroup,
            ).all()
            if chats:
                for chat in chats:
                    db.session.delete(chat)
            param = f"DELETE FROM members WHERE idMember = {idMem}"
            db.session.execute(text(param))
            db.session.execute(text("SET FOREIGN_KEY_CHECKS=0"))
            db.session.commit()
            return jsonify({"message": "user quitted successfully", "status": 200})
        else:
            return jsonify(
                {
                    "message": "Member not found, Please input idMember, not idUser !",
                    "status": 204,
                }
            )

    except Exception as e:
        return make_response(jsonify({"message": f"Error: {e}", "status": 500}), 500)


def getAllGroup(idMem):
    if request.method == "GET":
        try:

            groups_have_mem = db.session.execute(
                text(
                    "Select * from members as m inner join `groups` as g on m.idGroup=g.idGroup where m.idUser={} ORDER BY g.last_time_chat DESC".format(
                        idMem
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

                dataReturn.append(group_if)
    
            if dem_so_group_member_ben_trong == 0:
                return {
                    "status": 204,
                    "data": [],
                    "message": "You must input True idMember: "
                    + str(idMem)
                    + " because cant find idMember in all group",
                }
            return {"status": 200, "data": dataReturn, "message": "Done okie"}
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


def getGroup(idGroup):
    if request.method == "GET":
        try:
            group = Groups.query.filter(Groups.idGroup == idGroup).first()
            group_if = {}
            group_if["idGroup"] = group.idGroup
            group_mems_avt = []
            group_if["members"] = []
            tv = db.session.execute(
                text(
                    "select *  from members as m inner join users as u on m.idUser=u.id where m.idGroup={}".format(
                        group.idGroup
                    )
                )
            )

            for row in tv:
                print("_______tv___" + str(row))
                member_if = {}
                member_if["avt"] = row.linkAvatar
                member_if["name"] = row.name
                member_if["idUser"] = row.id
                member_if["idMember"] = row.idMember
                member_if["role"] = row.role
                member_if["user_name"] = row.user_name
                group_if["members"].append(member_if)
                group_mems_avt.append(row.linkAvatar)
            PATH_IMAGE = "/var/www/samnote-build/image"
            group_if["avt"] = {"avt": group.linkAvatar, "mems": group_mems_avt}
            group_if["name"] = group.name
            group_if["createAt"] = str(group.createAt)
            group_if["idOwner"] = group.idOwner
            group_if["describe"] = group.describe
            group_if["r"] = group.r
            group_if["g"] = group.g
            group_if["b"] = group.b
            group_if["a"] = group.a
            return {"status": 200, "data": group_if}
        except Exception as e:
            print(e)
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": "____Request fail. Please try again____" + str(e),
                    }
                ),
                400,
            )
    else:
        return {"status": 400, "message": "Invalid request method"}


def getAllPhotoGroup(idgroup):
    print("id cua user phan getAllPhotoGroup " + str(idgroup))
    page = request.args.get("page", default=1, type=int)
    if request.method == "GET":
        try:
            # Separate page
            limit = 20
            toan_bo_tin_nhan_1room = ChatGroupModel.query.filter(
                ChatGroupModel.idGroup == idgroup, ChatGroupModel.image != None
            ).all()
            tongtinnhan = len(toan_bo_tin_nhan_1room)
            if tongtinnhan == 0:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "message": "No image chat in idgroup = "
                            + str(idgroup)
                            + " in database",
                            "data": [],
                        }
                    ),
                    300,
                )
            print("____TONG_SO_TIN_NHAN_____" + str(tongtinnhan))

            tongsopage = tongtinnhan / limit
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
            print("____OFFSET___" + str(offset))
            chat_room = (
                ChatGroupModel.query.filter(
                    ChatGroupModel.idGroup == idgroup, ChatGroupModel.image != None
                )
                .order_by(ChatGroupModel.sendAt.asc())
                .offset(offset)
                .limit(limit)
                .all()
            )
            data = []
            for chat in chat_room:
                chat_parse = {}
                chat_parse["image"] = ""
                chat_parse["id"] = chat.idMes
                chat_parse["type"] = chat.type
                chat_parse["gif"] = ""
                print("_________chat.type___________", chat.type)

                chat_parse["idSend"] = chat.idSend
                user = Users.query.filter(Users.id == chat.idSend).first()
                if user:
                    chat_parse["avt"] = user.linkAvatar
                    chat_parse["name"] = user.name
                else:
                    continue
                print("______chat:___" + str(chat))
                if (
                    chat.type == "image"
                    or chat.type == "muti-image"
                    or chat.type == "icon-image"
                ):
                    image = chat.image
                    chat_parse["image"] = image
                elif chat.type == "gif":
                    gif = chat.gif
                    chat_parse["gif"] = gif
                else:
                    text = chat.text
                    print("____text chat____" + str(text))
                    chat_parse["content"] = text if text else ""
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)
                print("______RETURN___200____" + str(toan_bo_tin_nhan_1room))
            return {
                "status": 200,
                "data": data,
                "tong_so_trang": tongsopage,
                "tongtinnhan": tongtinnhan,
            }
        except Exception as e:
            print(e)
            return {"status": 500, "data": "____Error___" + str(e)}


def getMessages(idGroup):
    print("id cua Group phan getMessages " + str(idGroup))
    page = request.args.get("page", default=1, type=int)
    if request.method == "GET":
        try:
            # Separate page
            limit = 50
            toan_bo_tin_nhan_1room = ChatGroupModel.query.filter(
                ChatGroupModel.idGroup == idGroup
            ).all()
            tongsopage = len(toan_bo_tin_nhan_1room) / limit
            if tongsopage == 0:
                return {
                    "status": 202,
                    "data": [],
                    "message": "Database can not found Number "
                    + str(tongsopage)
                    + " chat of idGroup: "
                    + str(idGroup),
                }
            offset = 0
            if tongsopage > 0 and tongsopage < 1:
                offset = (1 - int(page)) * limit
            if tongsopage >= 1:
                truPage = tongsopage - int(page)
                if truPage > -1 and truPage < 0:
                    truPage = 0
                offset = truPage * limit
            if offset < 0:
                return {
                    "status": 203,
                    "data": [],
                    "message": "page not found " + str(page),
                }
            chats = (
                ChatGroupModel.query.filter(ChatGroupModel.idGroup == idGroup)
                .order_by(ChatGroupModel.sendAt.asc())
                .offset(offset)
                .limit(limit)
                .all()
            )
            data = []
            for chat in chats:
                chat_parse = {}
                chat_parse["image"] = ""
                chat_parse["id"] = chat.idMes
                chat_parse["type"] = chat.type
                chat_parse["gif"] = ""
                listUserReaded = []
                listIdUserReaded = chat.listIdUserReaded
                if listIdUserReaded != None:
                    if len(listIdUserReaded) > 0:
                        listID = listIdUserReaded.split("#")
                        for itemID in listID:
                            itemUser = {}
                            userReaded = Users.query.filter(Users.id == itemID).first()
                            if userReaded != None:
                                itemUser["avatar"] = userReaded.linkAvatar
                                itemUser["idUser"] = itemID
                                itemUser["username"] = userReaded.user_name
                                listUserReaded.append(itemUser)
                chat_parse["listUserReaded"] = listUserReaded
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
                    image = chat.image
                    chat_parse["image"] = image
                elif chat.type == "gif":
                    gif = chat.gif
                    chat_parse["gif"] = gif
                else:
                    text = chat.text
                    chat_parse["content"] = text if text else ""
                chat_parse["sendAt"] = chat.sendAt.strftime("%a, %d %b %Y %H:%M:%S GMT")
                data.append(chat_parse)
            return {
                "status": 200,
                "data": data,
                "tongsopage": tongsopage,
                "soItem": len(data),
            }
        except Exception as e:
            print(e)
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": "Request fail. Please try again_______" + str(e),
                    }
                ),
                400,
            )
    else:
        return {"status": 400, "message": "Invalid request method"}


def getImages(id):
    if request.method == "GET":
        try:
            images = db.session.execute(
                text(
                    f'select * from chats as c inner join users as u on c.idSend=u.id  where idGroup={id} and (type="image" or type="muti-image")'
                )
            )
            images_by_date = {}
            show = []
            idx = 1
            for image in images:
                # Lấy ngày từ trường 'created_at' của tin nhắn
                date = image.sendAt.strftime("%d-%m-%y")

                # Kiểm tra xem ngày đã được lưu trong dict chưa
                if date not in images_by_date:
                    # Nếu chưa, tạo một dict mới cho ngày này và lưu trữ các hình ảnh vào dict
                    images_by_date[date] = {"date": date, "images": []}

                # Lưu trữ thông tin của hình ảnh trong dict của ngày tương ứng
                if image.type == "image":
                    image_info = {
                        "id": idx,
                        "url": image.image,
                        "idSend": image.idSend,
                        "name": image.name,
                        "type": "image",
                        "sendAt": str(image.sendAt),
                    }
                    images_by_date[date]["images"].append(image_info)
                    if len(show) <= 8:
                        show.append(image_info)
                    idx += 1
                else:
                    arr_image = image.image.split(";")
                    for i in arr_image:
                        image_info = {
                            "id": idx,
                            "url": i,
                            "idSend": image.idSend,
                            "name": image.name,
                            "type": "image",
                            "sendAt": str(image.sendAt),
                        }
                        idx += 1
                        if len(show) <= 8:
                            show.append(image_info)
                        images_by_date[date]["images"].append(image_info)

            image_list = [images_by_date[date] for date in images_by_date]
            return {"status": 200, "images": image_list, "show": show}
        except Exception as e:
            print(e)
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    else:
        return {"status": 400, "message": "Invalid request method"}


def deleteMessages(idGroup, id, idMes):
    if request.method == "PATCH":
        try:
            group = ChatGroupModel.query.filter(
                ChatGroupModel.idGroup == idGroup,
                ChatGroupModel.idSend == id,
                ChatGroupModel.idMes == idMes,
            ).first()

            if not group:
                return {"status": 404, "message": "group not found"}

            data = request.json
            message = data.get("text", "message has been recovered")
            group.text = message
            db.session.add(group)
            db.session.commit()
            return jsonify({"status": 200, "message": "message has been recovered"})
        # except Exception as e:
        #     print(e)
        #     return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
        except Exception as e:
            # Log the error message
            print("Error:", str(e))
            return {"status": 500, "message": str(e)}
    else:
        return {"status": 400, "message": "Invalid request method"}


def history_search_user(idUser):
    try:
        listAll_Member_User_add = Members.query.filter(
            Members.idUserAddMe == idUser
        ).all()
        result_data = []
        for itemMember in listAll_Member_User_add:
            userFind = Users.query.filter(Users.id == itemMember.idUser).first()
            result_data.append(
                {
                    "idUser": userFind.id,
                    "userName": userFind.user_name,
                    "linkAvatar": userFind.linkAvatar,
                    "email": userFind.gmail,
                }
            )
        return jsonify({"status": 200, "data": result_data})
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": "Exception_____" + str(e)}


def searchUserByWord():
    try:
        json = request.json
        start_name = json["start_name"]
        users = Users.query.filter(Users.user_name.ilike(f"{start_name}%")).all()
        if len(users) == 0:
            return jsonify({"status": 400, "message": "no user start name like that"})

        result_data = []
        for user in users:
            result_data.append(
                {
                    "idUser": user.id,
                    "userName": user.user_name,
                    "linkAvatar": user.linkAvatar,
                    "email": user.gmail,
                }
            )
        return jsonify({"status": 200, "data": result_data})
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


def getListMessageUser(idUser):
    try:
        all_groups_of_member = Members.query.filter(Members.idUser == idUser).all()
        list_message = []
        for itemMember in all_groups_of_member:
            message_group_first = (
                ChatGroupModel.query.filter(
                    ChatGroupModel.idGroup == itemMember.idGroup
                )
                .order_by(ChatGroupModel.idMes.desc())
                .first()
            )
            # print(message)
            groupInfo = Groups.query.filter(
                Groups.idGroup == itemMember.idGroup
            ).first()
            groupName = "nameGroup Default"
            linkAvatar_Group = "https://vieclam123.vn/ckfinder/userfiles/images/images/phan-biet-group-va-team.jpeg"
            if groupInfo != None:
                print("_____" + str(itemMember.idGroup) + "____" + str(groupInfo.name))
                if type(groupInfo.linkAvatar) != type(None):
                    if groupInfo.linkAvatar != None:
                        linkAvatar_Group = groupInfo.linkAvatar
                        groupName = groupInfo.name

            members = Members.query.filter(Members.idGroup == itemMember.idGroup).all()
            admin = Members.query.filter(
                Members.idGroup == itemMember.idGroup, Members.role.like("admin")
            ).first()
            if admin:
                idAdmin = admin.idUser
            else:
                idAdmin = None
            if message_group_first:
                listMem = []
                for itemMem in members:
                    userMem = Users.query.filter(Users.id == itemMem.idUser).first()
                    itemJson = {}
                    itemJson["idMember"] = itemMem.idMember
                    itemJson["idGroup"] = itemMem.idGroup
                    itemJson["idUser"] = itemMem.idUser
                    itemJson["gmail"] = itemMem.gmail
                    itemJson["email"] = userMem.gmail
                    itemJson["linkAvatar"] = userMem.linkAvatar
                    itemJson["userName"] = userMem.user_name
                    listMem.append(itemJson)
                content = message_group_first.text
                listUserReaded = []
                if (
                    message_group_first.listIdUserReaded != None
                ):  # hien thi nhung ai da doc tin nhan
                    listIdUserReaded = message_group_first.listIdUserReaded
                    listID = listIdUserReaded.split("#")
                    for itemID in listID:
                        itemUser = {}
                        userReaded = Users.query.filter(Users.id == itemID).first()
                        if userReaded != None:

                            itemUser["avatar"] = userReaded.linkAvatar
                            itemUser["idUser"] = itemID
                            itemUser["username"] = userReaded.user_name
                            listUserReaded.append(itemUser)

                if message_group_first.type == "image":
                    content = "sent an image"
                if message_group_first.type == "gif":
                    content = "sent a gif"
                data = {
                    "idGroup": itemMember.idGroup,
                    "idAdmin": idAdmin,
                    "groupName": groupName,
                    "linkAvatar": linkAvatar_Group,
                    "Nummembers": len(members),
                    "members": listMem,
                    "idMes": message_group_first.idMes,
                    "content": content,
                    "list_user_read": listUserReaded,
                    "image": message_group_first.image,
                    "type": message_group_first.type,
                    "idSend": message_group_first.idSend,
                    "sendAt": message_group_first.sendAt,
                }
                list_message.append(data)

        result = {"data": list_message, "status": 200}
        return result
    except Exception as e:
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}
