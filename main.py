from InfoParse import InfoParse as IP
from imgText import ImgText as IT
import cv2
import sys

def parseImage(imageData, imgPath, outputPath):
	#parseColor
	#insert stuffs

	card = cv2.imread(imgPath)
	card = IT.InsertText(imageData, card)
	cv2.imwrite(outputPath, card)


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
	
	cardsList = IP.ParseExcel(cardsToMake)

	i = 0

	for x in cardsList:
		parseImage(x, "rcs/" + x.cardType + ".png", "outputs/" + x.cardType + "/" + str(i) + ".png")
		i = i + 1

if __name__ == "__main__":
	main()

