#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip("\n") for line in f]

def get_lists(text, i):
	len  = int(text[i][-2])
	res = []
	for j in range(len):
		index = 1 + j * 4
		pile = []
		x = 1
		while x <= i and text[i-x][index] != " ":
			pile.append(text[i-x][index])
			x += 1
		res.append(pile)
	return res

text = read_file("input.txt")
i = 0
for line in text:
	if i != -1:
		if line == "":
			piles = get_lists(text, i-1)
			i = -1
		else:
			i+=1
	else:
		a, b, c = [int(line.split()[i]) for i in [1, 3, 5]]
		tmp = piles[b-1][-a:]
		del piles[b-1][-a:]
		[piles[c-1].append(e) for e in tmp]
		
	
final = ""
for pile in piles:
	final += pile[-1]

print(final)
# print(read_file('input.txt'))