from imgStruct import imgStruct as IS
import pandas as pd

excelFilePath = "rcs/test.py"

class InfoParse:

	def __init__(self):
		pass

	@staticmethod
	def ParseExcel(cards):
		print("parsing e tudo")
		xls = pd.ExcelFile(excelFilePath)


		for card in cards:
			page = xls.read_excel(xls, card)





		return []