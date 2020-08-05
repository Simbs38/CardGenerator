from PIL import Image, ImageDraw
import pandas as pd

class ImgInput:
	def __init__(self, baseImage, card, confs, configs):
		allVars = confs['Cols']
		allImgs = {}
		self.draw = ImageDraw.Draw(baseImage)
		self.configs = configs

		for var in allVars:
			if var in confs:
				if("Type" in confs[var]):
					if confs[var]["Type"] == "Img":
						if(len(str(card[var])) > 0 and not(pd.isna(card[var]))):
							allImgs[var] = confs[var]
							allImgs[var]["Content"] = card[var]
				else:
					print("Type not found in: " + confs[var])

		for img in allImgs:
			self.InsertImg(baseImage, allImgs[img])


	def InsertImg(self, baseImage, img):
		try:
			imgToInsert = Image.open(self.configs.ImageFolder + img["Content"])
			imgToInsert = self.ResizeImage(imgToInsert, img)
			width, height = baseImage.size
			(x,y) = self.GetOffSet(img)
			baseImage.paste(imgToInsert, (x,y), mask=imgToInsert)
		except Exception as e:
			print("Error while loading icon: \n" + str(e))


	def GetOffSet(self, img):
		try:
			if("Offset-X" in img and "Offset-Y" in img):
				return (int(img["Offset-X"]), int(img["Offset-Y"]))
			elif("Offset-X" in img):
				return (int(img["Offset-X"]), int(self.configs.ImageStandart["Offset-Y"]))
			elif("Offset-Y" in img):
				return (int(self.configs.ImageStandart["Offset-X"]), int(img["Offset-Y"]))
			else:
				return (int(self.configs.ImageStandart["Offset-X"]), int(self.configs.ImageStandart["Offset-Y"]))
		except Exception as e:
			print("Error while setting offsets: \n" + str(e))
			return (0,0)

	def ResizeImage(self, imageToInsert, img):
		try:
			(x,y) = imageToInsert.size
			if("Size-X" in img and "Size-Y" in img):
				(x,y) = (img["Size-X"], img["Size-Y"]) 
			elif("Size-X" in img):
				x = img["Size-X"] 
			elif("Size-Y" in img):
				y = img["Size-Y"] 
			return imageToInsert.resize((x,y)) 
		except Exception as e:
			print("Error while resizing image: \n" + str(e))
			return imgToInsert