from tkinter import Tk, Label, Button, mainloop
from lists import sets
import random
import base64


score = 0
iterate = 0

def decrypt(stri=""):
	return str(base64.b64decode(stri.encode('ascii')).decode('ascii'))

def reset():
	global x
	global q
	global iterate
	global score
	iterate = 0
	score = 0
	q = sets().getSets()
	x = []
	y = 0
	while y < len(q):
		z = random.randint(0, len(q) - 1)
		if z in x:
			y -= 1
		else:
			x.append(z)
		y += 1
	_a.pack()
	_b.pack()
	_c.pack()
	_d.pack()
	ahead()

def ans(answ=5):
	global iterate
	global score
	y = x[iterate]
	if q[y].get("k") == answ:
		score += 1
	iterate += 1
	ahead()

def ahead():
	if iterate < len(x):
		z = x[iterate]
		r = decrypt(q[z].get("q"))
		_q.config(text=r)
		_a.config(text=decrypt(q[z].get("a")[0]))
		_b.config(text=decrypt(q[z].get("a")[1]))
		_c.config(text=decrypt(q[z].get("a")[2]))
		_d.config(text=decrypt(q[z].get("a")[3]))
	else:
		_q.config(text=f"You've got {score} over {len(x)} questions.")
		_a.config(text="Click again to start.", command=reset)
		_b.pack_forget()
		_c.pack_forget()
		_d.pack_forget()



def start():
	
	global _q
	global _a
	global _b
	global _c
	global _d
	global x
	global q
	global iterate
	global score

	frame = Tk()
	frame.title("Noli Me Tangere x El Filibustermismo")
	frame.geometry("500x500")

	width = 50
	q = sets().getSets()
	x = []
	y = 0
	while y < len(q):
		z = random.randint(0, len(q) - 1)
		if z in x:
			y -= 1
		else:
			x.append(z)
		y += 1

	_q = Label()
	_q.config(text="Question")
	_q.pack()
	
	_a = Button()
	_a.config(command=lambda: ans(0), width=width)
	_a.pack()
	
	_b = Button()
	_b.config(command=lambda: ans(1), width=width)
	_b.pack()

	_c = Button()
	_c.config(command=lambda: ans(2), width=width)
	_c.pack()

	_d = Button()
	_d.config(command=lambda: ans(3), width=width)
	_d.pack()

	ahead()

	mainloop()

start()