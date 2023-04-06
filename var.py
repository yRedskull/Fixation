import json
from urllib import request

try: 
    with open("config.json", "r") as vj:
        arquivo_json = vj.read()
    config = json.loads(arquivo_json)
except Exception:
    config = None

try:
    on_config_json = json.loads(request.urlopen(config["Auto-Update"]["url-config"]).read().decode('utf8'))
except:
    on_config_json = None