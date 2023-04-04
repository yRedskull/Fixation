from tkinter import *
from tkinter import messagebox as mb


def list_box_anexo(self):
    val_cb_for = 0
    val_cb_fol = 0

    for folder in self.cb_1_lista:
        if self.cb_1.get() == folder:
            val_cb_fol = 1
    for format_ in self.list_formats:
        if self.cb_2.get() == format_:
            val_cb_for = 1

    if self.cb_1.get() == '' and self.cb_2.get() == '':
        return mb.showwarning(title='Atenção', message='Nenhum formato a ser anexado!!!')
    elif val_cb_for == 0 or val_cb_fol == 0 or len(self.cb_1_lista) == 0:
        if len(self.cb_1_lista) == 0:
            return self.cb_1.set(''), self.cb_2.set(''), \
                mb.showwarning(title='Atenção', message='Formato ou Arquivo inexistente!!!')
        else:
            return self.cb_1.set(self.cb_1_lista[-1]), self.cb_2.set(
                self.list_formats[-1]), \
                mb.showwarning(title='Atenção', message='Formato ou Arquivo inválidos!!!')
    elif val_cb_for == 1 and val_cb_fol == 1:
        if len(self.list_formats) and len(self.cb_1_lista) == 1:
            self.list_box_1.insert(END, str(self.cb_1.get()) + ' | ' + str(self.cb_2.get()))
            self.cb_1_lista.remove(self.cb_1.get())
            self.list_formats.remove(self.cb_2.get())
            self.remove_list_box.append([self.cb_1.get(), self.cb_2.get()])
            self.cb_1.config(values=self.cb_1_lista)
            self.cb_2.config(values=self.list_formats)
            self.cb_1.set('')
            self.cb_2.set('')
            show_formats(self)
        else:
            self.list_box_1.insert(END, str(self.cb_1.get()) + ' | ' + str(self.cb_2.get()))
            self.cb_1_lista.remove(self.cb_1.get())
            self.list_formats.remove(self.cb_2.get())
            self.remove_list_box.append([self.cb_1.get(), self.cb_2.get()])
            self.cb_1.config(values=self.cb_1_lista)
            self.cb_2.config(values=self.list_formats)
            self.cb_1.set(self.cb_1_lista[-1])
            self.cb_2.set(self.list_formats[-1])
            show_formats(self)

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
        self.cb_1.set(self.cb_1_lista[-1])
        self.cb_2.set(self.list_formats[-1])
        show_formats(self)
    else:
        return mb.showwarning(title='Atenção', message="Nenhum formato a ser desanexado!!")


def show_formats(self):
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
