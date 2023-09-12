import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pack Demo")
root.geometry("300x200")

# place widgets top down
label1 = tk.Label(
    root,
    text="Box 1",
    bg="red",
    fg="white"
)
label1.pack(
    ipadx=10,
    ipady=10,
    fill="x"
)


root.mainloop()