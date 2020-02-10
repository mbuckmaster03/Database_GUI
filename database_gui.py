#!/usr/bin/python3
# Matthew Buckmaster
# 2/10/2020

"""GUI version of game_database.py"""

import pickle

import tkinter as tk

from tkinter import scrolledtext

TITLE_FONT = ("Times New Roman", 24)

BOTTOM_FONT = ("Arial", 15)





#Main
if __name__ == "__main__":

    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
    data_file.close()

