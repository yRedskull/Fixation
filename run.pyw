from var import *
import os


def Run():
    if on_config_json["Version"] != config["Version"]:
        os.startfile('auto_update')
    else:
        os.startfile('interface/app.pyw')

if __name__ == '__main__':
    Run()