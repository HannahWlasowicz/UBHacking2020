from tkinter import *
import tkinter as tk
from tkinter import font as tkfont
from button_func import *
from Model import Model

import os

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.model = Model("long_boi")
            self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

            self.title("Dion Nuggies")

            # the container is where we'll stack a bunch of frames
            # on top of each other, then the one we want visible
            # will be raised above the others
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (StartPage, MainPage):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("StartPage")

            

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def updateApp(self):
        self.model.update()
        self.after(1000, self.updateApp)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pick your starter pet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        b1 = tk.Button(self,text = "Sharp teeth", padx = 10, pady =10, fg ="white", bg="#038cfc", command = lambda:selectTrex(self.controller))

        b2 = tk.Button(self,text = "3-horn", padx = 10, pady =10, fg ="white", bg="#038cfc", command = lambda:select3Horn(self.controller))

        b3 = tk.Button(self,text = "Long neck", padx = 10, pady =10, fg ="white", bg="#038cfc", command = lambda:selectLongNeck(self.controller))
        b1.pack()
        b2.pack()
        b3.pack()


class MainPage(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        self.controller.updateApp()
        canvas = tk.Canvas(self, height = 400, width=400, bg = "#038cfc")
        canvas.grid(row = 0,columnspan =4)
        self.label = tk.Label(self, text="Hunger: " + str(self.controller.model.pet.m_fullness), font=self.controller.title_font)
        self.label.grid(row = 1, column = 0)

        self.label2 = tk.Label(self, text="Happiness: " + str(self.controller.model.pet.m_happiness), font=self.controller.title_font)
        self.label2.grid(row = 1, column = 1, columnspan = 3)

        self.updateLabel()

        b1 = tk.Button(self,text = "Feed", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:feedAction(self.controller.model), borderwidth=0)

        b2 = tk.Button(self,text = "Walk", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:walkAction(self.controller.model), borderwidth=0)

        b3 = tk.Button(self,text = "Pet", padx = 10, pady =5, fg ="white", bg="#038cfc", command = lambda:petAction(self.controller.model))

        b4 = tk.Button(self,text = "Connect", padx = 10, pady =10, fg ="white", bg="#038cfc", command = connectAction, borderwidth=0)

        b1.grid(row = 2, column = 0)
        b2.grid(row = 2, column = 1)
        b3.grid(row = 2, column = 2)
        b4.grid(row = 2, column = 3)

        
        self.update_idletasks()
        my_image = PhotoImage(file = "./photos/longbase.png")
        self.one = my_image

        width = canvas.winfo_width()/2
        height = canvas.winfo_height()/2

        print(width)
        print(height)

        canvas.create_image(width, height, image=my_image, anchor = CENTER)

    def updateLabel(self):
        self.label.configure(text="Hunger: " + str(self.controller.model.pet.m_fullness), font=self.controller.title_font)
        self.label2.configure(text="Happiness: " + str(self.controller.model.pet.m_happiness), font=self.controller.title_font)
        self.after(1000,self.updateLabel)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()