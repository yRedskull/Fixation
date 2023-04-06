import os
from tkinter import *
from var import config
from interface.outset import outset


class Start:
    def __init__(self):
        self.app = Tk()

        self.img_next = PhotoImage(file="image/next.png").subsample(1)
        self.img_anexo = PhotoImage(file='image/anexo.png').subsample(1)
        self.img_explorer = PhotoImage(file="image/explorer.png").subsample(1)
        self.img_back = PhotoImage(file="image/back.png").subsample(1)
        self.img_start = PhotoImage(file="image/start.png").subsample(1)
        self.img_information = PhotoImage(file='image/information.png').subsample(1)
        self.img_logo = PhotoImage(file="image/logo.png", master=self.app)
        self.img_minus = PhotoImage(file="image/minus.png").subsample(2)
        self.img_plus = PhotoImage(file='image/plus.png').subsample(2)
        self.img_github = PhotoImage(file='image/github.png').subsample(1)

        self.width_screen = self.app.winfo_screenwidth()
        self.height_screen = self.app.winfo_screenheight()
        self.win_height = 600
        self.win_width = 800
        width_plus = (self.width_screen//2 - self.win_width//2) 
        height_plus = (self.height_screen//2 - self.win_height//2) 
        self.app.geometry(f"{self.win_width}x{self.win_height}+{width_plus}+{height_plus}")
        self.app.resizable(False, False)

        self.app.iconphoto(False, self.img_logo)
        self.app.title(f"Fixation {config['Version']}")
        self.app.configure(background=config["Background-Color-APP"])

        self.nome = os.getlogin()
        self.move_cont = 0 
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
