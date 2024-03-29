from tkinter import *
from tkinter.ttk import Progressbar
from interface.app import Start
from var import on_config_json, config
from engine.update import Update_progress
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
            self.restart_val = False

            self.width_screen = self.upt.winfo_screenwidth()
            self.height_screen = self.upt.winfo_screenheight()
            self.win_width = 280
            self.win_height = 130
            self.width_plus = (self.width_screen//2 - self.win_width//2) 
            self.height_plus = (self.height_screen//2 - self.win_height//2) 
            self.upt.geometry(f"{self.win_width}x{self.win_height}+{self.width_plus}+{self.height_plus}")
            self.upt.resizable(False, False)
            
            self.text_checkin = Label(self.upt, text='Auto Update Fixation', fg=fog, bg=bag, font=fts)
            self.text_checkin.pack(side='top', padx=5, pady=5)

            self.Varp = DoubleVar()
            self.progressbar = Progressbar(self.upt, variable=self.Varp, maximum=len(self.auto_update["folders-files"]))
            self.progressbar.pack(ipadx=200, ipady=6, padx=3, pady=3)

            def configbgcolor(event):
                self.verify.config(bg='#333')
                return event

            def configbgbag(event):
                self.verify.config(bg=bag)
                return event
            
            self.verify = Button(self.upt, text="Atualizar",command=lambda: Thread(target=Update_progress(self, bag, fog, fts)).start(),
                                     bg=bag, fg=fog,font=fts, highlightthickness=0, border=1)
            self.verify.pack(side="bottom", padx=4, pady=4, ipadx=5, ipady=1)
            self.verify.bind("<Enter>", configbgcolor)
            self.verify.bind("<Leave>", configbgbag)
            self.upt.update()

            self.upt.mainloop()

            if not self.restart_val:
                Start()
            
        except Exception:
            pass

if __name__ == "__main__":
    Auto_Update()
