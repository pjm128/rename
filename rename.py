import os #import the os module
from Tkinter import *
def show(): 
    global name
    global file_type
    name = e1.get()
    file_type = e2.get()

master = Tk()
Label(master, text="name").grid(row=0)
Label(master, text="file type").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Set Name', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Rename Files', command=show).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
path = '.';  #initialise the path with the current directory.

x = 0
i = 1;
files = os.listdir(path);
for file in files:
    if file.startswith('rename'):
        continue;
    if i <= 9:
        os.rename(file, name + str(x) + str(i) + '.' + file_type); #to rename file
    else:
        os.rename(file, name  + str(i) + '.' + file_type); #to rename file
    i += 1
