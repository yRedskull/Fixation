from tkinter import *
from tkinter.ttk import Progressbar
from var import on_config_json, config
from urllib import request
import os
from time import sleep as sl
from threading import Thread


class Auto_Update:
    def __init__(self, bag=config["Background-Color-APP"], fog=config["Foreground-Color"], fts=config["Font"]):
        try: 
            self.upt = Tk()
            self.upt.title('Auto-Update')
            self.upt.iconphoto(False, PhotoImage(file="image/logo.png", master=self.upt))
            self.upt.configure(background=bag)

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
            
            
            self.text_checkin = Label(self.upt, text='Auto Update Fixation', fg=fog, bg=bag, font=fts)
            self.text_checkin.pack(side='top', padx=5, pady=5)

            self.Varp = DoubleVar()
            self.progressbar = Progressbar(self.upt, variable=self.Varp, maximum=len(self.auto_update["folders-files"]))
            self.progressbar.pack(ipadx=200, padx=3, pady=3)

            self.upt.update()
            Thread(target=self.Update_file).start()
        
            self.sair = Button(self.upt, text="Reiniciar",command=self.Restart, bg=bag, fg=fog,font=fts)
            self.sair.pack(side="bottom", padx=2, pady=2, ipadx=10, ipady=3)

            self.upt.mainloop()
        except Exception:
            pass

    def Restart(self):
        self.upt.destroy()
        if os.path.exists('Fixation.exe'):
            os.startfile('Fixation.exe')
        else:
            os.startfile('run.py')

    def Update_file(self):
        cont = 0
        for file in self.files:
            self.Varp.set(cont)
            try:        
                url_online_file = os.path.join(self.url_base, file)
                url_on_content = request.urlopen(url_online_file).read().decode('utf8')
                url_local_file = os.path.join(os.getcwd(), file)
                if os.path.exists(url_local_file):
                    with open(url_local_file, 'r') as file_txt:
                        file_txt = file_txt.read()
                        if file_txt != url_on_content:
                            if file.count('/') >= 1:
                                for pos, l in enumerate(file):
                                    if '/' == file[pos]:
                                        pasta = file[:pos]
                                        break
                                if not os.path.exists(os.path.join(os.getcwd(), pasta)):
                                    os.mkdir(pasta)
                                request.urlretrieve(url_online_file, url_local_file)
                            else:    
                                continue
                else:
                    if file.count('/') >= 1:
                            for pos, l in enumerate(file):
                                if '/' == file[pos]:
                                    pasta = file[:pos]
                                    break
                            if not os.path.exists(os.path.join(os.getcwd(), pasta)):
                                os.mkdir(pasta)
                            request.urlretrieve(url_online_file, url_local_file)


            except:
                cont += 1
                continue
            self.upt.update()
            cont += 1
        self.Varp.set(len(self.files))    
        self.upt.update()
        
