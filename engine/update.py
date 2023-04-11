from urllib import request
from tkinter import Button
from threading import Thread
import subprocess, os


def Update_file(self, bag, fog, fts):
        self.verificar.destroy()
        
        cont = 0
        for file in self.files:
            self.Varp.set(cont)
            try:        
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

            except:
                cont += 1
                continue
            self.upt.update()
            cont += 1
        self.Varp.set(len(self.files))    
        self.upt.update()
        self.restart = Button(self.upt, text="Reiniciar",command=lambda: Thread(target=Restart(self)),
                              bg=bag, fg=fog,font=fts, highlightthickness=0, bd=0)
        self.restart.pack(side="bottom", padx=2, pady=2, ipadx=10, ipady=3)
        self.upt.update()
    
def Restart(self):
        self.upt.destroy()
        if os.path.exists('Fixation.exe'):
            subprocess.call('Fixation.exe', shell=True)
        else:
            subprocess.call('run.py', shell=True)

if __name__ == "__main__":
    subprocess.call('auto_update.pyw', shell=True)