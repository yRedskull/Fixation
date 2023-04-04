from tkinter import END
from gear.apart import txt_create_folders
from tkinter import messagebox as mb
from time import sleep as sl
import os


def create_folders(self):
    from interface.outset import outset

    
    self.list_box_1.insert(END, 'Começando...')
    self.app.update()
    sl(0.5)
    self.list_box_1.insert(END, txt_create_folders(self))
    self.app.update()
    sl(0.3)
    folder_exists = os.path.exists(self.direc_padrao) 
    if folder_exists:
        self.lista_arq[str(self.pasta)] = os.listdir(self.direc_padrao)
        lista_folders = list(self.backup_cb_lista)
        for folder in lista_folders:
            folder_exists = os.path.exists(os.path.join(self.direc_padrao, folder))

            if not folder_exists:
                try:
                    os.mkdir(os.path.join(self.direc_padrao, folder))
                except Exception:
                    self.list_box_1.insert(END, f'[ERRO] Não foi possível criar a pasta "{folder}"')
            else:
                self.lista_arq[folder] = os.listdir(os.path.join(self.direc_padrao, folder)) 
                res = mb.askquestion(
                    icon='warning', message=f'A pasta [{folder}] ja existe, deseja utiliza-la mesmo assim?')
                if res == 'no':
                    self.formats.pop(folder)
                    self.backup_cb_lista.remove(folder)
                else:
                    continue

        if len(self.backup_cb_lista) != 0:
            self.list_box_1.insert(END, 'Êxito!')
            self.app.update()
        else:
            self.list_box_1.configure(fg="#d00")
            self.list_box_1.insert(END, '[ERRO]')
            sl(1)
            mb.showwarning(message='Nenhuma pasta encontrada ou aceita para mover os arquivos.')
            mb.showinfo(message='Voltando a tela inicial...')
            outset(self)
    else:
        self.list_box_1.configure(fg="#d00")
        self.list_box_1.insert(END, '[ERRO]')
        sl(1)
        mb.showerror(title='Atenção', message='Diretório inexistente!!!')
        mb.showinfo(message='Voltando a tela inicial...')
        self.direc_padrao = ''
        outset(self)
