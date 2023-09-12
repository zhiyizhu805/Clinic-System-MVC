import tkinter as tk
from tkinter import ttk
# create a new window
root = tk.Tk()
root.title('My First GUI')

def button_clicked():
    print('Button Clicked!')

# place a label to the root window
lalHello = ttk.Label(root,text="Hello there!")
lalHello.pack()

# place a button
btnClick = ttk.Button(root,text="Click me!",command = button_clicked)
btnClick.pack()
root.mainloop()

