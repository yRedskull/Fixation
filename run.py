from var import *
from interface.app import Start
import subprocess


def Run():
    if on_config_json["Version"] != config["Version"]:
        subprocess.call("auto_update.pyw", shell=True)
    else:
        Start()

if __name__ == '__main__':
    Run()