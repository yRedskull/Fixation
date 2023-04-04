from tkinter import *
from gear.folders import *
from gear.back import *
import webbrowser as browser
from interface.add_folders import add_folders


def select_dir(self, bag, fog, fts):
        self.frame_1.destroy()
        self.btn_github.destroy()

        # Quadro
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

        self.frame_2 = Frame(self.frame_1)
        self.frame_2.configure(bg=bag)
        self.frame_2.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=0)
        self.frame_2.columnconfigure(weight=10, index="all")
        self.frame_2.rowconfigure(weight=10, index="all")

        # Itens do Quadro
        self.label_1 = Label(self.frame_2, text='Selecione o diretório.', font=fts, anchor="center", bg=bag, fg=fog)
        self.label_1.grid(column=5, row=0)

        self.btn_1 = Button(self.frame_1, image=self.img_back, command=lambda:back_outset(self),
                            highlightthickness=0, bd=0, bg=bag)
        self.btn_1.pack(ipady=1, ipadx=2, pady=1, padx=2, side="left")

        def configbgcolor(event):
            self.btn_1.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        self.direc = Button(self.frame_2, image=self.img_explorer, command=lambda: direct(self), bd=2, bg=bag)
        self.direc.grid(column=6, row=2)

        def configbgcolor(event):
            self.direc.config(bg="#222")
            return event

        def configbgbag(event):
            self.direc.config(bg=bag)
            return event

        self.direc.bind("<Enter>", configbgcolor)
        self.direc.bind("<Leave>", configbgbag)

        self.direc_show = Label(self.frame_2, font=("Arial", 12), text=self.direc_padrao, bg="#000", fg="#0a0")
        self.direc_show.grid(column=5, row=2)

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=0, ipady=0, padx=0, pady=0, side="bottom")

        self.run = Button(self.frame_2, image=self.img_next, command=lambda: add_folders(self, bag, fog, fts), highlightthickness=0, bd=0,
                          bg=bag)
        self.run.grid(column=5, row=3)

        def configbgcolor(event):
            self.run.config(bg="#222")
            return event

        def configbgbag(event):
            self.run.config(bg=bag)
            return event

        self.run.bind("<Enter>", configbgcolor)
        self.run.bind("<Leave>", configbgbag)

        def configbgcolor(event):
            self.btn_github.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_github.config(bg=bag)
            return event
    
        self.btn_github = Button(self.app, image=self.img_github, command=lambda: browser.open('https://github.com/yRedskull/Fixation'), font=fts, bg="#222", fg=fog, bd=0, highlightthickness=0)
        self.btn_github.pack(ipadx=0, ipady=0, padx=1, pady=1, side='bottom')
        self.btn_github.bind('<Enter>', configbgbag)
        self.btn_github.bind('<Leave>', configbgcolor)

        self.app.update()