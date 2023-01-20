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

        for F in (Shopping_List, Create_List, Older_Lists):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0)

        self.show_frame(Shopping_List)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Shopping_List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Shopping List")
        button1 = ttk.Button(self, text="Create List",
                             command=lambda:
                             controller.show_frame(Create_List))
        button2 = ttk.Button(self, text="Older Lists",
                             command=lambda:
                             controller.show_frame(Older_Lists))

        label.grid(row=0, column=1, padx=(100, 100), pady=(100, 10))
        button1.grid(row=1, column=1, padx=(100, 100), pady=(10, 10))
        button2.grid(row=2, column=1, padx=(100, 100), pady=(10, 100))


class Create_List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Create List")
        entry1 = ttk.Entry(self)
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        label.grid(row=0, column=1, padx=50, pady=10)
        entry1.grid(row=1, column=1, padx=0, pady=10)
        back_button.grid(row=2, column=1, padx=50, pady=10)


class Older_Lists(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Older Lists")
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        label.grid(row=0, column=1, padx=50, pady=10)
        back_button.grid(row=1, column=1, padx=50, pady=10)


app = tkinterApp()
app.mainloop()
