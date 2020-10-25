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
    controller.model = Model("HORN")
    controller.show_frame("MainPage")
    #switch to main gui

def selectTrex(controller):
    controller.model = Model("REX")
    controller.show_frame("MainPage")
    #switch to main gui

def selectLongNeck(controller):
    controller.model = Model("LONG")
    controller.show_frame("MainPage")
    #switch to main gui
