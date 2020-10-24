import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def addApp():
    print("HI :)")
    
canvas = tk.Canvas(root, height = 700, width=700, bg = "#038cfc")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.8, relheight=0.8, relx = 0.1, rely = 0.1)


left = tk.Button(root,text = "Right", padx = 10, pady =5, fg ="white", bg="#038cfc", command = addApp)
left.pack()

middle = tk.Button(root,text = "Middle", padx = 10, pady =5, fg ="white", bg="#038cfc")
middle.pack()

right = tk.Button(root,text = "Left", padx = 10, pady =5, fg ="white", bg="#038cfc")
right.pack()



 
root.mainloop()
