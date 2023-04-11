from tkinter import *
from gear.listbox import *
from gear.back import back_add_folders
from interface.init_org import init_org
from gear.apart import information_lb
from tkinter.ttk import Combobox
from tkinter import messagebox as mb


def select_formats(self, bag, fog, fts, bg_app):
        if len(self.cb_1_lista) < 7:
            return mb.showwarning(title='Atenção', message="Mínimo de pastas não atingido!!! ")
        else:
            mb.showinfo(message="Selecione as pastas com seus respectivos formatos e clique no botão anexar.")
            self.list_formats = list(self.backup_cb_formats)
            self.backup_cb_lista = list(self.cb_1_lista)
            self.frame_1.destroy()
            self.frame_2.destroy()

            self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
            self.frame_1.configure(bg=bag)
            self.frame_1.pack(ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

            self.frame_2 = Frame(self.frame_1)
            self.frame_2.configure(bg=bag)
            self.frame_2.pack(ipadx=0, padx=0, pady=0, ipady=0)

            self.label_1 = Label(self.frame_2, text="Anexe as pastas com os formatos escolhidos", bg=bag, fg=fog,
                                 font=fts)
            self.label_1.pack(side='top', pady=5, padx=5)

            self.cb_1 = Combobox(self.frame_2, values=self.cb_1_lista, font=('Arial', 10))
            self.cb_1.pack(ipadx=30, ipady=2, padx=2, pady=2)
            self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

            self.formats = {
                'Arquivos': ['Pastas e outros'],
                'Documentos': ['*.pdf', '*.pptx', '*.txt', '*.cdr', '*.xml', '*.sql', '*.word', '*.doc', '*.docx',
                               '*.rtf', '*.ppt', '*.pps', '*.xls', '*.xlsx', '*.html', '*.dwg', '*.iss', '*.torrent'],
                'Executáveis': ['*.exe', '*.msi', '*.bat', '*.bin', '*.app', '*.iso'],
                'Imagens': ['*.jpeg', '*.jpg', '*.png', '*.gif', '*.jfif', '*.svg', '*.psd', '*.webp', '*.raw','*.tiff', '*.bmp', '*.cr2', '*.dng', '*.gpr', '*.nef'],
                'Compactados': ['*.zip', '*.rar', '*.7z'],
                'Áudios': ['*.mp3', '*.wma', '*.wav', '*.pcm', '*.flac', '*.m4a', '*.ogg'],
                'Vídeos': ['*.mp4', '*.avi', '*.wmv', '*.mov', '*.flv', '*.f4v', '*.swf', '*.mkv', '*.mpeg-2', '*.m4v', '*.webm']
            }

            def cb_2_formats():
                if len(self.list_formats) == 0:
                    for pos, folder in enumerate(self.formats):
                        self.list_formats.append(
                            str(self.formats[folder]).replace('[', '').replace(']', '').replace("'", ''))
                    self.backup_cb_formats = list(self.list_formats)
                    return self.list_formats
                else:
                    return self.list_formats

            self.cb_2 = Combobox(self.frame_2, values=cb_2_formats(), font=('Arial', 10))
            self.cb_2.set(self.list_formats[-1])
            self.cb_2.pack(ipadx=115, ipady=2, pady=2, padx=2)
            self.btn_2 = Button(self.frame_2, image=self.img_anexo, command=lambda: list_box_anexo(self), highlightthickness=0,
                                bd=0,
                                bg=bag)
            self.btn_2.pack(side='right', padx=5, pady=5)

            def configbgcolor(event):
                self.btn_2.config(bg="#222")
                return event

            def configbgbag(event):
                self.btn_2.config(bg=bag)
                return event

            self.btn_2.bind("<Enter>", configbgcolor)
            self.btn_2.bind("<Leave>", configbgbag)

            self.btn_1 = Button(self.frame_1, image=self.img_back, command=lambda: back_add_folders(self, bag, fog, fts, bg_app),
                                highlightthickness=0, bd=0, bg=bag)
            self.btn_1.pack(pady=5, padx=5, side='left')

            def configbgcolor(event):
                self.btn_1.config(bg="#222")
                return event

            def configbgbag(event):
                self.btn_1.config(bg=bag)
                return event

            self.btn_1.bind("<Enter>", configbgcolor)
            self.btn_1.bind("<Leave>", configbgbag)

            self.run = Button(self.frame_1, image=self.img_next, command=lambda: init_org(self, bag, fog, bg_app), highlightthickness=0,
                              bd=0, bg=bag)
            self.run.pack(side='right', pady=5, padx=5)

            def configbgcolor(event):
                self.run.config(bg="#222")
                return event

            def configbgbag(event):
                self.run.config(bg=bag)
                return event

            self.run.bind("<Enter>", configbgcolor)
            self.run.bind("<Leave>", configbgbag)

            self.btn_3 = Button(self.frame_2, image=self.img_minus, command=lambda: list_box_desanexar(self),
                                highlightthickness=0,
                                bd=0, bg=bag)
            self.btn_3.pack(side='right')

            def configbgcolor(event):
                self.btn_3.config(bg="#222")
                return event

            def configbgbag(*event):
                self.btn_3.config(bg=bag)
                return event

            self.btn_3.bind("<Enter>", configbgcolor)
            self.btn_3.bind("<Leave>", configbgbag)

            self._formats_show = Label(self.frame_1, text=self.texto_2, bg=bag, fg="#99DD00", font=fts)
            self._formats_show.pack(pady=3, side='bottom')

            self.list_box_1 = Listbox(self.frame_1, font=('Arial', 11), bg='#222', fg="#99DD00")
            self.list_box_1.pack(ipady=50, ipadx=180, padx=10, pady=10, side='bottom')

            self.btn_5 = Button(self.frame_2, image=self.img_information, command=lambda: information_lb(),
                                bg=bag, highlightthickness=0, bd=0)
            self.btn_5.pack(side='left', padx=5, pady=5)

            def configbgcolor(event):
                self.btn_5.config(bg="#222")
                return event

            def configbgbag(event):
                self.btn_5.config(bg=bag)
                return event

            self.btn_5.bind("<Enter>", configbgcolor)
            self.btn_5.bind("<Leave>", configbgbag)