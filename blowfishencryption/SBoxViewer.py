import tkinter as tk

class SBoxViewer(tk.Frame):
    def __init__(self, parent, s_box,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
