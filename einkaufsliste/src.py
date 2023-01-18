import tkinter as tk
from tkinter import ttk


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.geometry("880x690")

        for F in (Einkaufsliste, Liste_Erstellen, Ältere_Listen):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0)

        self.show_frame(Einkaufsliste)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Einkaufsliste(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Einkaufsliste")
        button1 = ttk.Button(self, text="Liste erstellen",
                             command=lambda:
                             controller.show_frame(Liste_Erstellen))
        button2 = ttk.Button(self, text="Ältere Listen",
                             command=lambda:
                             controller.show_frame(Ältere_Listen))

        label.grid(row=0, column=1, padx=10, pady=10)
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2.grid(row=2, column=1, padx=10, pady=10)


class Liste_Erstellen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Liste Erstellen")
        back_button = ttk.Button(self, text="zurück",
                                 command=lambda:
                                 controller.show_frame(Einkaufsliste))

        label.grid(row=0, column=1, padx=10, pady=10)
        back_button.grid(row=1, column=1, padx=10, pady=10)


class Ältere_Listen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Ältere Listen")
        back_button = ttk.Button(self, text="zurück",
                                 command=lambda:
                                 controller.show_frame(Einkaufsliste))

        label.grid(row=0, column=1, padx=10, pady=10)
        back_button.grid(row=1, column=1, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
