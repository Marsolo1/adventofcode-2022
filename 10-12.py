#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def exe(inst):
	global X
	RAM["inst"] = inst[0]
	if inst[0] == "addx":
		RAM["busy"] += 2
		RAM["value"] = int(inst[1])
	elif inst[0] == "noop":
		RAM["busy"] += 1
	else:
		return

def draw(Screen, num, X):
	id = num % len(Screen[0])
	if id in [X-1,X,X+1]:
		Screen[row] = Screen[row][:id] + "#" + Screen[row][id+1:]

text = read_file('input.txt')

X = 1
num = 0
cycle = 40
# cycle = 20
total = 0

RAM = {"busy":0, "inst":None, "value":0}


Screen = ["."*40]*6
row = 0
i = 0
while i < len(text):
	line = text[i]
	if RAM["busy"] > 0:
		RAM["busy"] -= 1
		draw(Screen,num,X)
		num += 1
	
	else:
		if RAM["inst"] == "addx":
			X += RAM["value"]
		inst = line.split()
		exe(inst)
		i += 1

	if num == cycle:
		cycle += 40
		# print(X)
		# total += num * X
		row += 1

# print(total)

for line in Screen:
	print(line)