from source import db
from source.main.model.users import Users
from source.main.model.notes import Notes
from source.main.model.datas import Datas
from source.main.model.groups import Groups
from source.main.model.ChatGroupModel import ChatGroupModel
from source.main.model.members import Members
from source.main.model.chatUnknowns import ChatUnknowns
from source.main.model.nbnotes import Nbnotes
from source.main.model.floders import Folder
from source.main.model.chat1vs1 import Chat1vs1
from source.main.model.relationship import Relationship

if __name__ == "__main__":
    db.create_all()
