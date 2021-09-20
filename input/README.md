# Data File

This file will hold all the data for your cards, all the titles, texts, images and icons.

To use it:

1) Open a new page on the excel file, name it accordingly(remember to update the pages name in the Config file).

2) See the current examples to see how to use text and image files. 

Dont worry about placing the text and what field is an image or a text for now, that is the job of the config file.

# Config

The config file is used as an argument to the main.py program.
It is the only file to be passed as an argument, all the remaining folder can be acessed by reading the config file.

The config is a simple json file to hold configurations, and it can be divided into 3 sections.

### Global Fields:

+ **Data** : The path to the excel file to analise

+ **CardsName**: A list of  tags used to build the final files names, in the current example, the name is "Title"+"Id", so the first card form the events folder will be named "Events1".

+ **ImageFolder**: The base path for acessing the images to use.

+ **CardsToGenerate**: Specifies the excel pages to be read and parsed. If the title of a page is not in this section, its output will not be produced

```

{
	"Data": "input/data.xlsx",
	"CardsName": "Title, Id",
	"ImageFolder" : "input/images/",
    "CardsToGenerate":[
		"Events",
		"Items",
		"Other"
	]
}

```

### Default Fields

These fields are used as a fallback for each of the existing elements (text, image and groups). If the field is not defined in the specific tag, them the value defined here is used instead.

```
{
    "TextStandart" :
    {
        "Offset-X" : 0,
        "Offset-Y" : 0,
        "Font-Size" : 45,
        "Font-Color" : "rgb(0, 0, 0)",
        "Line-Length" : 35,
        "Line-Spacing": 10
    },
    "ImageStandart": 
    {
        "Offset-X" : 0,
        "Offset-Y" : 0
    },
    "GroupStandart":
    {
        "Center-x": 200,
        "Center-y": 200,
        "Direction" : "Hor",
        "Padding" : 10
	}
}
```

### Specific Fields

For each given excel page you are allowed to define all the formating of the final card, to do so, the following fields can be used inside a tag with the same name as the excel page:

+ **Title** : Field used to define the path of the cards in this page, can be used allong with some other info to make it unique for every file.

+ **BaseImage** : The image background to use for this batch of cards.

+ **Cols** : To collumms to be read from the given excel page.

+ **Cols Properties** : For each collum defined in "Cols", you can now adjust its settings:

    + **Type** : Text, Img or Group;

    + **Offset-X** : Defines the Offset in the X axis in pixels;

    + **Offset-Y** : Defines the Offset in the Y axis in pixels;

    + **Line-Length**:(text only) Defines the line size;

    + **Line-Spacing**:(text only) Defines the space between lines;

    + **Font**:(text only) Defines the text font;

    + **Font-Size**:(text only) Defines the text font size;

    + **Size-X**:(img only) Defines the width of an image;

    + **Size-Y**:(img only) Defines the heigth of an image.


```
{
    "Items": {
		"Title": "Output/Items/Items",
		"BaseImage" : "BaseName",
		"Cols" :[
			"Id",
			"Name",
			"Info",
			"Price",
			"BaseName"],
		"Name" : {
			"Type" : "Text",
			"Offset-X" : 100,
			"Offset-Y" : 1270,
			"Font" : "input/Verdana.ttf"
		},
		"Info" : {
			"Type" : "Text",
			"Offset-X" : 100,
			"Offset-Y" : 1450,
			"Line-Length" : 25,
			"Line-Spacing" : 10,
			"Font" : "input/Verdana.ttf"
		},
		"Price" : {
			"Type" : "Img",
			"Size-X" : 400,
			"Size-Y" : 400,
			"Offset-X" : 850,
			"Offset-Y" : 1100
		}
	}
}

```