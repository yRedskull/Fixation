from interface.app import Start
from auto_update import Auto_Update
from var import *

if __name__ == "__main__":

    if on_config_json["Version"] != config["Version"]:
        Auto_Update()
    else:
        Start()