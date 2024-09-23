from source import socketIo, app
from source.socket import *

import source.main.controller


if __name__ == "__main__":
    socketIo.run(app, host="127.0.0.1", port=18011)
    #  ssl_context=('/etc/ssl/samnotes_online.crt','/etc/ssl/samnotes.online.key'))
