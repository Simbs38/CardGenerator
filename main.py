from InfoParse import InfoParse as IP
from imgText import ImgText as IT
from imgColors import ImgColors as IC
from ImgIcon import ImgIcon as II
import cv2
import sys

def parseImage(imageData, imgPath, outputPath, pallete):
	tmp = II()
	card = cv2.imread(imgPath)
	card = IC.ColorCard(imageData, card, pallete)
	card = IT.InsertText(imageData, card)
	cv2.imwrite(outputPath, card)

	if imageData.cardType == 'tunos':
		II.build_cubes(tmp.translate_colors(imageData.requirements), INPUT_DIR = outputPath)
	elif imageData.cardType == 'events':
		II.build_cubes(tmp.translate_colors(imageData.requirements), 1500, 220, INPUT_DIR = outputPath)

def main():
	cardsToMake = []

	if(len(sys.argv) == 1):
		cardsToMake.append("events")
		cardsToMake.append("breaks")
		cardsToMake.append("tunos")
		cardsToMake.append("items")
	elif(sys.argv[1] == 'e'):
		cardsToMake.append("events")
	elif(sys.argv[1] == 'b'):
		cardsToMake.append("breaks")
	elif(sys.argv[1] == 't'):
		cardsToMake.append("tunos")
	elif(sys.argv[1] == 'i'):
		cardsToMake.append("items")
	else:
		print("Unknown case")
	
	palletes = IP.ParseColors()
	cardsList = IP.ParseExcel(cardsToMake)

	i = 0

	for x in cardsList:
		parseImage(x, "rcs/" + x.cardType + ".png", "outputs/" + x.cardType + "/" + str(i) + ".png", palletes[x.pallete])
		i = i + 1

if __name__ == "__main__":
	main()
