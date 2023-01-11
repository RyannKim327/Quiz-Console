import json

class sets:
	def keys(self):
		k = [
			"a",
			"b",
			"c",
			"d"
		]
		return k
	def getKeys(self):
		keys = {
			"a": 0,
			"b": 1,
			"c": 2,
			"d": 3
		}
		return keys

	def getSets(self):
		lists = json.loads(open("lists.json", "r").read())["lists"]
		return lists