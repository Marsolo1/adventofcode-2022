#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

game = read_file('input.txt')

rpc1 = ['A', 'B', 'C']
rpc2 = ['X', 'Y', 'Z']

def victory(i, j):
	if i == 'A' and j == 'X':
		return 3
	elif i == 'A' and j == 'Y':
		return 6
	elif i == 'A' and j == 'Z':
		return 0
	elif i == 'B' and j == 'X':
		return 0
	elif i == 'B' and j == 'Y':
		return 3
	elif i == 'B' and j == 'Z':
		return 6
	elif i == 'C' and j == 'X':
		return 6
	elif i == 'C' and j == 'Y':
		return 0
	elif i == 'C' and j == 'Z':
		return 3

def choose(i, j):
	if j == 'X':
		return (rpc1.index(i) - 1) % 3 + 1
	elif j == 'Y':
		return rpc1.index(i) + 4
	elif j == 'Z':
		return (rpc1.index(i) - 2) % 3 + 7

score = 0
for g in game:
	score += choose(g[0], g[2])
	# score += rpc2.index(g[2]) + 1

print(score)