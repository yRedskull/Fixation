from urllib import request
from tkinter import Button
from interface.app import Start
import os


def Update_progress(self, bag, fog, fts):
    self.verify.destroy()
    
    cont = 0
    for file in self.files:
        self.Varp.set(cont)
        try:        
            Update(self, file)
        except Exception:
            cont += 1
            continue
        self.upt.update()
        cont += 1
    self.Varp.set(len(self.files))    
    self.upt.update()

    def configbgcolor(event):
            self.restart.config(bg="#333")
            return event

    def configbgbag(event):
        self.restart.config(bg=bag)
        return event
    
    self.restart = Button(self.upt, text="Reiniciar",command=lambda: Restart(self),
                            bg=bag, fg=fog,font=fts, highlightthickness=0, bd=1)
    self.restart.pack(side="bottom", padx=2, pady=2, ipadx=10, ipady=3)
    self.restart.bind("<Enter>", configbgcolor)
    self.restart.bind("<Leave>", configbgbag)

    self.upt.update()

def Update(self, file):
    url_online_file = os.path.join(self.url_base, file)
    url_local_file = os.path.join(os.getcwd(), file)
    if file.count('/') >= 1:
        for pos, l in enumerate(file):
            if '/' == file[pos]:
                pasta = file[:pos]
                break
        if not os.path.exists(os.path.join(os.getcwd(), pasta)):
            os.mkdir(pasta)
    request.urlretrieve(url_online_file, url_local_file)
    
def Restart(self):
    self.upt.destroy()
    self.restart_val = True
    Start()
