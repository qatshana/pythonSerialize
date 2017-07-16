class Pet(object):
	def __init__(self,name,species):
		self.name=name
		self.species=species
	def getName(self):
		return self.name
	def getSpecies(self):
		return self.species
	def __str__(self):
		return "%s is a %s" %(self.name,self.species)


class Dog(Pet):
	def __init__(self,name,chasesCats):
		Pet.__init__(self,name,"Dog")
		self.chasesCats=chasesCats
	def getChasesCats(self):
		return self.chasesCats
		