# Card Generator

The card Generator is a tool to quickly create decks of cards without having to edit all the images needed.
This can give a great flexibity when trying to apply changes in bulk.

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

```

To run the pdf features you will also need to [install latex](https://www.latex-project.org/get/) locally.