from tkinter import*
import tkinter as tk
from button_func import *
# from tkinter import filedialog, Text, RIGHT, BOTH, LEFT

import os

root = tk.Tk()
root.title("Menu Select")
root.geometry("400x400")


# canvas = tk.Canvas(root, height = 400, width=400, bg = "#038cfc")
# canvas.grid(row = 0,columnspan =4)
# print(canvas.winfo_height())

#frame = tk.Frame(root, bg="white")
# frame.grid(row=1,columnspan =4)




# frame.place(relwidth = 0.8, relheight=0.8, relx = 0.1, rely = 0.1)
# frame.grid(row = 0, column = 0)
# frame.grid()

b1 = tk.Button(root,text = "Sharp teeth", padx = 10, pady =10, fg ="white", bg="#038cfc", command = selectTrex)

b2 = tk.Button(root,text = "3-horn", padx = 10, pady =10, fg ="white", bg="#038cfc", command = select3Horn)

b3 = tk.Button(root,text = "Long neck", padx = 10, pady =10, fg ="white", bg="#038cfc", command = selectLongNeck)



b1.place(relx=0.0, rely=0.0, anchor=CENTER)
b2.place(relx=0.5, rely=0.0, anchor=CENTER)
b3.place(relx=1.0, rely=0.0, anchor=CENTER)



root.update_idletasks()
# my_image = PhotoImage(file = "./photos/trexfull.png")

# width = canvas.winfo_width()/2
# height = canvas.winfo_height()/2

# print(width)
# print(height)

# canvas.create_image(width, height, image=my_image, anchor = CENTER)




 
root.mainloop()
