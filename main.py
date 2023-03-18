# Import
from tkinter import *
import webbrowser as browser
import os
import sys
from tkinter.filedialog import askdirectory as directory_
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from time import sleep as sl
import json


# Def/Class

class Start:
    back_gr = "#333"
    fore_gr = "#DE6F1B"
    font_si = ("Arial", 14)

    # verde = #99DD00
    # laranja = #DE721F
    # rosa = #A91FDE
    # azul = #14C5DE
    def __init__(self):
        #  1920 -- 500
        #  width -- width_plus
        #  width_plus = (500*width)/1920

        # 1080 -- 200
        # height -- height_plus
        # height_plus = (200*height)/1080

        # Principal *app*
        self.app = Tk()

        # Pictures
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

        # Resolution
        self.width_screen = self.app.winfo_screenwidth()
        self.height_screen = self.app.winfo_screenheight()
        width_plus = int((550 * self.width_screen) / 1920)
        height_plus = int((250 * self.height_screen) / 1080)
        self.app.geometry(f"800x600+{width_plus}+{height_plus}")
        self.app.resizable(False, False)

        # Config
        try: 
            with open("version.json", "r") as vj:
                arquivo_json = vj.read()
            version = json.loads(arquivo_json)
        except Exception:
            version = {"version": ''}

        self.app.iconphoto(False, self.img_logo)
        self.app.title(f"Fixation {version['version']}")
        self.app.configure(background="#222")

        # Var
        self.formats_descart = None
        self.outros_arquivos = None
        self.pasta = None
        self.iniciar = None
        self.list_box_1 = None
        self.list_box_2 = None
        self._formats_show = None
        self.cb_1_lista_show = None
        self.cb_1 = None
        self.cb_2 = None
        self.direc_show = None
        self.frame_1 = None
        self.frame_2 = None
        self.label_1 = None
        self.label_2 = None
        self.label_3 = None
        self.btn_1 = None
        self.btn_2 = None
        self.btn_3 = None
        self.btn_4 = None
        self.btn_5 = None
        self.btn_github = None
        self.direc = None
        self.run = None
        self.sistema = sys.platform
        self.nome = os.getlogin()
        self.lista_no_move = list()
        self.cb_1_lista = list()
        # self.backup_cb_lista é para fazer backup das pastas removidas no momento do anexo
        self.backup_cb_lista = list()
        # self.backup_cb_formats é para fazer backup dos formatos em uma única string removidos no momento do anexo
        self.backup_cb_formats = list()
        # self.remove_list_box é para a locação dos anexos de pastas e formatos em uma única string feito pelo usuário
        self.remove_list_box = list()
        # self.list_formats é para a locação dos formatos em uma única string, dentro de uma lista
        self.list_formats = list()
        # self.formats é para a locação dos formatos de arquivo separadamente em uma lista
        self.formats = dict()
        self.lista_arq = dict()
        self.reverse_org = dict()
        self.cont_cb, self.cont_fm, self.val_cb_fol, self.val_cb_for = (0, 0, 0, 0)
        self.texto_1 = "Pastas: 0"
        self.texto_2 = "Faltam 7 formatos."
        self.direc_padrao = ''
        self.obs = """OBS: Esse programa serve para organizar qualquer diretório que esteja bagunçado, 
                colocando-os em pastas separadas por formatos de arquivo. """

        # Start

        self.inicio()

        self.app.mainloop()

    # Telas

    def inicio(self, bag=back_gr, fog=fore_gr, fts=font_si):
        # Quadro
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", fill=X, expand=True)

        # Itens do Quadro
        self.label_1 = Label(self.frame_1, text=f'''Olá {self.nome}, seja bem vindo ao Fixation!
Clique no botão abaixo para começarmos.''', anchor="w", bg=bag, fg=fog, font=fts)
        self.label_1.pack(ipadx=1, ipady=1, padx=1, pady=3, side="top")

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=1, ipady=1, padx=1, pady=1, side="bottom")

        def configbgcolor(event):
            self.btn_1.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1 = Button(self.frame_1, image=self.img_start, command=self.escolher_pasta, highlightthickness=0, bd=0,
                            bg=bag)
        self.btn_1.pack(ipadx=0, ipady=0, padx=10, pady=50)
        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        def configbgcolor(event):
            self.btn_github.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_github.config(bg=bag)
            return event
    
        self.btn_github = Button(self.app, image=self.img_github,  command=lambda: browser.open('https://github.com/yRedskull/Fixation'), bg="#222", fg=fog, bd=0, highlightthickness=0)
        self.btn_github.pack(ipadx=0, ipady=0, padx=1, pady=1, side='bottom')
        self.btn_github.bind('<Enter>', configbgbag)
        self.btn_github.bind('<Leave>', configbgcolor)

        self.app.update()

    def escolher_pasta(self, bag=back_gr, fog=fore_gr, fts=font_si):
        self.frame_1.destroy()
        self.btn_github.destroy()

        # Quadro
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

        self.frame_2 = Frame(self.frame_1)
        self.frame_2.configure(bg=bag)
        self.frame_2.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=0)
        self.frame_2.columnconfigure(weight=10, index="all")
        self.frame_2.rowconfigure(weight=10, index="all")

        # Itens do Quadro
        self.label_1 = Label(self.frame_2, text='Selecione o diretório.', font=fts, anchor="center", bg=bag, fg=fog)
        self.label_1.grid(column=5, row=0)

        self.btn_1 = Button(self.frame_1, image=self.img_back, command=self.voltar_inicio,
                            highlightthickness=0, bd=0, bg=bag)
        self.btn_1.pack(ipady=1, ipadx=2, pady=1, padx=2, side="left")

        def configbgcolor(event):
            self.btn_1.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        self.direc = Button(self.frame_2, image=self.img_explorer, command=self.direct, bd=2, bg=bag)
        self.direc.grid(column=6, row=2)

        def configbgcolor(event):
            self.direc.config(bg="#222")
            return event

        def configbgbag(event):
            self.direc.config(bg=bag)
            return event

        self.direc.bind("<Enter>", configbgcolor)
        self.direc.bind("<Leave>", configbgbag)

        self.direc_show = Label(self.frame_2, font=("Arial", 12), text=self.direc_padrao, bg="#000", fg="#0a0")
        self.direc_show.grid(column=5, row=2)

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=0, ipady=0, padx=0, pady=0, side="bottom")

        self.run = Button(self.frame_2, image=self.img_next, command=self.adicionar_pastas, highlightthickness=0, bd=0,
                          bg=bag)
        self.run.grid(column=5, row=3)

        def configbgcolor(event):
            self.run.config(bg="#222")
            return event

        def configbgbag(event):
            self.run.config(bg=bag)
            return event

        self.run.bind("<Enter>", configbgcolor)
        self.run.bind("<Leave>", configbgbag)

        def configbgcolor(event):
            self.btn_github.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_github.config(bg=bag)
            return event
    
        self.btn_github = Button(self.app, image=self.img_github, command=lambda: browser.open('https://github.com/yRedskull/Fixation'), font=fts, bg="#222", fg=fog, bd=0, highlightthickness=0)
        self.btn_github.pack(ipadx=0, ipady=0, padx=1, pady=1, side='bottom')
        self.btn_github.bind('<Enter>', configbgbag)
        self.btn_github.bind('<Leave>', configbgcolor)

        self.app.update()

    def adicionar_pastas(self, bag=back_gr, fog=fore_gr, fts=font_si):
        if self.direc_padrao == '':
            return mb.showinfo(icon='warning', message='Selecione o diretório antes de continuar!')

        self.frame_1.destroy()
        self.frame_2.destroy()
        self.btn_github.destroy()

        # Quadro
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
        self.frame_1.configure(bg=bag)
        self.frame_1.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

        self.frame_2 = Frame(self.frame_1)
        self.frame_2.configure(bg=bag)
        self.frame_2.pack(anchor="center", ipadx=0, padx=0, pady=0, ipady=0)
        self.frame_2.columnconfigure(weight=10, index="all")
        self.frame_2.rowconfigure(weight=10, index="all")

        # Itens do Quadro
        self.label_1 = Label(self.frame_2,
                             text="Adicione as pastas.",
                             bg=bag, fg=fog, font=fts)
        self.label_1.grid()

        self.label_3 = Label(self.frame_2,
                             text="""Ex: Arquivos, Documentos, Executáveis, Imagens, Compactados, Áudios, Vídeos.
        (Min: 7 formatos de arquivo)""", bg=bag, fg=fog, font=('Arial', 13))
        self.label_3.grid(row=3)

        self.btn_4 = Button(self.frame_2, text="Usar Exemplo", command=self.cb_1_exemplo, highlightthickness=0,
                            bd=1, bg=bag, fg=fog, font=("Arial", 12))
        self.btn_4.grid(row=8, pady=2)

        def configbgcolor(event):
            self.btn_4.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_4.config(bg=bag)
            return event

        self.btn_4.bind("<Enter>", configbgcolor)
        self.btn_4.bind("<Leave>", configbgbag)

        self.btn_5 = Button(self.frame_2, text='Redefinir', command=self.redefinir_pastas, highlightthickness=0,
                            bd=1, bg=bag, fg=fog, font=("Arial", 12))
        self.btn_5.grid(row=9, pady=2)

        def configbgcolor(event):
            self.btn_5.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_5.config(bg=bag)
            return event

        self.btn_5.bind("<Enter>", configbgcolor)
        self.btn_5.bind("<Leave>", configbgbag)

        self.cb_1 = Combobox(self.frame_2, values=self.cb_1_lista, font=('Arial', 11))
        self.cb_1.grid(row=4)
        self.cb_1.bind("<Key>", self.key_press)
        if len(self.cb_1_lista) > 0:
            self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

        self.cb_1_lista_show = Label(self.frame_2, text=self.texto_1, bg=bag, fg=fog, font=fts)
        self.cb_1_lista_show.grid(row=5)

        self.btn_1 = Button(self.frame_2, image=self.img_plus, command=self.cb_1_adicionar, highlightthickness=0,
                            bd=0, bg=bag)
        self.btn_1.grid(row=6)

        def configbgcolor(event):
            self.btn_1.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_1.config(bg=bag)
            return event

        self.btn_1.bind("<Enter>", configbgcolor)
        self.btn_1.bind("<Leave>", configbgbag)

        self.btn_2 = Button(self.frame_2, image=self.img_minus, command=self.cb_1_tirar, highlightthickness=0, bd=0,
                            bg=bag)
        self.btn_2.grid(row=7)

        def configbgcolor(event):
            self.btn_2.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_2.config(bg=bag)
            return event

        self.btn_2.bind("<Enter>", configbgcolor)
        self.btn_2.bind("<Leave>", configbgbag)

        self.label_2 = Label(self.frame_1, text=self.obs,
                             anchor="center", bg=bag, fg=fog, font=("Arial", 12))
        self.label_2.pack(ipadx=1, ipady=1, padx=1, pady=1, side="bottom")

        self.btn_3 = Button(self.frame_1, image=self.img_back, command=self.voltar_escolher_pasta, font=("Arial", 8),
                            highlightthickness=0, bd=0, bg=bag)
        self.btn_3.pack(ipady=1, ipadx=2, pady=1, padx=2, side="left")

        def configbgcolor(event):
            self.btn_3.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_3.config(bg=bag)
            return event

        self.btn_3.bind("<Enter>", configbgcolor)
        self.btn_3.bind("<Leave>", configbgbag)

        self.run = Button(self.frame_2, image=self.img_next, command=self.selecionar_formatos, highlightthickness=0,
                          bd=0, bg=bag)
        self.run.grid(column=6, row=3)

        def configbgcolor(event):
            self.run.config(bg="#222")
            return event

        def configbgbag(event):
            self.run.config(bg=bag)
            return event

        self.run.bind("<Enter>", configbgcolor)
        self.run.bind("<Leave>", configbgbag)

        def configbgcolor(event):
            self.btn_github.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_github.config(bg=bag)
            return event
    
        self.btn_github = Button(self.app, image=self.img_github, command=lambda: browser.open('https://github.com/yRedskull/Fixation'), font=fts, bg="#222", fg=fog, bd=0, highlightthickness=0)
        self.btn_github.pack(ipadx=0, ipady=0, padx=1, pady=1, side='bottom')
        self.btn_github.bind('<Enter>', configbgbag)
        self.btn_github.bind('<Leave>', configbgcolor)

        self.app.update()

    def selecionar_formatos(self, bag=back_gr, fog=fore_gr, fts=font_si):
        if len(self.cb_1_lista) < 7:
            return mb.showwarning(title='Atenção', message="Mínimo de pastas não atingido!!! ")
        else:
            mb.showinfo(message="Selecione as pastas com seus respectivos formatos e clique no botão anexar.")
            self.list_formats = [c for c in self.backup_cb_formats]
            self.backup_cb_lista = [c for c in self.cb_1_lista]
            self.frame_1.destroy()
            self.frame_2.destroy()
            self.btn_github.destroy()

            # Quadro
            self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
            self.frame_1.configure(bg=bag)
            self.frame_1.pack(ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

            self.frame_2 = Frame(self.frame_1)
            self.frame_2.configure(bg=bag)
            self.frame_2.pack(ipadx=0, padx=0, pady=0, ipady=0)

            # Itens do Quadro
            self.label_1 = Label(self.frame_2, text="Anexe as pastas com os formatos escolhidos", bg=bag, fg=fog,
                                 font=fts)
            self.label_1.pack(side='top', pady=5, padx=5)

            self.cb_1 = Combobox(self.frame_2, values=self.cb_1_lista, font=('Arial', 10))
            self.cb_1.pack(ipadx=30, ipady=2, padx=2, pady=2)
            self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

            # Todos os formatos em um dicionário
            self.formats = {
                'Arquivos': ['Pastas e outros'],
                'Documentos': ['*.pdf', '*.pptx', '*.txt', '*.cdr', '*.xml', '*.sql', '*.word', '*.doc', '*.docx',
                               '*.rtf', '*.ppt', '*.pps', '*.xls', '*.xlsx', '*.html', '*.dwg'],
                'Executáveis': ['*.exe', '*.msi', '*.bat', '*.bin', '*.com', '*.app', '*.iso'],
                'Imagens': ['*.jpeg', '*.jpg', '*.png', '*.gif', '*.jfif', '*.svg', '*.psd', '*.webp', '*.raw',
                            '*.tiff', '*.bmp'],
                'Compactados': ['*.zip', '*.rar', '*.7z'],
                'Áudios': ['*.mp3', '*.wma', '*.wav', '*.pcm', '*.flac'],
                'Vídeos': ['*.mp4', '*.avi', '*.wmv', '*.mov', '*.flv', '*.f4v', '*.swf', '*.mkv', '*.mpeg-2', '*.mv4']
            }

            self.cb_2 = Combobox(self.frame_2, values=self.cb_2_formats(), font=('Arial', 10))
            self.cb_2.set(self.list_formats[len(self.list_formats) - 1])
            self.cb_2.pack(ipadx=115, ipady=2, pady=2, padx=2)
            self.btn_2 = Button(self.frame_2, image=self.img_anexo, command=self.list_box_anexo, highlightthickness=0,
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

            self.btn_1 = Button(self.frame_1, image=self.img_back, command=self.voltar_adicionar_pastas,
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

            self.run = Button(self.frame_1, image=self.img_next, command=self.inicio_organizacao, highlightthickness=0,
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

            self.btn_3 = Button(self.frame_2, image=self.img_minus, command=self.list_box_desanexar,
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

            self.btn_5 = Button(self.frame_2, image=self.img_information, command=self.information_lb,
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

            self.app.update()

    def inicio_organizacao(self, bag=back_gr):
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

            # Quadro
            self.frame_1 = Frame(self.app, borderwidth=2, relief="solid")
            self.frame_1.configure(bg=bag)
            self.frame_1.pack(ipadx=0, padx=0, pady=0, ipady=50, fill=X, expand=True)

            self.frame_2 = Frame(self.frame_1)
            self.frame_2.configure(bg=bag)
            self.frame_2.pack(ipadx=0, padx=0, pady=0, ipady=0)

            # Itens do Quadro
            self.list_box_1 = Listbox(self.frame_1, bg='#222', fg="#99DD00", font=('Arial', 12))
            self.list_box_1.pack(ipady=150, ipadx=400, padx=5, pady=5, side='bottom')

            self.btn_1 = Button(self.frame_2, bg=bag, image=self.img_back, highlightthickness=0,
                                command=self.voltar_inicio, bd=0)
            self.btn_1.pack(side='top', pady=3, padx=3, ipadx=2, ipady=2)

            def configbgcolor(event):
                self.btn_1.config(bg="#222")
                return event

            def configbgbag(event):
                self.btn_1.config(bg=bag)
                return event

            self.btn_1.bind("<Enter>", configbgcolor)
            self.btn_1.bind("<Leave>", configbgbag)

            self.app.update()

            mb.showinfo(message='As alterações a seguir poderão ser desfeitas caso deseje.')
            # Pegando apenas o nome do diretório
            for carac in range(len(self.direc_padrao) - 1, -1, -1):
                if self.direc_padrao[carac] == '/':
                    self.pasta = self.direc_padrao[carac + 1:]
                    break
            # Question
            self.iniciar = mb.askquestion(title='Atenção', message=f'Iniciar a organização na pasta {self.pasta}?',
                                          icon='question')
            if self.iniciar == 'no':
                mb.showinfo(message='Voltando a tela inicial...')
                self.voltar_inicio()
            else:
                # Trocando as keys dos formatos em self.formats para serem identificadas pelas pastas escritas pelo
                # usuário
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
                self.exec_criar_pastas()
                self.app.update()
                sl(0.5)
                self.list_box_1.insert(END, 'Iniciando a organização...')
                self.app.update()
                sl(0.2)
                if not len(self.backup_cb_lista) == 0:
                    self.exec_organizar()
                else:
                    self.list_box_1.insert(END, '[ERRO] Não existe pasta para iniciar a movimentação de arquivos!')
                    self.list_box_1.configure(fg="#d00")
                    self.app.update()

    # Funções das telas
    def texto_criar_pastas(self):
        texto = 'Tentando criar as pastas: '
        for pos, folder in enumerate(self.backup_cb_lista):
            if folder == self.backup_cb_lista[len(self.backup_cb_lista) - 1]:
                texto = texto + str(self.backup_cb_lista[pos]) + '.'
            elif folder == self.backup_cb_lista[len(self.backup_cb_lista) - 2]:
                texto = texto + str(self.backup_cb_lista[pos]) + ' e '
            else:
                texto = texto + str(self.backup_cb_lista[pos]) + ', '
        return texto

    def key_press(self, event):
        if event.keysym == "Return":
            self.cb_1_adicionar()
        elif event.keysym == "Escape":
            self.cb_1_tirar()

    @staticmethod
    def information_lb():
        return mb.showinfo(message="Selecione as pastas com seus respectivos formatos e clique no botão anexar.")

    def redefinir_pastas(self):
        self.cb_1_lista = list()
        self.cb_1_lista_showdown()
        self.cb_1.config(values=self.cb_1_lista)
        self.cb_1.set('')

    # Listbox config
    def list_box_anexo(self):
        self.val_cb_for = 0
        self.val_cb_fol = 0
        # Análise para ver se os itens estão na lista original
        for folder in self.cb_1_lista:
            if self.cb_1.get() == folder:
                self.val_cb_fol = 1
        for format_ in self.list_formats:
            if self.cb_2.get() == format_:
                self.val_cb_for = 1
        # Validação

        # Caso não tenha nenhuma informação digitada
        if self.cb_1.get() == '' and self.cb_2.get() == '':
            return mb.showwarning(title='Atenção', message='Nenhum formato a ser anexado!!!')
        # Caso os valores forem distintos dos originais dado pelo usuário ou houve alteração de valores no combobox
        elif self.val_cb_for == 0 or self.val_cb_fol == 0 or len(self.cb_1_lista) == 0:
            if len(self.cb_1_lista) == 0:
                return self.cb_1.set(''), self.cb_2.set(''), \
                    mb.showwarning(title='Atenção', message='Formato ou Arquivo inexistente!!!')
            else:
                return self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1]), self.cb_2.set(
                    self.list_formats[len(self.list_formats) - 1]), \
                    mb.showwarning(title='Atenção', message='Formato ou Arquivo inválidos!!!')
        # Caso os valores forem validados conforme o usuário tinha informado
        elif self.val_cb_for == 1 and self.val_cb_fol == 1:
            # Colocando no quadro do Listbox os anexos

            # Caso sejam os últimos a serem anexados
            if len(self.list_formats) and len(self.cb_1_lista) == 1:
                self.list_box_1.insert(END, str(self.cb_1.get()) + ' | ' + str(self.cb_2.get()))
                self.cb_1_lista.remove(self.cb_1.get())
                self.list_formats.remove(self.cb_2.get())
                self.remove_list_box.append([self.cb_1.get(), self.cb_2.get()])
                self.cb_1.config(values=self.cb_1_lista)
                self.cb_2.config(values=self.list_formats)
                self.cb_1.set('')
                self.cb_2.set('')
                self._formats_showdown()
            else:
                self.list_box_1.insert(END, str(self.cb_1.get()) + ' | ' + str(self.cb_2.get()))
                self.cb_1_lista.remove(self.cb_1.get())
                self.list_formats.remove(self.cb_2.get())
                self.remove_list_box.append([self.cb_1.get(), self.cb_2.get()])
                self.cb_1.config(values=self.cb_1_lista)
                self.cb_2.config(values=self.list_formats)
                self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])
                self.cb_2.set(self.list_formats[len(self.list_formats) - 1])
                self._formats_showdown()

    def list_box_desanexar(self):
        # Caso tenha algum item no Listbox
        if len(self.remove_list_box) > 0:
            select = str(self.list_box_1.get(ACTIVE))
            pos = select.index('|')
            folder = select[:pos - 1]
            format_ = select[pos + 2:]
            # Posição do item no remove_list
            for c, v in enumerate(self.remove_list_box):
                for f in self.remove_list_box[c]:
                    if f == folder:
                        pos = c
            # removendo da lista remove_list o item selecionado
            self.remove_list_box.remove(self.remove_list_box[pos])
            # Voltando para lista principal os itens selecionados
            self.cb_1_lista.append(folder)
            self.list_formats.append(format_)
            self.cb_1.config(values=self.cb_1_lista)
            self.cb_2.config(values=self.list_formats)
            self.list_box_1.destroy()
            self.list_box_1 = Listbox(self.frame_1, bg='#222', fg="#99DD00", font=('Arial', 11))
            for fold, form in self.remove_list_box:
                self.list_box_1.insert(END, str(fold) + ' | ' + str(form))
            self.list_box_1.pack(ipady=50, ipadx=180, padx=10, pady=10, side='bottom')
            self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])
            self.cb_2.set(self.list_formats[len(self.list_formats) - 1])
            self._formats_showdown()
        else:
            return mb.showwarning(title='Atenção', message="Nenhum formato a ser desanexado!!")

    # Combobox config
    def cb_2_formats(self):
        if len(self.list_formats) == 0:
            for pos, folder in enumerate(self.formats):
                self.list_formats.append(
                    str(self.formats[str(folder)]).replace('[', '').replace(']', '').replace("'", ''))
            self.backup_cb_formats = [c for c in self.list_formats]
            return self.list_formats
        else:
            return self.list_formats

    def cb_1_exemplo(self):
        self.cb_1_lista = list()
        cb_1_lista = ['Arquivos', 'Documentos', 'Executáveis', 'Imagens', 'Compactados', 'Áudios', 'Vídeos']
        for folder in cb_1_lista:
            self.cb_1_lista.append(folder)
        self.cb_1_lista_showdown()
        self.cb_1.config(values=self.cb_1_lista)
        self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

    def cb_1_adicionar(self):
        selecionado = self.cb_1.get().strip()
        if len(self.cb_1_lista) == 7:
            return mb.showwarning(title="Atenção", message="Limite de pastas atingido!!!"), self.cb_1.set('') if len(
                self.cb_1_lista) == 0 else self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])
        elif len(self.cb_1_lista) > 0:
            for c in self.cb_1_lista:
                if c == selecionado:
                    return mb.showwarning(title="Atenção", message='Pasta ja adicionada!!!'), self.cb_1.set('') if len(
                        self.cb_1_lista) == 0 else self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])
        if selecionado == '':
            return mb.showwarning(title="Atenção", message="Nenhuma pasta foi criada!"), self.cb_1.set('') if len(
                self.cb_1_lista) == 0 else self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])
        else:
            self.cb_1_lista.append(selecionado)
            self.cb_1_lista_showdown()
            self.cb_1.config(values=self.cb_1_lista)
            self.cb_1.set('')

    def cb_1_tirar(self):
        selecionado = self.cb_1.get().strip()
        cont = 0
        for folder in self.cb_1_lista:
            if folder == selecionado:
                self.cb_1_lista.remove(folder)
                self.cb_1_lista_showdown()
                self.cb_1.config(values=self.cb_1_lista)
                self.cb_1.set('') if len(self.cb_1_lista) == 0 else self.cb_1.set(
                    self.cb_1_lista[len(self.cb_1_lista) - 1])
                cont = 1
        if cont == 0:
            mb.showwarning(title="Atenção", message="Pasta inexistente!")
            self.cb_1.set('') if len(self.cb_1_lista) == 0 else self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

    # Voltar
    def voltar_inicio(self):
        self.frame_1.destroy()
        self.frame_2.destroy()
        self.lista_no_move = list()
        self.cb_1_lista = list()
        self.formats = dict()
        self.lista_arq = dict()
        self.reverse_org = dict()
        self.backup_cb_lista = list()
        self.backup_cb_formats = list()
        self.remove_list_box = list()
        self.list_formats = list()
        self.texto_1 = "Pastas: 0"
        self.texto_2 = "Faltam 7 formatos."
        self.btn_github.destroy()
        self.inicio()

    def voltar_escolher_pasta(self):
        self.frame_1.destroy()
        self.frame_2.destroy()
        self.btn_github.destroy()
        self.escolher_pasta()

    def voltar_adicionar_pastas(self):
        self.frame_1.destroy()
        self.frame_2.destroy()
        self.cb_1_lista = [c for c in self.backup_cb_lista]
        self.texto_2 = "Faltam 7 itens."
        self.remove_list_box = list()
        self.btn_github.destroy()
        self.adicionar_pastas()

    # Mostrar formatos que faltam ser anexados
    def _formats_showdown(self):
        cont = len(self.list_formats)
        if cont > 1:
            self.texto_2 = f"Faltam {cont} formatos."
            self._formats_show.config(text=self.texto_2)
        elif cont == 0:
            self.texto_2 = 'Todos os formatos foram anexados.'
            self._formats_show.config(text=self.texto_2)
        else:
            self.texto_2 = f"Falta {cont} formato."
            self._formats_show.config(text=self.texto_2)
        pass

    # Mostrar pastas adicionadas
    def cb_1_lista_showdown(self):
        cont = len(self.cb_1_lista)
        self.texto_1 = f"Pastas: {cont}"
        self.cb_1_lista_show.config(text=self.texto_1)
        pass

    # Capturando diretório
    def direct(self):
        direc_padrao_verify = directory_()

        if direc_padrao_verify != "":
            self.direc_padrao = direc_padrao_verify
            self.direc_show.config(text=self.direc_padrao)
        return self.direc_padrao

    # Exec Back-End
    def exec_criar_pastas(self):
        self.list_box_1.insert(END, 'Começando...')
        self.app.update()
        sl(0.5)
        self.list_box_1.insert(END, self.texto_criar_pastas())
        self.app.update()
        sl(0.3)
        # Criação de pastas
        folder_exists = os.path.exists(self.direc_padrao)  # Verificando a existência da pasta
        if folder_exists:
            # Criando uma lista com os arquivos dentro do diretório escolhido
            self.lista_arq[str(self.pasta)] = os.listdir(self.direc_padrao)
            lista_folders = [c for c in self.backup_cb_lista]
            for folder in lista_folders:
                folder_exists = os.path.exists(os.path.join(self.direc_padrao, folder))
                if not folder_exists:
                    try:
                        os.mkdir(os.path.join(self.direc_padrao, folder))
                    except Exception:
                        self.list_box_1.insert(END, f'[ERRO] Não foi possível criar a pasta "{folder}"')
                else:
                    res = mb.askquestion(
                        icon='warning', message=f'A pasta [{folder}] ja existe, deseja utiliza-la mesmo assim?')
                    if res == 'no':
                        self.backup_cb_lista.remove(folder)
                    else:
                        continue
            # Dicionário onde irá alojar todos os arquivos das pastas, caso elas existam.
            if len(self.backup_cb_formats) != 0:
                for folder in self.backup_cb_lista:
                    self.lista_arq[folder] = os.listdir(os.path.join(self.direc_padrao, folder))
                self.list_box_1.insert(END, 'Completado com êxito!')
                self.app.update()
            else:
                self.list_box_1.configure(fg="#d00")
                self.list_box_1.insert(END, '[ERRO]')
                sl(1)
                mb.showwarning(message='Nenhuma pasta encontrada ou aceita para mover os arquivos.')
                mb.showinfo(message='Voltando a tela inicial...')
                self.voltar_inicio()
        else:
            self.list_box_1.configure(fg="#d00")
            self.list_box_1.insert(END, '[ERRO]')
            sl(1)
            mb.showerror(title='Atenção', message='Diretório inexistente!!!')
            mb.showinfo(message='Voltando a tela inicial...')
            self.direc_padrao = ''
            self.voltar_inicio()

    def exec_organizar(self, bag=back_gr, fog=fore_gr):
        # Arquivos que não devem ser movidos
        self.lista_no_move = ["desktop.ini", "netuser.ini", "Thumbs.db"]
        # Removendo, arquivos que não devem ser movidos, da lista do diretório
        for _file in self.lista_no_move:
            if self.lista_arq[str(self.pasta)].count(_file) != 0:
                self.lista_arq[str(self.pasta)].remove(_file)
            else:
                continue

        # Processo de movimentação de arquivo

        # Colocando as pastas do usuário dentro de um dicionario para que seja possível reverter
        for folder in self.backup_cb_lista:
            self.reverse_org[folder] = []

        # Passando por todos os arquivos do diretório escolhido
        for _file in self.lista_arq[self.pasta]:
            # Validação se o arquivo é compátivel com o formato *.?
            aceito = 0
            for key in self.formats:
                if aceito == 1:
                    break
                else:
                    # Passando por cada formato
                    for m_format in self.formats[key]:
                        if aceito == 1:
                            break
                        elif m_format in 'Pastas e outros':
                            continue
                        else:
                            # Encontrando o último ponto no arquivo selecionado do diretório
                            for pos in range(len(_file) - 1, -1, -1):
                                if '.' in _file[pos]:
                                    # Verificação para ver se depois do ponto é igual ao formato
                                    if _file[pos:] in m_format:
                                        # Movimentando o arquivo
                                        try:
                                            # Caso a pasta exista e ter o mesmo nome de arquivo nela
                                            if os.path.exists(os.path.join(self.direc_padrao, key, _file)) and \
                                                    self.lista_arq[key].count(_file) != 0:
                                                for num in range(1, 100):
                                                    try:
                                                        os.rename(os.path.join(self.direc_padrao, _file),
                                                                  os.path.join(self.direc_padrao, key,
                                                                               f'{_file[:pos]} ({num}){_file[pos:]}'))
                                                        self.list_box_1.insert(END,
                                                                               f'"{_file}" foi movido para a pasta "{key}" e renomeado...')
                                                        self.app.update()
                                                        self.list_box_1.insert(END,
                                                                               f'"{_file[:pos]} ({num}){_file[pos:]}".')
                                                        self.app.update()
                                                        self.reverse_org[key].append(
                                                            f'{_file[:pos]} ({num}){_file[pos:]}')
                                                        sl(0.02)
                                                        break
                                                    except:
                                                        continue
                                            else:
                                                try:
                                                    os.rename(os.path.join(self.direc_padrao, _file),
                                                            os.path.join(self.direc_padrao, key, _file))
                                                    self.list_box_1.insert(END,
                                                                        f'"{_file}" foi movido para a pasta "{key}".')
                                                    self.app.update()
                                                    self.reverse_org[key].append(_file)
                                                    sl(0.02)
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

        # Pegando o restante que sobrou e jogando em uma pasta
        self.lista_arq[self.pasta] = os.listdir(self.direc_padrao)
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
                    self.voltar_inicio()

            except:
                continue

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
                                    self.app.update()
                                    self.list_box_1.insert(END,
                                                           f'"{_file[:pos]} ({num}){_file[pos:]}".')
                                    self.app.update()
                                    self.reverse_org[self.outros_arquivos].append(
                                        f'{_file[:pos]} ({num}){_file[pos:]}')
                                    sl(0.02)
                                    cont = 1
                                    break

                                except Exception:
                                    continue
                        else:
                            try:
                                os.rename(os.path.join(self.direc_padrao, _file),
                                        os.path.join(self.direc_padrao, self.outros_arquivos, _file))
                                self.list_box_1.insert(END, f'"{_file}" foi movido para a pasta "{self.outros_arquivos}".')
                                self.app.update()
                                self.reverse_org[self.outros_arquivos].append(_file)
                                sl(0.02)
                                cont = 1
                            except Exception:
                                self.list_box_1.insert(END, f'[ERRO] Não foi possível mover o arquivo "{_file}" para a pasta "{self.outros_arquivos}".')
                                continue
                    else:
                        continue
                else:
                    break
            
            if cont == 0:
                try:
                    os.rename(os.path.join(self.direc_padrao, _file),
                            os.path.join(self.direc_padrao, self.outros_arquivos, _file))
                    self.list_box_1.insert(END, f'"{_file}" foi movido para a pasta "{self.outros_arquivos}".')
                    self.app.update()
                    self.reverse_org[self.outros_arquivos].append(_file)
                    sl(0.02)
                except Exception:
                    self.list_box_1.insert(END, f'[ERRO] Não foi possível mover o arquivo "{_file}" para a pasta "{self.outros_arquivos}".')
                    continue
            else:
                continue

        if len(self.backup_cb_formats) != 0:
            for folder in self.backup_cb_lista:
                self.lista_arq[folder] = os.listdir(os.path.join(self.direc_padrao, folder))
            self.list_box_1.insert(END, 'Completado com êxito!')
            self.app.update()
        else:
            self.list_box_1.configure(fg="#d00")
            self.list_box_1.insert(END, '[ERRO]')
            sl(1)
            mb.showwarning(message='Nenhuma pasta encontrada ou aceita para mover os arquivos.')
            mb.showinfo(message='Voltando a tela inicial...')
            self.voltar_inicio()

        self.btn_2 = Button(self.frame_2, text='Reverter', command=self.exec_reverter_org, bg=bag, fg=fog, font=(
            'Arial', 10))
        self.btn_2.pack(side='left', padx=4, pady=1, ipady=2, ipadx=2)

        def configbgcolor(event):
            self.btn_2.config(bg="#222")
            return event

        def configbgbag(event):
            self.btn_2.config(bg=bag)
            return event

        self.btn_2.bind("<Enter>", configbgcolor)
        self.btn_2.bind("<Leave>", configbgbag)

    def exec_reverter_org(self):
        res = mb.askquestion(message=f'Tem certeza de que deseja reverter a organização na pasta "{self.pasta}"?')
        if not res == 'no':
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
                                        self.app.update()
                                        sl(0.02)
                                    except Exception:
                                        self.list_box_1.insert(END, f'[ERRO] Não foi possível retornar o arquivo "{_file}" para a pasta "{self.pasta}".')
                        else:
                            os.rename(os.path.join(self.direc_padrao, key, _file),
                                      os.path.join(self.direc_padrao, _file))
                            self.list_box_1.insert(END, f'"{_file}" retornou a pasta "{self.pasta}".')
                            self.app.update()
                            sl(0.02)
                    else:
                        self.list_box_1.insert(END, f'"{_file}" não existe mais na pasta "{self.pasta}".')
                        self.app.update()

            for key in self.reverse_org:
                for _file in self.reverse_org[key]:
                    self.reverse_org[key].remove(_file)

            def text_message():
                cont = 0
                texto = 'Deseja apagar as pastas "'
                for _folder in self.backup_cb_lista:
                    self.lista_arq[_folder] = os.listdir(os.path.join(self.direc_padrao, _folder))
                    if len(self.lista_arq[_folder]) == 0:
                        cont += 1
                        if not self.backup_cb_lista[len(self.backup_cb_lista) - 1] == _folder:
                            texto += _folder + ', '
                        else:
                            texto += _folder + '" que não contém arquivos?'
                    else:
                        self.backup_cb_lista.remove(_folder)
                if cont != 0:
                    question = mb.askquestion(message=texto)
                    return question
                else:
                    return ''

            res = text_message()
            if res == 'yes':
                for folder in self.backup_cb_lista:
                    try:
                        if os.path.exists(os.path.join(self.direc_padrao, folder)) and len(os.listdir(
                                os.path.join(self.direc_padrao, folder))) == 0:
                            os.rmdir(os.path.join(self.direc_padrao, folder))
                            self.list_box_1.insert(END, f'Apagando a pasta "{folder}".')
                            self.app.update()
                        else:
                            continue
                    except OSError:
                        self.list_box_1.insert(END, f'Não foi possível apagar a pasta "{folder}".')
                        self.app.update()
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


# Home
if __name__ == '__main__':
    Start()
