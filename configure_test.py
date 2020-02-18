#!/usr/bin/python3
# Matthew Buckmaster
# 2/10/2020


import tkinter as tk

class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.btn_back = tk.Button(self, text = "Back")
        self.btn_back.grid(row = 0, column = 0)
        self.btn_back = tk.Button(self, text = "Frontttttttttttt")
        self.btn_back.grid(row = 1, column = 0)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        
root = tk.Tk
root.geometry("200 x 100")
app = App()
app.grid(row = 0, column = 0)
root.grid_columnconfigure(0, weight = 1)

root.mainloop()