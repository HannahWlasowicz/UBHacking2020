from Model import *
from gui import *

def feedAction(pet):
    pet.feed()

def walkAction(pet):
    pet.walkPet()

def petAction(pet):
    pet.petPet()

def connectAction():
    print("for later")

def select3Horn(controller):
    controller.model = Model("horn_boi")
    controller.show_frame("MainPage")
    #switch to main gui

def selectTrex(controller):
    controller.model = Model("t_rex")
    controller.show_frame("MainPage")
    #switch to main gui

def selectLongNeck(controller):
    controller.model = Model("long_boi")
    controller.show_frame("MainPage")
    #switch to main gui
