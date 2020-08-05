import sys
from src.Configs import Configs
from src.CardMaker import CardMaker

def main():
	
	if(len(sys.argv) == 1):
		print("Please insert a config file")
	elif(sys.argv[1][-5:] ==".json"):
		configs = Configs(sys.argv[1])
		if hasattr(configs, 'DataFile'):
			CardMaker(configs)

if __name__ == "__main__":
	main()