from tkinter import Tk, Button, Canvas, BOTH, TOP, Label, Entry, CENTER, LEFT
import threading
from loadconfig_save import escrever, ler
from rodape_oficial_html import montar_placares


class Janela:

    def __init__(self):
        self.window = Tk()
        self.window.title("Pog Overlay")
        self.window.iconbitmap(r"Icon\icon.ico")
        self.menus_center = self.menu_botton = self.entry = self.news = self.menus_top = \
            self.timer_placar = self.timer_sleep = self.configs_txt = self.rodando = self.button1 = None

        self.up = False

        self.window.geometry("500x250")
        self.window.eval('tk::PlaceWindow . center')
        self.window.resizable(width=False, height=False)

        self.window.rowconfigure([0, 1], minsize=50, weight=1)

        self.window.columnconfigure([0, 1], minsize=50, weight=1)

        self.telas()

        self.entry_link()
        self.button()
        self.label_info_status()
        self.configura()

        self.window.mainloop()

    def telas(self):
        self.menus_top = Canvas(bg="#023047", width=350, height=50, master=self.window)
        self.menus_top.pack(side=TOP, fill=BOTH)

        label = Label(self.menus_top, text="Gerador de Placares", font=('helvetica', 16, 'bold'), bg="#023047",
                      fg="#ffb703")
        label.place(anchor=CENTER, relx=0.5, rely=0.5)

        self.menus_center = Canvas(bg="#219ebc", width=350, height=50,
                                   master=self.window)
        self.menus_center.pack(side=TOP, fill=BOTH)

        self.menu_botton = Canvas(bg="#8ecae6", width=350, height=150, master=self.window)
        self.menu_botton.pack(side=TOP, fill=BOTH)

    def entry_link(self):
        label = Label(self.menus_center, text="Link EVENTO AQUI:", font=('helvetica', 9, 'bold'), bg="#219ebc")
        label.place(anchor=CENTER, relx=0.15, rely=0.5)
        self.entry = Entry(self.menus_center, width=50)
        self.entry.place(anchor=CENTER, relx=0.60, rely=0.5)

    def button(self):
        self.button1 = Button(master=self.menu_botton, command=self.parar_up,
                              text='Começar a gerar e atualizar placares', bg='brown', fg='white',
                              font=('helvetica', 9, 'bold'))
        self.button1.place(anchor=CENTER, relx=0.72, rely=0.85)

        button2 = Button(master=self.menu_botton, command=self.salvar_config,
                         text='Salvar config', bg='brown', fg='white',
                         font=('helvetica', 9, 'bold'))
        button2.place(anchor=CENTER, relx=0.15, rely=0.85)

    def label_info_status(self):
        self.news = Label(self.menu_botton, text="Nenhum Evento colocado", font=('helvetica', 9, 'bold'), bg="#8ecae6")
        self.news.place(anchor=CENTER, relx=0.70, rely=0.5)

    def configura(self):
        label_ = Label(self.menu_botton, text="Intervalo entre placares (ms):",
                       font=('helvetica', 9, 'bold'), bg="#8ecae6",
                       justify=LEFT)
        label_.place(anchor="w", relx=0.01, rely=0.15)
        label_ = Label(self.menu_botton, text="Intervalo de atualização (ms):",
                       font=('helvetica', 9, 'bold'), bg="#8ecae6",
                       justify=LEFT)
        label_.place(anchor="w", relx=0.01, rely=0.35)

        config_txt = ler()

        self.configs_txt = Label(self.menu_botton, text=f"Intervalo de atualização atual: {config_txt['sleep']}ms\n"
                                                        f"Intervalo entre placares atual: {config_txt['placares']}ms",
                                 font=('helvetica', 9, 'bold'), bg="#8ecae6", justify=LEFT)
        self.configs_txt.place(anchor="w", relx=0.01, rely=0.57)

        self.timer_placar = Entry(self.menu_botton, width=5)
        self.timer_placar.place(anchor="w", relx=0.38, rely=0.15)
        self.timer_sleep = Entry(self.menu_botton, width=5)
        self.timer_sleep.place(anchor="w", relx=0.38, rely=0.35)

    def make_image(self):

        app = montar_placares(self.entry.get())
        self.news.config(text=app)
        self.button1.config(text="Parar atualização", command=self.parar)
        self.window.update()
        configs = ler()
        self.rodando = self.window.after(configs["sleep"], self.parar_up)

    def thredad1(self):
        thre1 = threading.Thread(target=self.make_image)
        thre1.start()

    def salvar_config(self):

        config = escrever(sleep=self.timer_sleep.get(), placares=self.timer_placar.get())

        self.configs_txt.config(text=f"Intervalo de atualização atual: {config['sleep']} ms\n"
                                     f"Intervalo entre placares atual: {config['placares']} ms")

        self.window.update()

    def parar_up(self):

        if self.up:
            self.up = False
            self.window.after_cancel(self.rodando)
            self.button1.config(text="Começar a gerar e atualizar placares", command=self.parar_up)
            self.news.config(text="Atualização parada!")
            self.window.update()

        else:

            self.thredad1()

    def parar(self):
        self.up = True
        self.parar_up()
