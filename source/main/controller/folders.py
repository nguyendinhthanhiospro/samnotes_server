from source import app

from source.main.function.handleFolders import *
from source.main.function.loginUser import *

# id user
app.add_url_rule(
    "/folder/<string:param>",
    methods=["GET", "POST", "PATCH", "DELETE"],
    view_func=handleFolder,
)

app.add_url_rule(
    "/allfolder/<string:param>",
    methods=["GET"],
    view_func=allFolder,
)

app.add_url_rule(
    "/changefolder/<string:id>", methods=["PATCH", "DELETE"], view_func=changeFolder
)

app.add_url_rule(
    "/notefolder/<string:id>",
    methods=[
        "GET",
    ],
    view_func=getnotesFolder,
)

app.add_url_rule(
    "/token/",
    methods=[
        "GET",
    ],
    view_func=cofimtoken,
)
