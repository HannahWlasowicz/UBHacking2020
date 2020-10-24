from PetTypes import PetTypes
from PetStates import PetStates
from PetClass import *
import time

	
class Model:
	def __init__(self, PetType):
		self.pet = Pet(PetType)
		self.gameTime = time.time()
		self.lastUpdate = 0

	def feed(self):
		self.pet.feedPet(15)
		print(self.pet.m_fullness)

	def walkPet(self):
		self.pet.playWithPet(25)
		print(self.pet.m_happiness)

	def petPet(self):
		self.pet.playWithPet(5)
		print(self.pet.m_happiness)

	def update(self):
		curr = time.time()
		if (curr - lastUpdate) > 5:
			self.lastUpdate = curr
			self.pet.m_fullness -= 1
			self.pet.m_happiness -= 1
		self.pet.updatePetState()
		





