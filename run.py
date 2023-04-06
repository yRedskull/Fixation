from interface.app import Start
from auto_update import Auto_Update


if __name__ == "__main__":
    try:
        Auto_Update()
    except:
        ...

    Start()