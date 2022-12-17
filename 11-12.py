#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def funcFromExp(s:str):
	func = s.replace("Operation:","lambda").replace("=",":").replace("old","new")
	return eval(func)

text = read_file('input.txt')
MonkeyT = dict[str, any]
MonkeysT = list[MonkeyT]
Monkeys = MonkeysT()
current = 0
for line in text:
	words = line.split()
	# print(words)
	if len(words) == 0:
		current += 1
	elif words[0] == "Monkey":
		Monkeys.append(MonkeyT({"insp":0}))
	elif words[0] == "Starting":
		Monkeys[current]["items"] = [int(x) for x in [y.strip(',') for y in words[2:]]]
	elif words[0] == "Operation:":
		Monkeys[current]["op"] = funcFromExp(line)
	elif words[0] == "Test:":
		Monkeys[current]["test"] = int(words[-1])
	elif words[1] == "true:":
		Monkeys[current]["true"] = int(words[-1])
	elif words[1] == "false:":
		Monkeys[current]["false"] = int(words[-1])

# print(Monkeys)
# print(text)
rounds = 10000
# rounds = 20
while rounds > 0:
	for m in Monkeys:
		# print("Monkey",Monkeys.index(m), m["items"])
		for i in m["items"]:
			m["insp"] += 1
			# print("old:",i)
			new = m["op"](i)
			# print("new",new)
			# new //= 3
			# print("new3", new)
			# print("test", new%m["test"] == 0)
			Monkeys[m["true"] if new%m["test"] == 0 else m["false"]]["items"].append(new)
			# print(new,"to",m["true"] if new%m["test"] == 0 else m["false"])
		
		m["items"] = []

	rounds -= 1
	# print()
	# [print("Monkey", i, Monkeys[i]["items"]) for i in range(len(Monkeys))]
	print(rounds, [m["insp"] for m in Monkeys])

def part1(x:list):
	best = 0
	best2 = 0
	i = 0
	while i < len(x):
		if x[i] > best:
			best2 = best
			best = x[i]

		elif x[i] > best2:
			best2 = x[i]

		i += 1
	
	return best * best2

print(part1([m["insp"] for m in Monkeys]))