#!/usr/bin/python3
# Matthew Buckmaster
# 2/10/2020

"""GUI version of game_database.py"""

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", 24)

BOTTOM_FONT = ("Arial", 15)

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_add = tk.Button(text = "Add", font = BOTTOM_FONT)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_add = tk.Button(text = "Edit", font = BOTTOM_FONT)
        self.btn_add.grid(row = 2, column = 0)
        self.btn_add = tk.Button(text = "Serach", font = BOTTOM_FONT)
        self.btn_add.grid(row = 3, column = 0)
        self.btn_add = tk.Button(text = "Remove", font = BOTTOM_FONT)
        self.btn_add.grid(row = 4, column = 0)
        self.btn_add = tk.Button(text = "Save", font = BOTTOM_FONT)
        self.btn_add.grid(row = 5, column = 0)        


#Main
if __name__ == "__main__":

    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
    data_file.close()
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0)
    
    
    
    root.mainloop()

