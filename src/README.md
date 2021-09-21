# Src

The main.py file uses the classes present on this folder.

The [CardMaker](CardMaker.py) represents the key features of the tool, since it is the main file to build the cards using the helping classes.

There are 3 types of possible inputs, [Images](ImgInput.py), [Text](TextInput.py) and [Groups](GroupInput.py), and each of them is handled by its own class.

This folder also contains the [ExportPdf](ExportPdf.py) that handles all the images in the Output folder and exports them as a Pdf and the [ExcelParser](ExcelParse.py) that parses the given excel file with the cards data.

All the configurations writen in the config.json file are stored and used by the [Config](Config.py).
