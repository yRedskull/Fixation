from tkinter import *
from tkinter.ttk import Progressbar
from var import config
from urllib import request
import json
import os
from time import sleep as sl

class Auto_Update:
    def __init__(self):
        try: 
            on_config = request.urlopen(config["Auto-Update"]["url-config"])
            on_config_json = json.loads(on_config.read().decode('utf8'))
            if on_config_json["Version"] != config["Version"]:
                self.upt = Tk()
                self.upt.title('Auto-Update')
                self.upt.iconphoto(False, PhotoImage(file="image/logo.png", master=self.upt))

                self.auto_update = dict(on_config_json["Auto-Update"])
                self.url_base = self.auto_update["url"]
                self.files = self.auto_update["folders-files"]

                self.width_screen = self.upt.winfo_screenwidth()
                self.height_screen = self.upt.winfo_screenheight()
                self.win_width = 280
                self.win_height = 100
                self.width_plus = (self.width_screen//2 - self.win_width//2) 
                self.height_plus = (self.height_screen//2 - self.win_height//2) 
                self.upt.geometry(f"{self.win_width}x{self.win_height}+{self.width_plus}+{self.height_plus}")
                self.upt.resizable(False, False)
                
                self.text_checkin = Label(self.upt, text='Auto Update Fixation', font=('Arial', 14))
                self.text_checkin.pack(side='top', padx=5, pady=5)

                self.Varp = DoubleVar()
                self.progressbar = Progressbar(self.upt, variable=self.Varp, maximum=len(self.auto_update["folders-files"]))
                self.progressbar.pack(ipadx=200, padx=3, pady=3)


                self.Update_file()
                
                self.sair = Button(self.upt, text="Close",command=self.upt.destroy, font=("Arial", 12))
                self.sair.pack(side="bottom", padx=2, pady=2, ipadx=10, ipady=3)

                self.upt.mainloop()
            else:
                pass
        except Exception:
            pass
        

    def Update_file(self):
        cont = 0
        for file in self.files:
            self.Varp.set(cont)
            try:        
                url_online = os.path.join(self.url_base, file)
                local_file = os.path.join(os.getcwd(), file)
                if file.count('/') >= 1:
                    for pos, l in enumerate(file):
                        if '/' == file[pos]:
                            pasta = file[:pos]
                            break
                    if not os.path.exists(os.path.join(os.getcwd(), pasta)):
                        os.mkdir(pasta)
                request.urlretrieve(url_online, local_file)
            except:
                cont += 1
                continue
            cont += 1
        self.Varp.set(len(self.files))      