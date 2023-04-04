import os
from tkinter import messagebox as mb

def information_lb():
    return mb.showinfo(message="Selecione as pastas com seus respectivos formatos e clique no botão anexar.")

def txt_create_folders(self):
    texto = 'Tentando criar as pastas: '
    for pos, folder in enumerate(self.backup_cb_lista):
        if folder == self.backup_cb_lista[len(self.backup_cb_lista) - 1]:
            texto = texto + str(self.backup_cb_lista[pos]) + '.'
        elif folder == self.backup_cb_lista[len(self.backup_cb_lista) - 2]:
            texto = texto + str(self.backup_cb_lista[pos]) + ' e '
        else:
            texto = texto + str(self.backup_cb_lista[pos]) + ', '
    return texto

def question_del_folders(self):
            cont = 0
            texto = 'Deseja apagar as pastas "'
            lista_folders = list(self.backup_cb_lista)
            for _folder in lista_folders:
                try:
                    self.lista_arq[_folder] = os.listdir(os.path.join(self.direc_padrao, _folder))
                except Exception:
                    continue
                if len(self.lista_arq[_folder]) == 0:
                    cont += 1
                    if not self.backup_cb_lista[len(self.backup_cb_lista) - 1] == _folder:
                        texto += _folder + ', '
                    else:
                        texto += _folder + '" que não contém arquivos?'
                else:
                    continue
            if cont != 0:
                teste_texto = texto.strip()
                if teste_texto[-1] == ',':
                    texto.replace(teste_texto[-1], '" que não contém arquivos?')
                question = mb.askquestion(message=texto)
                return question
            else:
                return ''