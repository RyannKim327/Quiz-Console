import base64

while True:
	a = input("Enter text: ")
	b = a.encode('ascii')
	c = base64.b64encode(b)

	print(f"Output: {c}")