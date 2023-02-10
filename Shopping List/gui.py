import tkinter as tk
from tkinter import ttk
from functions import Functions


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Shopping_List, ShoppingLists, Create_List, Products,
                  Create_Product):
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

        mainlabel = ttk.Label(self, text="Shopping List", font=(
                              'Helvetica bold', 15))
        button1 = ttk.Button(self, text="Lists",
                             command=lambda:
                             controller.show_frame(ShoppingLists))
        button2 = ttk.Button(self, text="Products",
                             command=lambda:
                             controller.show_frame(Products))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        button1.grid(row=1, column=1, padx=(100, 100), pady=(10, 10))
        button2.grid(row=2, column=1, padx=(100, 100), pady=(10, 80))


class ShoppingLists(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Shopping_Lists = Functions.read_shopping_lists()
        list_names = [list.Name for list in Shopping_Lists]

        mainlabel = ttk.Label(self, text="Lists", font=(
                              'Helvetica bold', 15))
        create_list_button = ttk.Button(self, text="Create List",
                                        command=lambda: controller.show_frame
                                        (Create_List))

        for i, list_name in enumerate(list_names):
            list_buttons = ttk.Button(self, text=list_name)
            list_buttons.grid(row=2+i, column=1)

        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        create_list_button.grid(row=1, column=1, padx=(0, 0), pady=(10, 10))
        back_button.grid(row=3+i, column=1, padx=(100, 100), pady=(10, 80))


class ListButton(ttk.Button):
    def __init__(self, Name, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.Name = Name
        self.config(command=lambda: print(Name))


class Create_List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text="Create List", font=(
                              'Helvetica bold', 15))
        label1 = ttk.Label(self, text="List Name")
        entry1 = ttk.Entry(self, width=10)
        label2 = ttk.Label(self, text="List Date")
        entry2 = ttk.Entry(self, width=10)
        create_button = ttk.Button(self, text="Create", command=lambda:
                                   [Functions.create_shopping_list
                                    (entry1.get(), entry2.get()),
                                    controller.show_frame(ShoppingLists),
                                    entry1.delete(0, 100),
                                    entry2.delete(0, 100)])
        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(ShoppingLists))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        label1.grid(row=1, column=1, padx=(100, 100), pady=(10, 0))
        entry1.grid(row=2, column=1, padx=(0, 0), pady=(0, 10))
        label2.grid(row=3, column=1, padx=(100, 100), pady=(10, 0))
        entry2.grid(row=4, column=1, padx=(0, 0), pady=(0, 10))
        create_button.grid(row=5, column=1, padx=(0, 0), pady=(10, 10))
        back_button.grid(row=6, column=1, padx=(100, 100), pady=(10, 80))


class Products(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Products = Functions.read_products()
        product_names = [product.Name for product in Products]

        mainlabel = ttk.Label(self, text="Products", font=(
                              'Helvetica bold', 15))

        create_product_button = ttk.Button(self, text="Create Product",
                                           command=lambda: controller.
                                           show_frame(Create_Product))

        for i, product_name in enumerate(product_names):
            product_buttons = ttk.Button(self, text=product_name)
            product_buttons.grid(row=2+i, column=1)

        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Shopping_List))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        create_product_button.grid(row=1, column=1, padx=(0, 0), pady=(10, 10))
        back_button.grid(row=3+i, column=1, padx=(100, 100), pady=(10, 80))


class Create_Product(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text="Create List", font=(
                              'Helvetica bold', 15))
        label1 = ttk.Label(self, text="Product Name")
        entry1 = ttk.Entry(self, width=10)
        label2 = ttk.Label(self, text="Product Volume in l")
        entry2 = ttk.Entry(self, width=10)
        label3 = ttk.Label(self, text="Product Weight in g")
        entry3 = ttk.Entry(self, width=10)
        create_button = ttk.Button(self, text="Create", command=lambda:
                                   [Functions.create_product
                                    (entry1.get(), entry2.get(), entry3.get()),
                                    controller.show_frame(Products),
                                    entry1.delete(0, 100), entry2.delete(0,
                                                                         100),
                                    entry3.delete(0, 100)])

        back_button = ttk.Button(self, text="Back",
                                 command=lambda:
                                 controller.show_frame(Products))

        mainlabel.grid(row=0, column=1, padx=(0, 0), pady=(80, 10))
        label1.grid(row=1, column=1, padx=(100, 100), pady=(10, 0))
        entry1.grid(row=2, column=1, padx=(0, 0), pady=(0, 10))
        label2.grid(row=3, column=1, padx=(100, 100), pady=(10, 0))
        entry2.grid(row=4, column=1, padx=(0, 0), pady=(0, 10))
        label3.grid(row=5, column=1, padx=(100, 100), pady=(10, 0))
        entry3.grid(row=6, column=1, padx=(0, 0), pady=(0, 10))
        create_button.grid(row=7, column=1, padx=(0, 0), pady=(10, 10))
        back_button.grid(row=8, column=1, padx=(100, 100), pady=(10, 80))


class List(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        products = Functions.read_products()
        product_names = [product.Name for product in products]
        product_volumes = [product.Volume_in_l for product in products]
        product_weights = [product.Weight_in_g for product in products]

        mainlabel = ttk.Label(self, text="1")
        for i, list_name in enumerate(product_names):
            product_name_labels = ttk.Button(self, text=list_name)
            product_name_labels.grid(row=1+i, column=1)
        for i, list_volume in enumerate(product_volumes):
            product_volume_labels = ttk.Button(self, text=list_volume)
            product_volume_labels.grid(row=2+i, column=1)
        for i, list_weight in enumerate(product_weights):
            product_weight_labels = ttk.Button(self, text=list_weight)
            product_weight_labels.grid(row=2+i, column=1)

        mainlabel.grid(row=0, column=1)


app = tkinterApp()
app.mainloop()
