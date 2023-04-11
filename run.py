from var import *
from interface.app import Start
import os


def Run():
    if on_config_json["Version"] != config["Version"]:
        os.startfile(os.path.join(local_file, 'auto_update.pyw'))
    else:
        Start()

if __name__ == '__main__':
    Run()