import os #import the os module to rename files
from Tkinter import * # for gui

def show():
    global name
    name = e1.get()

OPTIONS = [
    "mp4",
    "avi",
    "mkv",
]

master = Tk()

Label(master, text="Name").grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)

Button(master, text='Set Name', command=master.quit).grid(row=3, column=0, sticky=W, pady=2)
Button(master, text='Rename Files', command=show).grid(row=3, column=1, sticky=W, pady=2)

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

dropdown = apply(OptionMenu, (master, variable) + tuple(OPTIONS))
dropdown.grid(row=2, column=0)

mainloop()

path = '.';  #initialise the path with the current directory.

x = 0
i = 1;
files = os.listdir(path);
for file in files:
    if file.startswith('dropdown'):
        continue;
    if i <= 9:
        os.rename(file, name + str(x) + str(i) + '.' + variable.get()); #to rename file
    else:
        os.rename(file, name  + str(i) + '.' + variable.get()); #to rename file
    i += 1
