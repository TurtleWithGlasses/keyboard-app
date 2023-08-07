import tkinter as tk

keyboard_app = tk.Tk()

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "=",
        "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "DEL",
        "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "''",
        "z", "x", "c", "v", "b", "n", "m", ",", ".", "!", "TAB",
        "SPACE"]

current_button = [-1, -1]
button_L = [[]]
entry = tk.Text(keyboard_app, width=97, height=8)
entry.grid(row=0, columnspan=15)

var_row = 1
var_column = 0

