import re

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
		self.cardType = cardType


class Pallete:
	def __init__(self):
		self.name = "Unnamed"
		self.TextBackground = (0,0,0)
		self.NameField = (0,0,0)
		self.Border = (0,0,0)
		self.Background = (0,0,0)

	@staticmethod
	def ParseColor(line):
		line = re.sub('[/()]', '', line)
		lines = line.split(",")
		
		return (int(lines[0]),int(lines[1]),int(lines[2]))
