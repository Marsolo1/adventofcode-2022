#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def moveT(h, t):
	dx = h[0] - t[0]
	dy = h[1] - t[1]
	if abs(dx) == 2:
		t[0] += dx//abs(dx)
		if abs(dy) >= 1:
			t[1] += dy//abs(dy)

	elif abs(dy) == 2:
		t[1] += dy//abs(dy)
		if abs(dx) >= 1:
			t[0] += dx//abs(dx)



def move(d):
	if d == 'R':
		H[0] += 1
	elif d == 'D':
		H[1] += 1
	elif d == 'L':
		H[0] -= 1
	elif d == 'U':
		H[1] -= 1
	else:
		raise KeyError("mauvaise direction")

	for i in range(1,lrope):
		moveT(rope[i-1], rope[i])

text = read_file('input.txt')
places = set()
lrope = 10
rope = [[0,0] for i in range(lrope)]
H = rope[0]
T = rope[lrope-1]
for line in text:
	d, n = line.split()
	for _ in range(int(n)):
		move(d)
		places.add(tuple(T))

# print(places)
print(rope)
print(len(places))