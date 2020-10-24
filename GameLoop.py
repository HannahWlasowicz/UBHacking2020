from PetTypes import PetTypes
from PetStates import PetStates
from PetClass import Pet
import time

pet = Pet(PetTypes.ANIMAL_A)
gameTime = time.time()
lastUpdate = 0

def feed():
	global pet
	pet.feedPet(15)

def walkPet():
	global pet
	pet.playWithPet(25)

def petPet():
	global pet
	pet.playWithPet(5)

def update():
	global pet
	global lastUpdate
	curr = time.time()
	#print ("current time", curr, "old time", lastUpdate)
	if (curr - lastUpdate) > 5:
		lastUpdate = curr
		pet.m_fullness -= 1
		pet.m_happiness -= 1
		#print(pet.m_fullness)
		#print(pet.m_happiness)
	pet.updatePetState()
	

def initialize(petType):
	global pet
	pet = Pet(petType)

initialize(PetTypes.ANIMAL_B)

while(True):
	update()



