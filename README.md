# Card Generator

The card Generator is a tool to quickly create decks of cards without having to edit all the images needed.
This can give a great flexibity when trying to apply changes in bulk.

Check out the inputs [here](/input).

And the results [here](/Output)

## Getting Started

Clone the project and enter the folder:

```
git clone https://github.com/Simbs38/CardGenerator
cd CardGenerator
```

To run the program you will need a Config file to be used as a formating file, an Excel file to hold all your data about your cards, and all the images needed.

To help you getting started the project is presented with a sample files. To execute it with the sample files, after cloning the project use:

```
python main.py input/config.json
```

## Dependencys

To run the project you will need to install the following packages:

```
pip install xlrd
pip install openpyxl
pip install Pillow
pip install pandas
pip install pylatex
```

## Configuring to your project

+ Use the [data.xlsl](/input#Data) file to save all the data from your cards (you can rename this file, but you will have to replace the name in the config.json file). 

+ Use a page for each type of deck your are building, in the default sample, we are building 3 types of diferent decks.

+ Each page should start with the card Id, followed by all the parameters needed for the card, you are free to add or remove parameters form here.

+ Once your data is build, the config.json file can be used to set the position and some other aspects of the elements inside the card. Learn how to build the config file [here](/input#Config)