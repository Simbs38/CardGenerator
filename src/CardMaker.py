from src.ExcelParse import ExcelParse
from src.TextInput import TextInput as HandleText
from src.ImgInput import ImgInput as HandleImgs
from src.GroupInput import GroupInput as HandleGroups
from PIL import Image
import os

class CardMaker:
	def __init__(self, configs):
		self.configs = configs
		self.Parser = ExcelParse(configs)

		for item in self.configs.CardsToGenerate:
			pageInfos = self.Parser.GetPageInfos(item)
			for card in pageInfos:
				self.CreateImage(card, configs.CardsType[item])
				
	def CreateImage(self, card, confs):
		try:		
			baseImage = Image.open(self.configs.ImageFolder + card[confs["BaseImage"]])
			cardName = self.GetCardName(card, confs)
			HandleText(baseImage, card, confs, self.configs)
			HandleImgs(baseImage, card, confs, self.configs)
			HandleGroups(baseImage, card, confs, self.configs)
			self.CheckFolderExists(cardName)
			baseImage.save(cardName)
			print("Card: " + cardName + " created")
		except Exception as e:
			print("Error editing image: \n" + str(e))
			
	def GetCardName(self, card, confs):
		try:
			titleParts = self.configs.CardsName.replace(" ", "").split(',')
			ans = ""

			for part in titleParts:
				if part in card:
					ans += str(card[part]).replace(" ","")
				elif part in confs:
					ans += str(confs[part]).replace(" ","")
				else:
					print("Information about", part, "was not found")

			ans += ".png"
			return ans

		except Exception as e:
			print("Error while loading card name: \n" + str(e))
			return "notFound.png"

	def CheckFolderExists(self, cardName):
		try:
			cardName = cardName.split("/")
			cardName.pop()
			totalName = ""

			for folder in cardName:
				if len(totalName) == 0:
					totalName += folder
				else:
					totalName += "/" + folder

				if not os.path.isdir(totalName):
					os.mkdir(totalName)
		except Exception as e:
			print("Error creating folder: \n" + str(e))