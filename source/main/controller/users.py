from source import app, mail
from source.main.function.handleUsers import handleUsers
from source.main.function.handleUsers import getAllUser
from source.main.function.handleUsers import checkPasssword2
from source.main.function.handleUsers import createPass2
from source.main.function.handleUsers import get20LastestUser
from source.main.function.createUser import *
from source.main.function.loginUser import *
from source.main.function.loginUser import logout
from source.main.function.handleUsers import getProfile
from source.main.function.loginUser import stateLogin
from source.main.function.handleUsers import changeProfile
from source.main.function.handleUsers import searchUser
from source.main.function.handleUsers import searchnameUser
from source.main.function.handleUsers import *
from flask import jsonify, make_response, request, url_for
from itsdangerous import URLSafeTimedSerializer
from flask_mail import *
from sqlalchemy import or_
from source.main.model.users import Users
from postmarker.core import PostmarkClient
import random
import mysql.connector
from email.message import EmailMessage
import string

config = {
    "user": "sonpro",
    "password": "Ratiendi89",
    "host": "localhost",
    "port": 3306,
    "database": "FutureLove4",
    "auth_plugin": "mysql_native_password",
}

# from source.main.function.resetPassword import forgotPasswork
# from source.main.function.resetPassword import confirmforgotPassword
# from source.main.function.resetPassword import fogot

from passlib.hash import pbkdf2_sha256

client = PostmarkClient(server_token=app.config["POSTMARK_API"])

s = URLSafeTimedSerializer(app.config["SECRET_KEY"])

app.add_url_rule(
    "/user/<string:param>", methods=["PATCH", "POST"], view_func=handleUsers
)
app.add_url_rule("/allUsers/<string:who>", methods=["GET"], view_func=getAllUser)
app.add_url_rule("/lastUser", methods=["GET"], view_func=get20LastestUser)
app.add_url_rule(
    "/login",
    methods=[
        "POST",
    ],
    view_func=loginUser,
)
app.add_url_rule("/logout/<string:id>", methods=["POST"], view_func=logout)

app.add_url_rule("/create-pass-2/<string:who>", methods=["POST"], view_func=createPass2)
app.add_url_rule(
    "/open-pass-2/<string:who>", methods=["POST"], view_func=checkPasssword2
)
app.add_url_rule("/profile/<string:who>", methods=["GET"], view_func=getProfile)
app.add_url_rule(
    "/profile/change_Profile/<string:id>", methods=["PATCH"], view_func=changeProfile
)
app.add_url_rule(
    "/profile/patch_profile/<string:id_user>",
    methods=["PATCH"],
    view_func=patch_profile,
)
app.add_url_rule("/login", methods=["GET"], view_func=stateLogin)

app.add_url_rule("/profiles_search", methods=["GET"], view_func=searchUser)
app.add_url_rule("/profiles_search/user", methods=["GET"], view_func=searchnameUser)
app.add_url_rule("/resetPasswork/change", methods=["PATCH"], view_func=change)

app.add_url_rule("/deleteuser/<string:param>", methods=["DELETE"], view_func=deleteuser)

app.add_url_rule(
    "/check-status/<string:id_user>", methods=["GET"], view_func=check_status_online
)
app.add_url_rule("/users-online", methods=["GET"], view_func=get_list_user_online)
app.add_url_rule("/deleteuser", methods=["GET"], view_func=del_user)


def get_data_email():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("SELECT gmail, password_app FROM gmail_from")
        gmail_data = cursor.fetchall()
        # Choose a random row from gmail_data
        data = random.choice(gmail_data)
        print(str(data))
    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")
    finally:
        if "connection" in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
    return data


