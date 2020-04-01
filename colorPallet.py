
class Palletes:
	def __init__(self):
		pass

	@staticmethod
	def GetBluePallete():
		ans = Palletes()

		ans.baseColor = (255,0,0)
		ans.textContainerColor = (150,0,0)
		ans.borderColor = (120,0,0)
		ans.nameContainerColor = (90,0,0)
		ans.bannerColor = (50,0,0)
		ans.name = "blue"

		return ans