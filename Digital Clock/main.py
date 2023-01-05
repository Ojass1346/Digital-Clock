from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title("Test_Window")
root.geometry('700x700')

Label(root, text="Player 1").grid(row=0,column=1)
Label(root, text = "Player 2").grid(row=0, column=2)

root.mainloop()