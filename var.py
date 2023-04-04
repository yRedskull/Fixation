import json

try: 
    with open("config.json", "r") as vj:
        arquivo_json = vj.read()
    config = json.loads(arquivo_json)
except Exception:
    config = None