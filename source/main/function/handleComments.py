from source import db
from flask import request, make_response, jsonify
from source.main.model.favorite import Favorites
from source.main.model.notes import Notes
from source.main.model.users import Users
from source.main.model.comments import Comments
from source.main.model import *
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.sql import label
from flask_jwt_extended import jwt_required
from sqlalchemy import text, and_
import jwt

def postCommentnotes(idNote):
    if (request.method=="POST"):         
            try:
                json = request.json           
                print(json)
                print(json['sendAt'])
                sentAt_time = datetime.strptime( json['sendAt'], '%Y-%m-%dT%H:%M:%S.%f%z')
                print(json['content'])
                comments=Comments(sendAt=sentAt_time,idNote=json['idNote'],text=json['content'],parent_id=json['parent_id'])
                print("loi o ghep su kien")                
                if (json['idUser']):
                    comments.idUser=json['idUser']
                # print(comments)
                db.session.add(comments)
                db.session.commit()
                comments_users = {}
                comments_users["id"] = comments.id
                comments_users["idNote"] = comments.idNote
                comments_users["idUser"] = comments.idUser
                comments_users["parent_id"] = comments.parent_id
                comments_users['content']=comments.text
                comments_users['sendAt'] = str(comments.sendAt)
                return {'status': 200, 'message': comments_users}
            except Exception as e :
                print(e)
                return make_response(jsonify({'status': 300, 'message': str(e)}), 300)
            
def getCommentnotes(idNote):
    if (request.method == 'GET'):
        try:   
            current_user_id = request.args.get("current_user_id")      
            data = []
            comments = Comments.query.filter(Comments.idNote == idNote).order_by(Comments.idNote.desc()).all()
            for comment in comments:
                if comment.parent_id == 0:

                    # GET LIKE, DISLIKE, CURRENT USER FAVORITE STATUS
                    like = Favorites.query.filter(Favorites.idComment == comment.id, Favorites.type.like("like")).all()
                    if like:
                        like_count = len(like)
                    else:
                        like_count = 0

                    dislike = Favorites.query.filter(Favorites.idComment == comment.id, Favorites.type.like("dislike")).all()
                    if dislike:
                        dislike_count = len(dislike)
                    else:
                        dislike_count = 0

                    favoriteType = None
                    if current_user_id:
                        isFavorite = Favorites.query.filter(Favorites.idUser == current_user_id, Favorites.idComment == comment.id).first() 
                        if isFavorite:
                            favoriteType = isFavorite.type
                        else:
                            favoriteType = None

                    # GET ALL COMMENT AND REPLY COMMENT
                    comment_parse = {}
                    user = Users.query.filter(Users.id == comment.idUser).first()
                    comment_parse["id"] = comment.id
                    comment_parse["idUser"] = user.id
                    comment_parse["idNote"] = comment.idNote
                    comment_parse["parent_id"] = comment.parent_id
                    comment_parse["avt"] = user.linkAvatar
                    comment_parse["user_name"] = user.user_name
                    comment_parse['content'] = comment.text
                    comment_parse['sendAt'] = str(comment.sendAt)
                    comment_parse['like'] = like_count
                    comment_parse['dislike'] = dislike_count
                    comment_parse['favoriteType'] = favoriteType if favoriteType else None
                    reply_comments = Comments.query.filter(Comments.parent_id == comment.id).order_by(Comments.id.desc())
                    if reply_comments:
                        list_reply = []
                        for reply in reply_comments:
                            reply_user = Users.query.filter(Users.id == reply.idUser).first()
                            reply_data = {
                                    "id": reply.id,
                                    "idUser": reply.id,
                                    "idNote": reply.idNote,
                                    "parent_id": reply.parent_id,
                                    "avt": reply_user.linkAvatar,
                                    "user_name": reply_user.user_name,
                                    "content": reply.text,
                                    "sendAt": reply.sendAt,
                                }
                            list_reply.append(reply_data)
                        comment_parse['reply_comments'] = list_reply
                    else:
                        comment_parse['reply_comments'] = None
                    data.append(comment_parse)
                else:
                    print(comment)
            return {'status': 200, 'data': data}
        except Exception as e :
                print(e)
                return make_response(jsonify({'status': 300, 'message': str(e)}), 300)