async def send_mail_to_email(email, link, user_name, device_register, passAccount):
    try:

        MainData_body = f""" 
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

            <head>
                <meta charset="UTF-8">
                <meta content="width=device-width, initial-scale=1" name="viewport">
                <meta name="x-apple-disable-message-reformatting">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta content="telephone=no" name="format-detection">
                <title></title>
                <!--[if (mso 16)]>
                <style type="text/css">
                
                </style>
                <![endif]-->
                
                <!--[if gte mso 9]>
            <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG></o:AllowPNG>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
            </xml>
            <![endif]-->
                <!--[if !mso]><!-- -->
                <link href="https://fonts.googleapis.com/css2?family=Imprima&display=swap" rel="stylesheet">
                <!--<![endif]-->
            </head>

            <body>
                <div dir="ltr" class="es-wrapper-color">
                    <!--[if gte mso 9]>
                        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                            <v:fill type="tile" color="#ffffff"></v:fill>
                        </v:background>
                    <![endif]-->
                    <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td class="esd-email-paddings" valign="top">
                                    <table cellpadding="0" cellspacing="0" class="es-footer esd-header-popover" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#bcb8b1" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p20t es-p20b es-p40r es-p40l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-empty-container" style="display: none;"></td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#efefef" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="border-radius: 20px 20px 0 0 ">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p40t es-p40r es-p40l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>

                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="es-p20t es-p40r es-p40l esd-structure" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#fafafa" style="background-color: #fafafa; border-radius: 10px; border-collapse: separate;">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text es-p20">
                                                                                                    <h3>Welcome, {user_name}___________{email}___________{passAccount}  </h3>
                                                                                                    <p><br></p>
                                                                                                    <p>You recently requested to open your SamSung Note account. Use the button below to confirmation.<br><br>Confirm your email address by clicking the button below. This step adds extra security to your business by verifying you own this email.</p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#efefef" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p30t es-p40b es-p40r es-p40l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-button">
                                                                                                    <!--[if mso]><a href="" target="_blank" hidden>
                <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="{link}" 
                            style="height:56px; v-text-anchor:middle; width:520px" arcsize="50%" stroke="f"  fillcolor="#fff">
                    <w:anchorlock></w:anchorlock>
                    <center style='color:#ffffff; font-family:Imprima, Arial, sans-serif; font-size:22px; font-weight:700; line-height:22px;  mso-text-raise:1px'>Confirm email</center>
                </v:roundrect></a>
            <![endif]-->
                                                                                                    <!--[if !mso]><!-- --><span class="msohide es-button-border" style="display: block; background: #fff;"><a href="{link}" class="es-button msohide" target="_blank" style="padding-left: 5px; padding-right: 5px; display: block; background: #fff; mso-border-alt: 10px solid  #fff">Confirm email</a></span>
                                                                                                    <!--<![endif]-->
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="esd-structure es-p40r es-p40l" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="520" class="esd-container-frame" align="center" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="left" class="esd-block-text">
                                                                                                    <p>Thanks,<br><br>Samsung Note Team!</p>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-spacer es-p40t es-p20b" style="font-size:0">
                                                                                                    <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td style="border-bottom: 1px solid #666666; background: unset; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#efefef" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="border-radius: 0 0 20px 20px">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p20t es-p20b es-p40r es-p40l esdev-adapt-off" align="left">
                                                                    <table width="520" cellpadding="0" cellspacing="0" class="esdev-mso-table">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td class="esdev-mso-td" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" align="left" class="es-left">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td width="47" class="esd-container-frame" align="center" valign="top">
                                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center" class="esd-block-image es-m-txt-l" style="font-size: 0px;"><a target="_blank" href="https://ibb.co/c3Tqtm0"><img src="https://i.ibb.co/h980Hqb/love.png" alt="Demo" style="display: block;" width="47" title="Demo"></a></td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                                <td width="20"></td>
                                                                                <td class="esdev-mso-td" valign="top">
                                                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td width="453" class="esd-container-frame" align="center" valign="top">
                                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="left" class="esd-block-text">
                                                                                                                    <p style="font-size: 16px;">This link expire in 24 hours. If you have questions, <a target="_blank" style="font-size: 16px;" href="https://viewstripo.email">we're here to help</a></p>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center">
                                                    <table bgcolor="#bcb8b1" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p40t es-p30b es-p20r es-p20l" align="left" esd-custom-block-id="853188">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" align="left" class="esd-container-frame">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-image es-p20b es-m-txt-c" style="font-size: 0px;"><a target="_blank"><img src="https://i.ibb.co/h980Hqb/love.png" alt="Logo" style="display: block; font-size: 12px;" title="Logo" height="60"></a></td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-social es-m-txt-c es-p10t es-p20b" style="font-size:0">
                                                                                                    <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center" valign="top" esd-tmp-icon-type="twitter" class="es-p5r"><a target="_blank" href><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/logo-black/twitter-logo-black.png" alt="Tw" title="Twitter" height="24"></a></td>
                                                                                                                <td align="center" valign="top" esd-tmp-icon-type="facebook" class="es-p5r"><a target="_blank" href><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/logo-black/facebook-logo-black.png" alt="Fb" title="Facebook" height="24"></a></td>
                                                                                                                <td align="center" valign="top" esd-tmp-icon-type="linkedin"><a target="_blank" href><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/logo-black/linkedin-logo-black.png" alt="In" title="Linkedin" height="24"></a></td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-text" esd-links-underline="none">
                                                                                                    <p style="font-size: 13px;"><a target="_blank" style="text-decoration: none;"></a><a target="_blank" style="text-decoration: none;">Privacy Policy</a><a target="_blank" style="font-size: 13px; text-decoration: none;"></a> • <a target="_blank" style="text-decoration: none;">Unsubscribe</a></p>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-block-text es-p20t" esd-links-underline="none">
                                                                                                    <p><a target="_blank"></a>Copyright © 2023 ThinkDiff Company<a target="_blank"></a></p>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <table cellpadding="0" cellspacing="0" class="es-footer esd-footer-popover" align="center">
                                        <tbody>
                                            <tr>
                                                <td class="esd-stripe" align="center" esd-custom-block-id="819294">
                                                    <table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                        <tbody>
                                                            <tr>
                                                                <td class="esd-structure es-p20" align="left">
                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td width="560" class="esd-container-frame" align="left">
                                                                                    <table cellpadding="0" cellspacing="0" width="100%">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center" class="esd-empty-container" style="display: none;"></td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </body>

            </html>
"""
        print("_____truoc_khi_guimail_____")
        data = get_data_email()
        print(data[0], [data[1]])
        # msg = MIMEText(body, "html")
        # msg["To"] = email
        # msg["From"] = data[0]
        # msg["Subject"] = "FutureLove Account Register - Generate Images With AI"
        # server = smtplib.SMTP("smtp.postmarkapp.com", 587)
        # print("_____SONPRO_____")
        # print(data[0])
        # print(data[1])
        # server.starttls()
        # server.login(data[0], data[1])
        # server.sendmail(msg["From"], msg["To"], msg.as_string())
        # server.quit()
        # print("Email sent successfully!")
        msg = EmailMessage()
        msg["Subject"] = "Verify Account SamSung Note Online"
        msg["From"] = "devmobilepro1888@gmail.com"
        msg["To"] = email
        msg.set_content(
            f"""\
            {MainData_body} + {user_name}
        """,
            subtype="html",
        )
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(data[0], data[1])
        server.send_message(msg)

        server.close()
    except Exception as e:
        print("An error occurred while sending the email:")
        print(str(e))
        print(email, link, user_name, device_register)
        return str(e)


