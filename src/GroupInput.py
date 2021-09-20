from PIL import Image, ImageDraw
import pandas as pd

class GroupInput:
	def __init__(self, baseImage, card, confs, configs):
		allVars = confs['Cols']
		allGroups = {}
		self.baseImage = baseImage
		self.draw = ImageDraw.Draw(baseImage)
		self.configs = configs

		for var in allVars:
			if var in confs:
				if confs[var]["Type"] == "Group":
					if(len(str(card[var])) > 0 and not(pd.isna(card[var]))):
						allGroups[var] = confs[var]
						tmp = card[var].replace(" ","")
						allGroups[var]["Content"] = tmp

		print(len(allGroups))

		for group in allGroups:
			self.InsertGroup(allGroups[group])


	def InsertGroup(self, group):
		(x, y) = self.GetCenter(group)
		content = self.GetContent(group)
		content = self.GetImages(content, group)
		direction = self.GetDirection(group)
		padding = self.GetPadding(group)
		(sizeX, sizeY) = self.GetSize(direction, padding, content, group)
		(insertX, insertY) = (x - sizeX/2, y - sizeY/2)

		self.InsertImages(insertX, insertY, direction, padding, content, group)


	def GetCenter(self, group):
		try:
			if("Center-x" in group and "Center-y" in group):
				return (group["Center-x"], group["Center-y"])
			elif("Center-x" in group):
				return (group["Center-x"], self.configs.GroupStandart["Center-y"])
			elif("Center-y" in group):
				return (self.configs.GroupStandart["Center-x"], group["Center-y"])
			else:
				return (self.configs.GroupStandart["Center-x"], self.configs.GroupStandart["Center-y"])
		except Exception as e:
			print("Error reading group center point: \n" + str(e))
			return (0,0)

	def GetContent(self, group):
		try:
			if("Content-Mapping" in group):
				ans = {}
				for item in group["Content-Mapping"]:
					ans[item] = group["Content-Mapping"][item]
				return ans
			elif("Content-Mapping" in self.configs.GroupStandart):
				ans = {}
				for item in self.configs.GroupStandart["Content-Mapping"]:

					ans[item] = self.configs.GroupStandart["Content-Mapping"][item]
				return ans
			else:
				return {}
		except Exception as e:
			print("Error reading Content-Mapping: \n" + str(e))
			return {}

	def GetImages(self, content, group):
		try:
			ans = {}
			for item in content:
				tmpImage = Image.open(self.configs.ImageFolder + content[item])
				tmpImage = self.ResizeImage(tmpImage, group)
				ans[item] = tmpImage
			return ans
		except Exception as e:
			print("Error while loading images: \n" + str(e))

	def ResizeImage(self, img, content):
		try:
			(x,y) = self.baseImage.size
			if("Size-X" in content and "Size-Y" in content):
				(x,y) = (content["Size-X"], content["Size-Y"]) 
			elif("Size-X" in content):
				x = content["Size-X"] 
			elif("Size-Y" in content):
				y = content["Size-Y"] 
			return img.resize((x,y))
		except Exception as e:
			print("Error while resizing image: \n" + str(e))


	def GetDirection(self, group):
		try:
			if("Direction" in group):
				if(group["Direction"] == "Ver"):
					return (0,1)
				else:
					return (1,0)
			elif("Direction" in self.configs.GroupStandart):
				if(self.configs.GroupStandart["Direction"] == "Ver"):
					return (0,1)
				else:
					return (1,0)
			else:
				return (1,0)
		except Exception as e:
			print("Error reading group direction")
			return (1,0)

	def GetPadding(self, group):
		try:
			if("Padding" in group):
				return group["Padding"]
			elif("Padding" in self.configs.GroupStandart):
				return self.configs.GroupStandart["Padding"]
			else:
				return 0
		except Exception as e:
			print("Error while reading padding: \n" + str(e))
			return 0


	def GetSize(self, direction, padding, content, group):
		ans = 0
		maxX = 0
		maxY = 0
		for item in group["Content"]:
			if(item in content):
				x, y = content[item].size
				ans += direction[0] * (x + padding) + direction[1] * (y + padding)
				
				if(x > maxX):
					maxX = x

				if(y > maxY):
					maxY = y

		return (direction[0] * max(maxX,(ans - padding)), direction[1] * max(maxY, (ans - padding)))


	def InsertImages(self, x, y,direction, padding, content, group):
		try:
			for item in group["Content"]:
				self.baseImage.paste(content[item], (int(x),int(y)), mask=content[item])
				(sizeX, sizeY) = content[item].size
				x += direction[0] * (padding + sizeX/2)
				y += direction[1] * (padding + sizeY/2)
		except Exception as e:
			print("Error while inserting group images: \n" + str(e))