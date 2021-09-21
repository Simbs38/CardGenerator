import sys
from src.Configs import Configs
from src.CardMaker import CardMaker
from src.ExportPdf import ExportPdf

def main():
	'''
	if(len(sys.argv) == 1):
		print("Please insert a config file")
	elif(sys.argv[1][-5:] ==".json"):
		configs = Configs(sys.argv[1])
		if hasattr(configs, 'DataFile'):
			CardMaker(configs)
	'''
	
	if(len(sys.argv) == 3 and sys.argv[2] == "-pdf"):
		ExportPdf()

if __name__ == "__main__":
	main()