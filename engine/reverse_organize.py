from tkinter import *
from tkinter import messagebox as mb
from gear.apart import question_del_folders
from engine.del_folders import del_folders
from time import sleep as sl
import os


def reverse_organize(self):
    self.btn_1.config(command='')
    res = mb.askquestion(message=f'Tem certeza de que deseja reverter a organização na pasta "{self.pasta}"?')
    if res == 'yes':
        self.btn_2.destroy()
        self.lista_arq[self.pasta] = os.listdir(self.direc_padrao)
        self.list_box_1.insert(END, '-' * 200)
        self.app.update()
        sl(0.02)
        self.list_box_1.insert(END, 'Revertendo...')
        self.app.update()
        sl(0.02)
        for key in self.reverse_org:
            for _file in self.reverse_org[key]:
                if os.path.exists(os.path.join(self.direc_padrao, key, _file)):
                    if self.lista_arq[self.pasta].count(_file) != 0:
                        for pos in range(len(_file) - 1, -1, -1):
                            if '.' in _file[pos]:
                                try:
                                    os.rename(os.path.join(self.direc_padrao, key, _file), os.path.join(
                                        self.direc_padrao,
                                        f'{_file[:pos]} ({self.lista_arq[key].count(_file)}){_file[pos:]}'))
                                    self.list_box_1.insert(END, f'"{_file}" retornou a pasta "{self.pasta}".')
                                    self.list_box_1.see(END)
                                    self.app.update()
                                    sl(0.02)
                                except Exception:
                                    self.list_box_1.insert(END, f'[ERRO] Não foi possível retornar o arquivo "{_file}" para a pasta "{self.pasta}".')
                    else:
                        os.rename(os.path.join(self.direc_padrao, key, _file),
                                    os.path.join(self.direc_padrao, _file))
                        self.list_box_1.insert(END, f'"{_file}" retornou a pasta "{self.pasta}".')
                        self.list_box_1.see(END)
                        self.app.update()
                        sl(0.02)
                else:
                    self.list_box_1.insert(END, f'"{_file}" não existe mais na pasta "{self.pasta}".')
                    self.app.update()

        for key in self.reverse_org:
            for _file in self.reverse_org[key]:
                self.reverse_org[key].remove(_file)

        res = question_del_folders(self)
        if res == 'yes':
            del_folders(self)
        if self.list_box_1.get(END) == 'Revertendo...':
            self.list_box_1.configure(fg="#d00")
            self.app.update()
            for num in range(0, 5):
                self.list_box_1.insert(END, '-')
                self.app.update()
                sl(0.1)
            self.list_box_1.insert(END, '[ERRO]')
            self.app.update()
            sl(0.5)
            self.list_box_1.insert(END, 'Nenhum item identificado para ser movido!')
            self.app.update()

    else:
        pass

    from gear.back import back_outset
    self.btn_1.config(command=lambda: back_outset(self))

