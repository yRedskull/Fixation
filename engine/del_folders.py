from tkinter import END
import os

def del_folders(self):
    for folder in self.backup_cb_lista:
                try:
                    if os.path.exists(os.path.join(self.direc_padrao, folder)) and len(os.listdir(
                            os.path.join(self.direc_padrao, folder))) == 0:
                        os.rmdir(os.path.join(self.direc_padrao, folder))
                        self.list_box_1.insert(END, f'Apagando a pasta "{folder}".')
                        self.list_box_1.see(END)
                        self.app.update()
                    else:
                        continue
                except OSError:
                    self.list_box_1.insert(END, f'Não foi possível apagar a pasta "{folder}".')
                    self.list_box_1.see(END)
                    self.app.update()