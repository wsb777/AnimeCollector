from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()