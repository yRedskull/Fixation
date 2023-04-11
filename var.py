import json, os
from urllib import request


with open("config.json", "r") as vj:
    arquivo_json = vj.read()
    config = json.loads(arquivo_json)

on_config_json = json.loads(request.urlopen(config["Auto-Update"]["url-config"]).read().decode('utf8'))

local_file = os.path.dirname(os.path.realpath(__file__))
