from PetStates import PetStates

class Pet:

	def __init__(self, petType):

		self.m_fullness = 50
		self.m_happiness = 75
		self.m_petType = petType
		self.m_petState = PetStates.CONTENT

	def feedPet(self, amount):
		self.m_fullness += amount
		if self.m_fullness >= 100:
			self.m_happiness -= self.m_fullness - 100
		else:
			self.m_happiness += amount//5

	def playWithPet(self, amount):
		self.m_happiness = (self.m_happiness + amount)
		if self.m_happiness > 100:
			self.m_happiness=100
		self.m_fullness -= amount//5
		if self.m_fullness < 0:
			self.m_fullness = 0

	def updatePetState(self):
		mood = self.m_happiness
		if mood >= 75:
			self.m_petState = PetStates.HAPPY
		elif mood >= 50:
			self.m_petState = PetStates.CONTENT
		elif mood == 0 and self.m_fullness == 0:
			self.m_petState = PetStates.DEAD
		else:
			self.m_petState = PetStates.SAD





