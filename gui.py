from tkinter import *
import tkinter as tk
from button_func import *
from Model import Model
from PetTypes import PetTypes
# from tkinter import filedialog, Text, RIGHT, BOTH, LEFT

import os

root = tk.Tk()
root.title("Tamagotchi")


canvas = tk.Canvas(root, height = 400, width=400, bg = "#038cfc")
canvas.grid(row = 0,columnspan =4)
print(canvas.winfo_height())

frame = tk.Frame(root, bg="white")
frame.grid(row=1,columnspan =4)

model = Model(PetTypes.ANIMAL_A)
model.canvas = canvas

# frame.place(relwidth = 0.8, relheight=0.8, relx = 0.1, rely = 0.1)
# frame.grid(row = 0, column = 0)
# frame.grid()


b1 = tk.Button(root,text = "Feed", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:feedAction(model), borderwidth=0)

b2 = tk.Button(root,text = "Walk", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:walkAction(model), borderwidth=0)

b3 = tk.Button(root,text = "Pet", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:petAction(model))

b4 = tk.Button(root,text = "Connect", padx = 10, pady =10, fg ="white", bg="#038cfc", command = connectAction, borderwidth=0)



b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)
b3.grid(row = 2, column = 2)
b4.grid(row = 2, column = 3)

root.update_idletasks()
my_image = PhotoImage(file = "./photos/newLongNeck.png")

width = canvas.winfo_width()/2
height = canvas.winfo_height()/2

print(width)
print(height)

canvas.create_image(width, height, image=my_image, anchor = CENTER)



# root.after(1000, model.update)
 
root.mainloop()

