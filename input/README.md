# Data File

This file will hold all the data for your cards, all the titles, texts, images and icons.

To use it:

1) Open a new page on the excel file, name it accordingly(remember to update the pages name in the Config file).

2) See the current examples to see how to use text and image files. 

Dont worry about placing the text and what field is an image or a text for now, that is the job of the config file.

# Config

The config file is used as an argument to the main.py program.
It is the only file to be passed as an argument, all the remaining folder can be acessed by reading the config file.

The config is a simple json file to hold configurations.

Fields:

+ **Data** : The path to the excel file to analise

+ **Cards Name**: A list of  tags used to build the final files names, in the current example, the name is "Title"+"Id", so the first card form the events folder will be named "Events1".

+ **Image Folder**: The base path for acessing the images to use.