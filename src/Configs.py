import json


class Configs():
	def __init__(self, fileName):
		self.CardsType = {}

		try:
			with open(fileName) as file:
				data = json.load(file)
				self.DataFile = data["Data"]
				self.CardsName = data["CardsName"]
				self.CardsToGenerate = data["CardsToGenerate"]
				self.ImageFolder = data["ImageFolder"]
				self.TextStandart = data["TextStandart"]
				self.ImageStandart = data["ImageStandart"]
				self.GroupStandart = data["GroupStandart"]
				for item in self.CardsToGenerate:
					self.CardsType[item] = data[item]
		except Exception as e:
			print("Error while loading JSON file: \n" + str(e))
		