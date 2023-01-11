from lists import sets
import random
import base64

c = sets()
x = []

def decrypt(stri=""):
	return str(base64.b64decode(stri.encode('ascii')).decode('ascii'))

def typing(txt="", time=10):
	speed = 10000 * time
	length = len(txt)
	i = 0
	while i < speed * length:
		if i % speed == 0:
			print(txt[i // speed], end="", flush=True)
		i += 1
	print()

keys = c.getKeys()
q = c.getSets()
i = 0
score = 0

typing("Welcome to my simple quiz console program...\n\n")

while i < len(q):
	y = random.randint(0, len(q) - 1)
	if y in x:
		i -= 1
	else:
		x.append(y)
	i += 1

for i in x:
	r = q[i]
	typing(decrypt(r.get("q")))
	for j in range(len(r.get("a"))):
		typing(c.keys()[j] + ". " + decrypt(r.get("a")[j]))
	ans = input("Enter your answer: ").lower()
	while ans != "a" and ans != "b" and ans != "c" and ans != "d":
		ans = input("Enter your answer: ").lower()
	if keys.get(ans) == r.get("k"):
		score += 1
	print("\n")

ave = (score / len(x)) * 100
typing("------------------------------------------------------")
typing(f"You've got {score} points over {len(x)} with the average of {ave}")