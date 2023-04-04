from tkinter import *
from gear.back import back_outset
from tkinter import messagebox as mb
from time import sleep as sl
from engine.create_folders import create_folders
from engine.organize import organize

def init_org(self, bag, fog, bg_app):
        if len(self.list_formats) != 0 and len(self.cb_1_lista) != 0:
            if len(self.list_formats) != 1 and len(self.cb_1_lista) != 1:
                return mb.showwarning(title='Atenção',
                                      message=f"Faltam {len(self.list_formats)} formatos a serem anexados!!!")
            else:
                return mb.showwarning(title='Atenção',
                                      message=f"Falta {len(self.list_formats)} formato a ser anexado!!!")

        else:
            self.frame_1.destroy()
            self.frame_2.destroy()

            self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
            self.frame_1.configure(bg=bag)
            self.frame_1.pack(ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

            self.frame_2 = Frame(self.frame_1)
            self.frame_2.configure(bg=bag)
            self.frame_2.pack(ipadx=0, padx=0, pady=0, ipady=0)

            self.btn_1 = Button(self.frame_1, bg=bag, image=self.img_back, highlightthickness=0, bd=0)
            self.btn_1.pack(side='top', pady=3, padx=3, ipadx=3, ipady=3)

            def configbgcolor(event):
                self.btn_1.config(bg=bg_app)
                return event

            def configbgbag(event):
                self.btn_1.config(bg=bag)
                return event

            self.btn_1.bind("<Enter>", configbgcolor)
            self.btn_1.bind("<Leave>", configbgbag)

            self.scrollbar = Scrollbar(self.frame_2, orient=VERTICAL)

            self.list_box_1 = Listbox(self.frame_2, bg=bg_app, fg="#99DD00", font=('Arial', 12), yscrollcommand=self.scrollbar.set)

            self.scrollbar.config(command=self.list_box_1.yview)
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.list_box_1.pack(ipady=130, ipadx=400, padx=5, pady=5, fill=BOTH, expand=True)
            
            mb.showinfo(message='As alterações a seguir poderão ser desfeitas caso deseje.')
            for carac in range(len(self.direc_padrao) - 1, -1, -1):
                if self.direc_padrao[carac] == '/':
                    self.pasta = self.direc_padrao[carac + 1:]
                    break
            self.iniciar = mb.askquestion(title='Atenção', message=f'Iniciar a organização na pasta {self.pasta}?',
                                          icon='question')
            if self.iniciar == 'no':
                mb.showinfo(message='Voltando a tela inicial...')
                back_outset(self)
            else:
                self.formats_descart = dict(self.formats)
                for folder in self.remove_list_box:
                    cont = 0
                    for key in self.formats_descart:
                        if cont == 1:
                            break
                        else:
                            if str(self.formats[key]).replace('[', '').replace(']', '').replace("'", '') in folder[1]:
                                self.formats[folder[0]] = self.formats.pop(key)
                                cont = 1
                            else:
                                continue
                create_folders(self)
                self.app.update()
                sl(0.5)
                self.list_box_1.insert(END, 'Iniciando a organização...')
                self.app.update()
                sl(0.2)
                if not len(self.backup_cb_lista) == 0:
                    organize(self, bag, fog, bg_app)
                else:
                    self.list_box_1.insert(END, '[ERRO] Não existe pasta para iniciar a movimentação de arquivos!')
                    self.list_box_1.configure(fg="#d00")
                    self.app.update()
