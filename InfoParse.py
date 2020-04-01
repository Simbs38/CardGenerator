from Structs import imgStruct as IS
from Structs import Pallete
import pandas as pd

#excelFilePath = "rcs/test.xlsx"
excelFilePath = "rcs/Cards.xlsx"

class InfoParse:

	def __init__(self):
		pass

	@staticmethod
	def ParseExcel(cards):
		xls = pd.ExcelFile(excelFilePath)
		ans = []

		for card in cards:
			page = pd.read_excel(xls, card)

			for i in page.index:
				imgStruct = IS(card)
				for item in page.columns:
					tmpType = page[item].head(0).name

					if(tmpType == "Name"):
						imgStruct.name = page[item][i]
					elif(tmpType == "Text"):
						imgStruct.text = page[item][i]
					elif(tmpType == "Image"):
						imgStruct.image = page[item][i]
					elif(tmpType == "Requirements"):
						imgStruct.requirements = page[item][i]
					elif(tmpType == "Prestige"):
						imgStruct.prestige = page[item][i]
					elif(tmpType == "Pallete"):
						imgStruct.pallete = page[item][i]
					elif(tmpType == "Type"):
						imgStruct.type = page[item][i]
					elif(tmpType == "Unnamed: 0"):
						pass

				ans.append(imgStruct)

		return ans

	@staticmethod
	def ParseColors():
		xls = pd.ExcelFile(excelFilePath)
		ans = {}
		page = pd.read_excel(xls, "pallete")

		for i in page.index:
			colorStruct = Pallete()
			for item in page.columns:
				tmpType = page[item].head(0).name

				if(tmpType == "name"):
					colorStruct.name = page[item][i]
				elif(tmpType == "TextBackground"):
					colorStruct.TextBackground = colorStruct.ParseColor(page[item][i])
				elif(tmpType == "NameFieldColor"):
					colorStruct.NameField = colorStruct.ParseColor(page[item][i])
				elif(tmpType == "BorderColor"):
					colorStruct.Border = colorStruct.ParseColor(page[item][i])
				elif(tmpType == "BackgroundColor"):
					colorStruct.Background = colorStruct.ParseColor(page[item][i])

			ans[colorStruct.name] = colorStruct

		return ans
