from tkinter import *
from var import config
import webbrowser as browser
from interface.select_dir import select_dir

def outset(self,  bag=config['Background-Color'], fog=config['Foreground-Color'], fts=(config['Font'][0], config['Font'][1]), bg_app=config["Background-Color-APP"]):
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", fill=X, expand=True)

        self.label_1 = Label(self.frame_1, text=f'''Olá {self.nome}, seja bem vindo ao Fixation!
Clique no botão abaixo para começarmos.''', anchor="w", bg=bag, fg=fog, font=fts)
        self.label_1.pack(ipadx=1, ipady=1, padx=1, pady=3, side="top")

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=1, ipady=1, padx=1, pady=1, side="bottom")

        def configbgcolor(event):
            self.btn_1.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1 = Button(self.frame_1, image=self.img_start, command=lambda: select_dir(self, bag, fog, fts, bg_app), highlightthickness=0, bd=0, bg=bag)
        self.btn_1.pack(ipadx=3, ipady=3, padx=10, pady=50)
        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        def configbgcolor(event):
            self.btn_github.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_github.config(bg=bag)
            return event
    
        self.btn_github = Button(self.app, image=self.img_github,  command=lambda: browser.open('https://github.com/yRedskull/Fixation'), bg=bg_app, fg=fog, bd=0, highlightthickness=0)
        self.btn_github.pack(ipadx=3, ipady=3, padx=1, pady=1, side='bottom')
        self.btn_github.bind('<Enter>', configbgbag)
        self.btn_github.bind('<Leave>', configbgcolor)

        self.app.update()
