from InfoParse import InfoParse as IP
import sys

def parseImage(imageData):
	#parseColor
	#parseText

	pass


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

	for x in cardsList:
		parseImage(x)
		pass

if __name__ == "__main__":
	main()

