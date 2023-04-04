from tkinter import *
from gear.folders import *
from gear.back import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from interface.select_formats import select_formats

def add_folders(self, bag, fog, fts, bg_app):
        if self.direc_padrao == '':
            return mb.showinfo(icon='warning', message='Selecione o diretório antes de continuar!')

        self.frame_1.destroy()
        self.frame_2.destroy()
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

        self.frame_2 = Frame(self.frame_1)
        self.frame_2.configure(bg=bag)
        self.frame_2.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=0)
        self.frame_2.columnconfigure(weight=10, index="all")
        self.frame_2.rowconfigure(weight=10, index="all")

        self.label_1 = Label(self.frame_2,
                             text="Adicione as pastas.",
                             bg=bag, fg=fog, font=fts)
        self.label_1.grid()

        self.label_3 = Label(self.frame_2,
                             text="""Ex: Arquivos, Documentos, Executáveis, Imagens, Compactados, Áudios, Vídeos.
        (Min: 7 formatos de arquivo)""", bg=bag, fg=fog, font=('Arial', 13))
        self.label_3.grid(row=3)

        self.btn_4 = Button(self.frame_2, text="Usar Exemplo", command=lambda: cb_1_exemplo(self), highlightthickness=0,
                            bd=1, bg=bag, fg=fog, font=("Arial", 12))
        self.btn_4.grid(row=8, pady=2, ipadx=3, ipady=3)

        def configbgcolor(event):
            self.btn_4.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_4.config(bg=bag)
            return event

        self.btn_4.bind("<Enter>", configbgcolor)
        self.btn_4.bind("<Leave>", configbgbag)

        self.btn_5 = Button(self.frame_2, text='Redefinir', command=lambda: redefinir_pastas(self), highlightthickness=0,
                            bd=1, bg=bag, fg=fog, font=("Arial", 12))
        self.btn_5.grid(row=9, pady=2, ipadx=3, ipady=3)

        def configbgcolor(event):
            self.btn_5.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_5.config(bg=bag)
            return event

        self.btn_5.bind("<Enter>", configbgcolor)
        self.btn_5.bind("<Leave>", configbgbag)

        def key_press(event):
            if event.keysym == "Return":
                cb_1_adicionar(self)
            elif event.keysym == "Escape":
                cb_1_tirar(self)
        self.cb_1 = Combobox(self.frame_2, values=self.cb_1_lista, font=('Arial', 11))
        self.cb_1.grid(row=4)
        self.cb_1.bind("<Key>", key_press)

        if len(self.cb_1_lista) > 0:
            self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

        self.cb_1_lista_show = Label(self.frame_2, text=self.texto_1, bg=bag, fg=fog, font=fts)
        self.cb_1_lista_show.grid(row=5)

        self.btn_1 = Button(self.frame_2, image=self.img_plus, command=lambda: cb_1_adicionar(self), highlightthickness=0,
                            bd=0, bg=bag)
        self.btn_1.grid(row=6, ipadx=3, ipady=3)

        def configbgcolor(event):
            self.btn_1.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        self.btn_2 = Button(self.frame_2, image=self.img_minus, command=lambda: cb_1_tirar(self), highlightthickness=0, bd=0,
                            bg=bag)
        self.btn_2.grid(row=7, ipadx=3, ipady=3)

        def configbgcolor(event):
            self.btn_2.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_2.config(bg=bag)
            return event

        self.btn_2.bind("<Enter>", configbgcolor)
        self.btn_2.bind("<Leave>", configbgbag)

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=1, ipady=1, padx=1, pady=1, side="bottom")

        self.btn_3 = Button(self.frame_1, image=self.img_back, command=lambda: back_select_dir(self, bag, fog, fts, bg_app), font=("Arial", 8),
                            highlightthickness=0, bd=0, bg=bag)
        self.btn_3.pack(ipady=3, ipadx=3, pady=1, padx=2, side="left")

        def configbgcolor(event):
            self.btn_3.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_3.config(bg=bag)
            return event

        self.btn_3.bind("<Enter>", configbgcolor)
        self.btn_3.bind("<Leave>", configbgbag)

        self.run = Button(self.frame_2, image=self.img_next, command=lambda: select_formats(self, bag, fog, fts, bg_app), highlightthickness=0, bd=0, bg=bag)
        self.run.grid(column=6, row=3, ipadx=3, ipady=3)

        def configbgcolor(event):
            self.run.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.run.config(bg=bag)
            return event

        self.run.bind("<Enter>", configbgcolor)
        self.run.bind("<Leave>", configbgbag)
