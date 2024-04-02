from api import *
from config import SERVER_HOST, SERVER_PORT, SERVER_DEBUG

app.run(SERVER_HOST, port=SERVER_PORT, debug=SERVER_DEBUG)
