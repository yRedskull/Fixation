import os
from tkinter import *
from var import config
from interface.outset import outset


class Start:
    def __init__(self):
        self.app = Tk()

        self.img_next = PhotoImage(file="Image/next.png").subsample(1)
        self.img_anexo = PhotoImage(file='Image/anexo.png').subsample(1)
        self.img_explorer = PhotoImage(file="Image/explorer.png").subsample(1)
        self.img_back = PhotoImage(file="Image/back.png").subsample(1)
        self.img_start = PhotoImage(file="Image/start.png").subsample(1)
        self.img_information = PhotoImage(file='Image/information.png').subsample(1)
        self.img_logo = PhotoImage(file="Image/logo.png", master=self.app)
        self.img_minus = PhotoImage(file="Image/minus.png").subsample(2)
        self.img_plus = PhotoImage(file='Image/plus.png').subsample(2)
        self.img_github = PhotoImage(file='Image/github.png').subsample(1)

        self.width_screen = self.app.winfo_screenwidth()
        self.height_screen = self.app.winfo_screenheight()
        width_plus = int((550 * self.width_screen) / 1920)
        height_plus = int((250 * self.height_screen) / 1080)
        self.app.geometry(f"800x600+{width_plus}+{height_plus}")
        self.app.resizable(False, False)

        self.app.iconphoto(False, self.img_logo)
        self.app.title(f"Fixation {config['version']}")
        self.app.configure(background="#222")

        self.nome = os.getlogin()
        self.lista_no_move = list()
        self.cb_1_lista = list()
        self.backup_cb_lista = list()
        self.backup_cb_formats = list()
        self.remove_list_box = list()
        self.list_formats = list()
        self.formats = dict()
        self.lista_arq = dict()
        self.reverse_org = dict()
        self.texto_1 = "Pastas: 0"
        self.texto_2 = "Faltam 7 formatos."
        self.direc_padrao = ''
        self.obs = """OBS: Este programa é útil para organizar diretórios em pastas 
        separadas com os formatos adequados. """

        outset(self)

        self.app.mainloop()
