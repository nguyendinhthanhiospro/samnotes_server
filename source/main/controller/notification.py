from source import app

from source.main.function.handlenotification import *
app.add_url_rule('/notifications',
                 methods=['GET', 'POST'], view_func=IOSpush_notifications)
app.add_url_rule('/androidnotifications',
                 methods=['GET', 'POST'], view_func=Androidpush_notifications)

app.add_url_rule('/notificationsemail/<string:id>',#id chat1vs1
                 methods=['GET', 'POST'], view_func=pushemail)

app.add_url_rule('/device/<string:id>',#idUser
                 methods=['GET', 'POST'], view_func=posttoken)