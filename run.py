from interface.app import Start
from auto_update import Auto_Update
from threading import Thread
from var import *

if __name__ == "__main__":

    if on_config_json["Version"] != config["Version"]:
        Thread(target=Auto_Update()).start()
    else:
        Thread(target=Start()).start()