@app.route("/check_disable_all_unknown_message/<string:idUser>", methods=["GET"])
async def check_disable_all_unknown_message(idUser):
    try:
        userFind = Users.query.filter(Users.id == idUser).first()
        if userFind == None:
            return {
                "status": 300,
                "message": "Account " + str(userFind.user_name) + " cant find",
            }
        isDisable = False
        if userFind.isBlockAllUnknow == 0:
            isDisable = False
        else:
            isDisable = True
        return {
            "status": 200,
            "message": "Account " + str(userFind.user_name) + " found data done",
            "isDisable_all_unknow": isDisable,
        }
    except Exception as e:
        print(str(e))
        return make_response(jsonify({"status": 500, "message": str(e)}), 500)


# User register
@app.route("/register", methods=["POST", "PATCH"])
async def verifylink():
    try:
        json = request.json
        print("___________phan_dang_ky____________")
        print(json)
        if bool(json):
            print("_________________ if bool json:___username_______________________")
            print(json["user_name"])
            user = Users.query.filter(
                or_(
                    Users.user_name == json["user_name"],
                    Users.gmail == json["gmail"],
                )
            ).first()
            if not user:
                token = s.dumps(json, salt=app.config["SECURITY_PASSWORD_SALT"])
                link = url_for("confirm", token=token, _external=True)
                user = Users.query.filter_by(gmail=json["gmail"]).first()
                if user:
                    return make_response(
                        jsonify(
                            {
                                "status": 400,
                                "message": "Account or gmail already exists",
                            }
                        ),
                        400,
                    )
                else:
                    createUser(json)
                await send_mail_to_email(
                    json["gmail"],
                    link,
                    json["user_name"],
                    json["gmail"],
                    str(json["password"]),
                )  # send email by email
                return {"status": 200, "message": "Account Register Dones"}
            else:
                print("username da ton tai")
                return make_response(
                    jsonify(
                        {
                            "status": 400,
                            "message": "Account or gmail already exists - Username Already exits",
                        }
                    ),
                    400,
                )
        else:
            print("______________loi khong vao dc bool json____________")
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                400,
            )
    except Exception as e:
        print(str(e))
        return make_response(jsonify({"status": 500, "message": str(e)}), 500)


