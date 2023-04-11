from engine.reverse_organize import reverse_organize
from gear.apart import question_del_folders
from engine.del_folders import del_folders
from tkinter import messagebox as mb
from time import sleep as sl
from tkinter import *
import os


def organize(self, bag, fog, bg_app):
    from gear.back import back_outset
    self.lista_no_move = ["desktop.ini", "netuser.ini", "Thumbs.db"]
    for _file in self.lista_no_move:
        if self.lista_arq[str(self.pasta)].count(_file) != 0:
            self.lista_arq[str(self.pasta)].remove(_file)
        else:
            continue

    for folder in self.backup_cb_lista:
        self.reverse_org[folder] = []
    if len(self.lista_arq[self.pasta]) != 0:
        for _file in self.lista_arq[self.pasta]:
            aceito = 0
            for key in self.formats:
                if aceito == 1:
                    break
                else:
                    for m_format in self.formats[key]:
                        if aceito == 1:
                            break
                        elif m_format in 'Pastas e outros':
                            continue
                        else:
                            for pos in range(len(_file) - 1, -1, -1):
                                if '.' in _file[pos]:
                                    if _file[pos:] in m_format:
                                        try:
                                            if os.path.exists(os.path.join(self.direc_padrao, key, _file)) and \
                                                    self.lista_arq[key].count(_file) != 0:
                                                for num in range(1, 100):
                                                    try:
                                                        os.rename(os.path.join(self.direc_padrao, _file),
                                                                os.path.join(self.direc_padrao, key,
                                                                            f'{_file[:pos]} ({num}){_file[pos:]}'))
                                                        self.list_box_1.insert(END,
                                                                            f'["{_file}" foi movido para a pasta "{key}" e renomeado...')
                                                        self.move_cont += 1 
                                                        self.list_box_1.see(END)
                                                        self.app.update()
                                                        self.list_box_1.insert(END,
                                                                            f'"{_file[:pos]} ({num}){_file[pos:]}"]')
                                                        self.app.update()
                                                        self.reverse_org[key].append(
                                                            f'{_file[:pos]} ({num}){_file[pos:]}')
                                                        break
                                                    except:
                                                        continue
                                            else:
                                                try:
                                                    os.rename(os.path.join(self.direc_padrao, _file),
                                                            os.path.join(self.direc_padrao, key, _file))
                                                    self.list_box_1.insert(END,
                                                                        f'"{_file}" foi movido para a pasta "{key}".')
                                                    self.move_cont += 1 
                                                    self.list_box_1.see(END)
                                                    self.app.update()
                                                    self.reverse_org[key].append(_file)
                                                except Exception:
                                                    self.list_box_1.insert(END, f'[ERRO] Não foi possível mover o arquivo "{_file}" para a pasta "{key}".')
                                                    continue
                                            aceito = 1
                                            break
                                        except:
                                            continue
                                    else:
                                        break
                                else:
                                    continue
                        
        self.lista_arq[self.pasta] = os.listdir(self.direc_padrao)

        from interface.outset import outset

        for pos, folder in enumerate(self.remove_list_box):
            if self.remove_list_box[pos][1] in 'Pastas e outros':
                self.outros_arquivos = self.remove_list_box[pos][0]
            try:
                if self.lista_arq[self.pasta].count(self.remove_list_box[pos][0]) == 1:
                    self.lista_arq[self.pasta].remove(str(self.remove_list_box[pos][0]))
                elif self.lista_arq[self.pasta].count(str(self.remove_list_box[pos][0]).lower()) == 1:
                    self.lista_arq[self.pasta].remove(str(self.remove_list_box[pos][0]).lower())
                elif self.lista_arq[self.pasta].count(str(self.remove_list_box[pos][0]).capitalize()) == 1:
                    self.lista_arq[self.pasta].remove(str(self.remove_list_box[pos][0]).capitalize())
                else:
                    mb.showerror(message='[ERRO]')
                    outset(self)

            except:
                continue

        if self.backup_cb_lista.count(self.outros_arquivos) == 1:        
            for _file in self.lista_arq[self.pasta]:
                cont = 0
                for pos in range(len(_file) - 1, -1, -1):
                    if cont == 0:
                        if '.' in _file[pos]:
                            if os.path.exists(os.path.join(self.direc_padrao, self.outros_arquivos, _file)
                                            ) and self.lista_arq[self.outros_arquivos].count(_file) != 0:
                                for num in range(1, 100):
                                    try:
                                        os.rename(os.path.join(self.direc_padrao, _file),
                                                os.path.join(self.direc_padrao,
                                                            self.outros_arquivos,
                                                            f'{_file[:pos]} ({num}){_file[pos:]}'))
                                        self.list_box_1.insert(END,
                                                            f'"{_file}" foi movido para a pasta "{self.outros_arquivos}" renomeado para')
                                        self.move_cont += 1 
                                        self.list_box_1.see(END)
                                        self.app.update()
                                        self.list_box_1.insert(END,
                                                            f'"{_file[:pos]} ({num}){_file[pos:]}".')
                                        self.app.update()
                                        self.reverse_org[self.outros_arquivos].append(
                                            f'{_file[:pos]} ({num}){_file[pos:]}')
                                        cont = 1
                                        break

                                    except Exception:
                                        continue
                            else:
                                try:
                                    os.rename(os.path.join(self.direc_padrao, _file),
                                            os.path.join(self.direc_padrao, self.outros_arquivos, _file))
                                    self.list_box_1.insert(END, f'"{_file}" foi movido para a pasta "{self.outros_arquivos}".')
                                    self.move_cont += 1 
                                    self.list_box_1.see(END)
                                    self.app.update()
                                    self.reverse_org[self.outros_arquivos].append(_file)
                                    cont = 1
                                except Exception:
                                    self.list_box_1.insert(END, f'[ERRO] Não foi possível mover o arquivo "{_file}" para a pasta "{self.outros_arquivos}".')
                                    continue
                        else:
                            continue
                    else:
                        break
            
                if cont == 0:
                    if self.backup_cb_lista.count(self.outros_arquivos) == 1:
                        try:
                            os.rename(os.path.join(self.direc_padrao, _file),
                                    os.path.join(self.direc_padrao, self.outros_arquivos, _file))
                            self.list_box_1.insert(END, f'"{_file}" foi movido para a pasta "{self.outros_arquivos}".')
                            self.move_cont += 1 
                            self.list_box_1.see(END)
                            self.app.update()
                            self.reverse_org[self.outros_arquivos].append(_file)
                        except Exception as e:
                            print(e)
                            self.list_box_1.insert(END, f'[ERRO] Não foi possível mover o arquivo "{_file}" para a pasta "{self.outros_arquivos}".')

        if len(self.backup_cb_lista) != 0:
            for folder in self.backup_cb_lista:
                self.lista_arq[folder] = os.listdir(os.path.join(self.direc_padrao, folder)) 
            self.list_box_1.insert(END, 'Êxito!')
            self.list_box_1.insert(END, f'{self.move_cont} itens movidos.' )
            self.list_box_1.see(END)
            self.app.update()
        else:
            self.list_box_1.configure(fg="#d00")
            self.list_box_1.insert(END, '[ERRO]')
            sl(1)
            mb.showwarning(message='Nenhuma pasta encontrada ou aceita para mover os arquivos.')
            mb.showinfo(message='Voltando a tela inicial...')
            outset(self)

        self.btn_1.config(command=lambda: back_outset(self))

        self.btn_2 = Button(self.frame_2, text='Reverter', command=lambda: reverse_organize(self), bg=bag, fg=fog, font=(
            'Arial', 10))
        self.btn_2.pack(side='left', padx=4, pady=1, ipady=2, ipadx=2)

        def configbgcolor(event):
            self.btn_2.config(bg=bg_app)
            return event

        def configbgbag(event):
            self.btn_2.config(bg=bag)
            return event

        self.btn_2.bind("<Enter>", configbgcolor)
        self.btn_2.bind("<Leave>", configbgbag)

        res = question_del_folders(self)
        if res == 'yes':
            del_folders(self)

    else:
        
        self.list_box_1.insert(END, f'[Atenção]')
        self.list_box_1.insert(END, f'Não existe arquivos para ser movidos na pasta "{self.pasta}"!')
        self.list_box_1.configure(fg="#F5D93D")
        self.app.update()
        sl(0.5)

        res = question_del_folders(self)
        if res == 'yes':
            del_folders(self)
        
        self.btn_1.config(command=lambda: back_outset(self))