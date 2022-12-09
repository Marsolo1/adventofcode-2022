#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
group = 0
letters = {}
for line in read_file('input.txt'):
	if group%3 == 0:
		letters = {}
		for char in line:
			letters[char] = 0
	elif group%3 == 1:
		for char in line:
			if char in letters:
				letters[char] = 1
	else:
		for char in line:
			if letters.get(char,0) == 1:
				letters[char] = 2
		total += alphabet.index(max(letters, key=letters.get)) + 1
	group += 1


# print(read_file('input.txt'))
print(total)