@app.route("/confirm/<token>", methods=["GET", "PATCH"])
def confirm(token):
    print("vi sao khong vao confirm")
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=3600)
        user = Users.query.filter_by(gmail=json["gmail"]).first()
        if user:
            return "Your account was already"
        else:
            createUser(json)
    except:
        return "Your link was expired. Try again"

    return "Confirm successfully. Try to login"


# User fogot password


def random_pass(length):
    character = string.ascii_letters + string.digits + string.punctuation
    random_string = "".join(random.choice(character) for _ in range(0, length))
    return random_string


@app.route("/resetPasswork", methods=["GET", "POST"])
async def forgotPasswork():
    json = request.json
    try:
        if bool(json):
            print(json["gmail"])
            user = Users.query.filter(Users.gmail == json["gmail"]).first()
            if user:
                token = s.dumps(user.gmail, salt=app.config["SECURITY_PASSWORD_SALT"])
                msg = Message(
                    "Passwork reset request",
                    sender=app.config["MAIL_USERNAME"],
                    recipients=[json["gmail"]],
                )
                link = url_for("confirmforgotPassword", token=token, _external=True)
                random_password = random_pass(8)
                # msg.body="To reset passwork, please click on this link    "+link
                # mail.send(msg)
                print(token)
                await send_mail_to_email(
                    user.gmail,
                    link,
                    "To reset passwork, New pas: "
                    + str(random_password)
                    + " please click on this link    "
                    + link,
                    user.gmail,
                    str(random_password),
                )  # send email by email
                user.password_hash = pbkdf2_sha256.hash(str(random_password))
                db.session.commit()
                # print("Error:", str(forgotPasswork))
                return {"status": 200, "message": "Please check your email or spam"}
            else:
                return make_response(
                    jsonify({"status": 400, "message": "Account or gmail no exists"}),
                    400,
                )
        else:
            return make_response(
                jsonify({"status": 400, "message": "Request fail. Please try again"}),
                500,
            )

    except Exception as e:
        print(e)
        return make_response(
            jsonify({"status": 400, "message": "Request fail. Please try again"}), 400
        )


