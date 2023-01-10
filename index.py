from lists import sets
import random

c = sets()
x = []

keys = c.getKeys()
q = c.getSets()
i = 0
score = 0
while i < len(q):
	y = random.randint(0, len(q) - 1)
	if y in x:
		i -= 1
	else:
		x.append(y)
	i += 1

for i in x:
	r = q[i]
	print(r.get("q"))
	for j in range(len(r.get("a"))):
		print(c.keys()[j] + ". " + r.get("a")[j])
	ans = input("Enter your answer: ")
	while ans != "a" and ans != "b" and ans != "c" and ans != "d":
		ans = input("Enter your answer: ")
	if keys.get(ans) == r.get("k"):
		score += 1

print(f"You've got {score} points")