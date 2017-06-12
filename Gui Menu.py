from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Simple Web Gui Menu -- Thomas Nguyen")


def newFile():
    tkinter.messagebox.showinfo("New File", "It will create a new file scenario")


def openFile():
    tkinter.messagebox.showinfo("Open File", "It will open a file of your choosing scenario")


def about():
    tkinter.messagebox.showinfo("About", "This is a simple web gui menu in Python")


menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New ", command = newFile)
filemenu.add_command(label = "Open File", command = openFile)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)

helpMenu = Menu(menu)
menu.add_cascade(label = "HELP ME PLEASE!", menu = helpMenu)
helpMenu.add_command(label = "About", command = about)



root.mainloop()
