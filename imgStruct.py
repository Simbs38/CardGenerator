

class imgStruct:

	def __init__(self, cardType):
		if(cardType == "events"):
			self.requirements = ""
			self.prestige = 0
		elif(cardType == "tunos"):
			self.requirements = ""
			self.type = ""
		
		self.name = ""
		self.image = ""
		self.text = ""
		
		self.pallete = ""
		self.borderColor = ""
		self.brackgroundColorLight = ""
		self.backgroundColorDark = ""
		self.textBoxColor = ""
		self.nameColor = ""
		self.nameBoxColor = ""
		self.cardType = cardType