import operator
from colorPallet import Palletes


class ImgColors:

	def __init__(self):
		pass

	@staticmethod
	def ColorCard(cardInfo, card):
		colors = ImgColors.GetAllColors(card)
		pallete = Palletes.GetBluePallete()
		print("colors: " + str(len(colors)))

		colorBase = colors[0][0]
		colorTextContainer = colors[1][0]
		colorBorder = colors[2][0]
		
		card = ImgColors.PaintColor(card, colorBase, pallete.baseColor)
		card = ImgColors.PaintColor(card, colorTextContainer, pallete.textContainerColor)
		card = ImgColors.PaintColor(card, colorBorder, pallete.borderColor)

		colorName = colors[3]
		colorBanner = colors[4]
		
		if(cardInfo.cardType != "events"):
			card = ImgColors.PaintColor(card, colorName[0], pallete.nameContainerColor)
			colors.remove(colorName)
			if(cardInfo.cardType == "tunos"):
				card = ImgColors.PaintColor(card, colorBanner[0], pallete.bannerColor)
				colors.remove(colorBanner)

		return card

	@staticmethod
	def PaintColor(img, filterColor, newColor):
		rows,cols,length = img.shape
		values = []
		for i in range(rows):
			for j in range(cols):
				tmp = (img[i,j,0],img[i,j,1],img[i,j,2])
				if(tmp == filterColor):
					img[i,j,0] = newColor[0]
					img[i,j,1] = newColor[1]
					img[i,j,2] = newColor[2]
			
		return img

	@staticmethod
	def GetAllColors(img):
		rows,cols,length = img.shape
		values = {}
		for i in range(rows):
			for j in range(cols):
				tmp = (img[i,j,0],img[i,j,1],img[i,j,2])
				if(tmp not in values):
					values[tmp] = 1
				else:
					values[tmp] += 1

		return sorted(values.items(), key=operator.itemgetter(1), reverse = True)