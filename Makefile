
mainFolder = outputs
eventsFolder = $(mainFolder)/events
tunosFolder = $(mainFolder)/tunos
breaksFolder = $(mainFolder)/breaks
itemsFolder = $(mainFolder)/items

make:
	@if [ -d $(mainFolder) ]; then  echo "Main folder alredy exists"; else echo "creating main folder" && mkdir $(mainFolder); fi
	@if [ -d $(eventsFolder) ]; then  echo "Events folder alredy exists"; else echo "creating events folder" && mkdir $(eventsFolder); fi
	@if [ -d $(tunosFolder) ]; then  echo "Tunos folder alredy exists"; else echo "creating tunos folder" && mkdir $(tunosFolder); fi
	@if [ -d $(breaksFolder) ]; then  echo "Breaks folder alredy exists"; else echo "creating breaks folder" && mkdir $(breaksFolder); fi
	@if [ -d $(itemsFolder) ]; then  echo "Items folder alredy exists"; else echo "creating items folder" && mkdir $(itemsFolder); fi
	python3 main.py

events:
	@if [ -d $(mainFolder) ]; then  echo "Folder alredy exists"; else echo "creating folder" && mkdir $(outputs); fi
	@if [ -d $(eventsFolder) ]; then  echo "Events folder alredy exists"; else echo "creating events folder" && mkdir $(eventsFolder); fi
	python3 main.py e

tunos:
	@if [ -d $(mainFolder) ]; then  echo "Folder alredy exists"; else echo "creating folder" && mkdir $(mainFolder); fi
	@if [ -d $(tunosFolder) ]; then  echo "Tunos folder alredy exists"; else echo "creating tunos folder" && mkdir $(tunosFolder); fi
	python3 main.py t
	

breaks:
	@if [ -d $(mainFolder) ]; then  echo "Folder alredy exists"; else echo "creating folder" && mkdir $(mainFolder); fi
	@if [ -d $(breaksFolder) ]; then  echo "Breaks folder alredy exists"; else echo "creating breaks folder" && mkdir $(breaksFolder); fi
	python3 main.py b

items:
	@if [ -d $(mainFolder) ]; then  echo "Folder alredy exists"; else echo "creating folder" && mkdir $(mainFolder); fi
	@if [ -d $(itemsFolder) ]; then  echo "Items folder alredy exists"; else echo "creating items folder" && mkdir $(itemsFolder); fi
	python3 main.py i

clear:
	@ rm -r outputs