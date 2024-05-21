from api import *
from config import SERVER_HOST, SERVER_PORT, SERVER_DEBUG
from pathlib import Path
Path('files').mkdir(exist_ok=True)
app.run(SERVER_HOST, port=SERVER_PORT, debug=SERVER_DEBUG)
