from PIL import Image, ImageDraw, ImageFont
import textwrap
import pandas as pd

class TextInput:
	def __init__(self, baseImage, card, confs, configs):
		allVars = confs['Cols']
		allText = {}
		self.configs = configs
		self.draw = ImageDraw.Draw(baseImage)

		for var in allVars:
			if var in confs:
				if confs[var]["Type"] == "Text":
					if(len(str(card[var])) > 0 and not(pd.isna(card[var]))):
						allText[var] = confs[var]
						allText[var]["Content"] = str(card[var])

		for text in allText:
			self.InsertText(baseImage, allText[text])

	def InsertText(self, baseImage, text):
		lines = self.GetTextLines(text)
		(x,y) = self.GetOffSet(text)
		font = self.GetFont(text)
		color = self.GetColor(text)
		lineSpacing = self.GetLineSpacing(text)
		
		for line in lines:
			if(font is not None):
				width, height = font.getsize(line)
				self.draw.text((x,y), line, fill = color, font = font)
				y += height + lineSpacing
			else:
				self.draw.text((x,y), line, fill = color)
				y += 40 + lineSpacing

	def GetTextLines(self, text):
		try:
			if("Line-Length" in text):
				return textwrap.wrap(text["Content"], width = text["Line-Length"])
			else:
				return textwrap.wrap(text["Content"], width = self.configs.TextStandart["Line-Length"])
		except Exception as e:
			print("Error while loading text: \n" + str(e))
			return [""]

	def GetOffSet(self, text):
		try:
			if("Offset-X" in text and "Offset-Y" in text):
				return (int(text["Offset-X"]), int(text["Offset-Y"]))
			elif("Offset-X" in text):
				return (int(text["Offset-X"]), int(self.configs.TextStandart["Offset-Y"]))
			elif("Offset-Y" in text):
				return (int(self.configs.TextStandart["Offset-X"]), int(text["Offset-Y"]))
			else:
				return (int(self.configs.TextStandart["Offset-X"]), int(self.configs.TextStandart["Offset-Y"]))
		except Exception as e:
			print("Error while setting offsets: \n" + str(e))
			return (0,0)

	def GetFont(self, text):
		try:
			if("Font" in text and "Font-Size" in text):
				return ImageFont.truetype(text["Font"], size=text["Font-Size"])
			elif("Font" in text):
				return ImageFont.truetype(text["Font"], size=self.configs.TextStandart["Font-Size"])
			else:
				return None
		except Exception as e:
			print("Error while setting font: \n" + str(e))
			return None

	def GetColor(self, text):
		try:
			if("Font-Color" in text):
				return text["Font-Color"]
			else:
				return self.configs.TextStandart["Font-Color"]
		except Exception as e:
			print("Error while loading color: \n" + str(e))
			return "rgb(0, 0, 0)"

	def GetLineSpacing(self, text):
		try:
			if("Line-Spacing" in text):
				return text["Line-Spacing"]
			else:
				return self.configs.TextStandart["Line-Spacing"]
		except Exception as e:
			print("Error while loading line spacing: \n" + str(e))
			return 0