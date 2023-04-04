from tkinter.filedialog import askdirectory as directory_
from tkinter import messagebox as mb

def direct(self):
        direc_padrao_verify = directory_()
        if direc_padrao_verify != "":
            self.direc_padrao = direc_padrao_verify
            self.direc_show.config(text=self.direc_padrao)
        return self.direc_padrao

def cb_1_exemplo(self):
    self.cb_1_lista = ['Arquivos', 'Documentos', 'Executáveis', 'Imagens', 'Compactados', 'Áudios', 'Vídeos']
    cb_1_lista_show(self)
    self.cb_1.config(values=self.cb_1_lista)
    self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

def cb_1_adicionar(self):
    selecionado = self.cb_1.get().strip()
    if len(self.cb_1_lista) == 7:
        return mb.showwarning(title="Atenção", message="Limite de pastas atingido!!!"), self.cb_1.set('') 
    elif len(self.cb_1_lista) > 0:
        for c in self.cb_1_lista:
            if c == selecionado:
                return mb.showwarning(title="Atenção", message='Pasta ja adicionada!!!'), self.cb_1.set('')
    if selecionado == '':
        return mb.showwarning(title="Atenção", message="Nenhuma pasta foi criada!"), self.cb_1.set('') 
    else:
        self.cb_1_lista.append(selecionado)
        cb_1_lista_show(self)
        self.cb_1.config(values=self.cb_1_lista)
        self.cb_1.set('')

def cb_1_tirar(self):
    selecionado = self.cb_1.get().strip()
    cont = 0
    for folder in self.cb_1_lista:
        if folder == selecionado:
            self.cb_1_lista.remove(folder)
            cb_1_lista_show(self)
            self.cb_1.config(values=self.cb_1_lista)
            self.cb_1.set('') if len(self.cb_1_lista) == 0 else self.cb_1.set(
                self.cb_1_lista[len(self.cb_1_lista) - 1])
            cont = 1
    if cont == 0:
        mb.showwarning(title="Atenção", message="Pasta inexistente!")
        self.cb_1.set('') if len(self.cb_1_lista) == 0 else self.cb_1.set(self.cb_1_lista[len(self.cb_1_lista) - 1])

def cb_1_lista_show(self):
    cont = len(self.cb_1_lista)
    self.texto_1 = f"Pastas: {cont}"
    self.cb_1_lista_show.config(text=self.texto_1)
    pass

def redefinir_pastas(self):
    self.cb_1_lista = list()
    cb_1_lista_show(self)
    self.cb_1.config(values=self.cb_1_lista)
    self.cb_1.set('')