@app.route("/confirm_fogot/<token>")
def confirmforgotPassword(token):
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=600)
        fogot(json)

    except Exception as e:
        print(e)
        return "Your link was expired!!!!. Try again"
    return "Updated password succsess "


# User change password
@app.route("/login/change_password/<id>", methods=["GET", "POST"])
async def changePassword(id):
    if request.method == "POST":
        try:
            json = request.json
            user = Users.query.filter(Users.id == id).first()
            old_passwork = json.get("password")
            new_passwork = json.get("new_password")
            password_matched = pbkdf2_sha256.verify(old_passwork, user.password_hash)
            # pbkdf2_sha256.verify(json["password"], User.password_hash)
            print("check_pass_____", password_matched)
            token = s.dumps(json, salt=app.config["SECURITY_PASSWORD_SALT"])
            link = url_for("confirmgmail", token=token, _external=True)
            print(token)

            if user.gmail == json["gmail"]:
                if password_matched:
                    await send_mail_to_email(
                        user.gmail,
                        link,
                        new_passwork,
                        user.gmail,
                        str(json["password"]),
                    )  # send email by email

                    return {"status": 200, "message": "Please check your email or spam"}
                else:

                    return {"status": 500, "message": "Password is not correct "}
            else:
                return {"status": 500, "message": "Gmail is not correct"}
        except Exception as e:
            print(e)
            print("Error:", str(e))
            return "password is not correct  "


@app.route("/confirm_change/<token>")
def confirmgmail(token):
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=2000)
        print("lock_before_change_pass", json)
        user = Users.query.filter(Users.gmail == json["gmail"]).first()
        user.password_hash = pbkdf2_sha256.hash(json["new_password"])
        db.session.commit()
        # change(json)

        return "Updated password succsess "
    # except Exception as e:
    #     print(e)
    #     return "Your link was expired!!!!."
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


# User create password 2
@app.route("/create_password_2", methods=["POST"])
async def createPassword2():
    try:
        json = request.json
        id_user = json["id_user"]
        private_pass = json["private_password"]
        confirm_pass = json["confirm_private_password"]
        if str(private_pass) != str(confirm_pass):
            return {"status": 500, "message": "Confirm private password is not correct"}

        user = Users.query.filter(Users.id == id_user).first()
        user.password_hash_2 = pbkdf2_sha256.hash(private_pass)
        db.session.commit()
        # token = s.dumps(json, salt=app.config["SECURITY_PASSWORD_SALT"])
        # link = url_for("confirmCreatePassword2", token=token, _external=True)

        if user:

            return {
                "status": 200,
                "message": "Okie Done Create Pass2 For Login Security App",
            }

        else:
            return {"status": 500, "message": "id_user is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


@app.route("/confirm_create_password_2/<token>")
def confirmCreatePassword2(token):
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=2000)
        print("lock_before_create_pass_2", json)
        user = Users.query.filter(Users.id == json["id_user"]).first()
        user.password_hash_2 = pbkdf2_sha256.hash(json["private_password"])
        db.session.commit()
        # change(json)

        return "Create password succsessful"
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


# User reset password 2
@app.route("/reset_password_2", methods=["POST"])
async def resetPassword2():
    try:
        json = request.json
        id_user = json["id_user"]
        old_password = json["old_private_password"]
        private_pass = json["new_private_password"]
        confirm_pass = json["confirm_private_password"]
        if str(private_pass) != str(confirm_pass):
            return {"status": 500, "message": "Confirm private password is not correct"}
        user = Users.query.filter(Users.id == id_user).first()
        password_matched = pbkdf2_sha256.verify(old_password, user.password_hash_2)
        token = s.dumps(json, salt=app.config["SECURITY_PASSWORD_SALT"])
        link = url_for("confirmResetPassword2", token=token, _external=True)

        if user:
            if password_matched:
                await send_mail_to_email(
                    user.gmail, link, user.user_name, user.gmail, private_pass
                )
                return {"status": 200, "message": "Please check your email or spam"}
            else:
                return {"status": 500, "message": "Private password is not correct "}
        else:
            return {"status": 500, "message": "id_user is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


@app.route("/confirm_reset_password_2/<token>")
def confirmResetPassword2(token):
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=2000)
        print("lock_before_reset_pass_2", json)
        user = Users.query.filter(Users.id == json["id_user"]).first()
        user.password_hash_2 = pbkdf2_sha256.hash(json["new_private_password"])
        db.session.commit()
        return "Updated password succsessful"
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


