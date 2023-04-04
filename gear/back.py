def back_outset(self):
    from interface.outset import outset

    self.frame_1.destroy()
    self.frame_2.destroy()
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
    self.btn_github.destroy()
    outset(self)

def back_select_dir(self, bag, fog, fts):
    from interface.select_dir import select_dir

    self.frame_1.destroy()
    self.frame_2.destroy()
    self.btn_github.destroy()
    select_dir(self, bag, fog, fts)

def back_add_folders(self, bag, fog, fts):
    from interface.add_folders import add_folders

    self.frame_1.destroy()
    self.frame_2.destroy()
    self.cb_1_lista = list(self.backup_cb_lista)
    self.texto_2 = "Faltam 7 itens."
    self.remove_list_box = list()
    self.btn_github.destroy()
    add_folders(self, bag, fog, fts)