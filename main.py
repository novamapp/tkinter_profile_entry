import tkinter as tk
from tkinter import ttk

class Entry_Form(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('User Profile Entry Form')
        self.geometry('640x480')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        Profile_Frame(self).grid(row=0, column=0, sticky='ns')
        Profile_Entry_Frame(self).grid(row=0, column=1, sticky='ns')

class Profile_Frame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)

        label = ttk.Label(self, text="placeholder")
        label.pack()

class Profile_Entry_Frame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)

        label = ttk.Label(self, text="placeholder")
        label.pack()


Entry_Form().mainloop()