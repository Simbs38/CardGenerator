import pandas as pd

class ExcelParse:
	def __init__(self, configs):
		self.configs = configs

	def GetPageInfos(self, pageName):
		ans = []

		try:
			xls = pd.ExcelFile(self.configs.DataFile)
		except Exception as e:
			print("Excel file not found: \n" + str(e))
			
		try:
			page = pd.read_excel(xls, pageName)
			for i in page.index:
				tmp = {}
				for item in page.columns:
					tmp[item] = page[item][i]
				ans.append(dict(tmp))
				tmp.clear()

		except Exception as e:
			print("Excel page not found: \n" + str(e))
			
		return ans
