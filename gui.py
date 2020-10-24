import tkinter as tk
from tkinter import filedialog, Text, RIGHT, BOTH, LEFT
import os

root = tk.Tk()
root.title("Tamagotchi")

def addApp():
    print("HI :)")
    
canvas = tk.Canvas(root, height = 700, width=700, bg = "#038cfc")
canvas.grid(row = 0, columnspan =4)

frame = tk.Frame(root, bg="white")
frame.grid(row=1,columnspan =4)


# frame.place(relwidth = 0.8, relheight=0.8, relx = 0.1, rely = 0.1)
# frame.grid(row = 0, column = 0)
# frame.grid()

b1 = tk.Button(root,text = "Feed", padx = 10, pady =5, fg ="white", bg="#038cfc", command = addApp)
# left.pack(side = RIGHT)



b2 = tk.Button(root,text = "Walk", padx = 10, pady =5, fg ="white", bg="#038cfc")
# middle.pack()


# second_middle.pack()

b3 = tk.Button(root,text = "Pet", padx = 10, pady =5, fg ="white", bg="#038cfc")
# right.pack(side = LEFT)

b4 = tk.Button(root,text = "Connect", padx = 10, pady =5, fg ="white", bg="#038cfc")



b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)
b3.grid(row = 2, column = 2)
b4.grid(row = 2, column = 3)






 
root.mainloop()
