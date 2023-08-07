import tkinter as tk

keyboard_app = tk.Tk()
keyboard_app.title("Practical Keyboard")

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


def left_key(event):
    if current_button == [-1, -1]:
        current_button[:] = [0,0]
        button_L[0][0].configure(highlightbackground="red")
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [0, 10]
        button_L[0][10].configure(highlightbackground="red")
    else:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [current_button[0], (current_button[1]-1)%11]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    button_L[current_button[0]][current_button[1]].focus_set()

def right_key(event):
    if current_button == [-1, -1]:
        current_button[:] = [0,0]
        button_L[0][0].configure(highlightbackground="red")
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [0, 0]
        button_L[0][10].configure(highlightbackground="red")
    else:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [current_button[0], (current_button[1]+1)%11]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    button_L[current_button[0]][current_button[1]].focus_set()

def up_key(event):
    if current_button == [-1, -1]:
        current_button[:] = [0,0]
        button_L[0][0].configure(highlightbackground="red")
    elif current_button[0] == 0:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]-1)%5, 0]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]-1)%5, 0]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    else:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]-1)%5, current_button[1]]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    button_L[current_button[0]][current_button[1]].focus_set()


def down_key(event):
    if current_button == [-1, -1]:
        current_button[:] = [0,0]
        button_L[0][0].configure(highlightbackground="red")
    elif current_button[0] == 3:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]+1)%5, 0]
        button_L[current_button[0]][current_button[1]%11].configure(highlightbackground="red")
    elif current_button[0] == 4:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]+1)%5, 5]
        button_L[current_button[0]][current_button[1]%11].configure(highlightbackground="red")
    else:
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
        current_button[:] = [(current_button[0]+1)%5, current_button[1]]
        button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
    button_L[current_button[0]][current_button[1]].focus_set()


def select(value, x, y):
        if current_button != [-1, -1]:
                button_L[current_button[0]][current_button[1]].configure(highlightbackground="red")
                button_L[current_button[0]][current_button[1]].configure(highlightcolor="red")
        current_button[:] = [x, y]
        button_L[x][y].configure(highlightbackground="red")
        button_L[x][y].configure(highlightcolor="red")

        if value == "DEL":
                input_value = entry.get("1.0", "end-2c")
                entry.delete("1.0", "end")
                entry.insert("1.0", input_value, "end")
        elif value == "SPACE":
                entry.insert("insert", " ")
        elif value == "TAB":
                entry.insert("insert", "    ")
        else:
                entry.insert("end", value)


for button in keys:
        if button != "SPACE":
                but = tk.Button(keyboard_app, text=button, width=5, bg="gray", fg="black",
                                highlightthickness=4, activebackground="light gray", activeforeground="dark gray",
                                highlightcolor="red", relief="raised", padx=12, pady=4, bd=4,
                                command=lambda x=button, i=var_row-1, j=var_column: select(x,i,j))
                but.bind("<Return>", lambda event, x=button, i=var_row-1,j=var_column: select(x,i,j))
                button_L[var_row-1].append(but)
                but.grid(row=var_row, column=var_column)


        if button == "SPACE":
            but = tk.Button(keyboard_app, text=button, width=60, bg="gray", fg="black",
                            highlightthickness=4, activebackground="light gray", activeforeground="dark gray",
                            highlightcolor="red", relief="raised", padx=4, pady=4, bd=4,
                            command=lambda x=button, i=var_row - 1,
                                           j=var_column: select(x, i, j))
            but.bind("<Return>", lambda event, x=button, i=var_row - 1, j=var_column: select(x, i, j))
            button_L[var_row - 1].append(but)
            but.grid(row=6, columnspan=16)

        var_column += 1
        if var_column > 10:
            var_column = 0
            var_row += 1
            button_L.append([])

keyboard_app.bind("<Left>", left_key)
keyboard_app.bind("<Right>", right_key)
keyboard_app.bind("<Up>", up_key)
keyboard_app.bind("<Down>", down_key)


keyboard_app.mainloop()