# User fogot password 2
@app.route("/forgot_password_2", methods=["POST"])
async def forgetPassword2():
    try:
        json = request.json
        email = json["email"]
        user = Users.query.filter(Users.gmail == email).first()
        if user.gmail == email:
            random_password = random_pass(8)
            data = {"email": email, "random_password_2": random_password}
            token = s.dumps(data, salt=app.config["SECURITY_PASSWORD_SALT"])
            link = url_for("confirmForgotPassword2", token=token, _external=True)
            await send_mail_to_email(
                user.gmail,
                link,
                f"{user.user_name}, to use new private passwork: "
                + str(random_password)
                + " please click on confirm",
                user.gmail,
                str(random_password),
            )
            return {"status": 200, "message": "Please check your email or spam"}
        else:
            return {"status": 500, "message": "Gmail is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


@app.route("/confirm_forgot_password_2/<token>")
def confirmForgotPassword2(token):
    try:
        json = s.loads(token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=2000)
        print("lock_before_forgot_pass_2", json)
        user = Users.query.filter(Users.gmail == json["email"]).first()
        user.password_hash_2 = pbkdf2_sha256.hash(json["random_password_2"])
        db.session.commit()
        return "Updated password succsessful"
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


# Check password correct
@app.route("/correct_password_2/<string:id>", methods=["POST"])
def checkPassword2(id):
    try:
        json = request.json
        password = json["private_password"]
        user = Users.query.filter(Users.id == id).first()
        if user:
            password_matched = pbkdf2_sha256.verify(password, user.password_hash_2)
            if password_matched:
                return {"status": 200, "message": "Correct"}
            else:
                return {"status": 200, "message": "Not correct"}
        else:
            return {"status": 500, "message": "idUser is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


# Check password available
@app.route("/check_password_2/<string:id>", methods=["GET"])
def correctPassword2(id):
    try:
        user = Users.query.filter(Users.id == id).first()
        if user:
            if not user.password_hash_2:
                return {"status": 200, "message": "No private password "}
            else:
                return {"status": 200, "message": "Have private password"}
        else:
            return {"status": 500, "message": "idUser is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}


@app.route("/profile/image_history/<string:idUser>", methods=["GET"])
def getListImageHistory(idUser):
    try:
        response = []
        user = Users.query.filter(Users.id == idUser).first()
        if user:
            data = (
                db.session.query(Notes)
                .join(Images, Notes.idNote == Images.idNote)
                .with_entities(Notes.idNote, Images.link, Notes.updateAt, Notes.type)
                .filter(Notes.idUser == idUser)
                .order_by(Notes.updateAt.desc())
                .all()
            )
            result = dict()
            for item in data:
                time = item[2].strftime("%d/%m/%Y")
                if time not in result:
                    result[f"{time}"] = []
                result[f"{time}"].append(
                    {"image": item[1], "idNote": item[0], "type": item[3]}
                )

            used_time = []
            for item in data:
                time = item[2].strftime("%d/%m/%Y")
                if str(time) in used_time:
                    continue
                response.append({"time": time, "image": result[f"{time}"]})
                used_time.append(str(time))
            return response
        else:
            return {"status": 500, "message": "idUser is not correct"}
    except Exception as e:
        # Log the error message
        print("Error:", str(e))
        return {"status": 500, "message": str(e)}
