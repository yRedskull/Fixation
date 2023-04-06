from interface.app import Start
from auto_update import Auto_Update
from time import sleep as sl

if __name__ == "__main__":
    try:
        Auto_Update()
    except Exception:
        print('erro')
    sl(0.1)
    Start()