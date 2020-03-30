from imgStruct import imgStruct as IS
import pandas as pd

excelFilePath = "rcs/test.xlsx"

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
					else:
						print("forgoton: " + tmpType)

				ans.append(imgStruct)

		return ans