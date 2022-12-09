#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

total = 0
text = read_file('input.txt')
for line in text:
	[[d1, f1], [d2, f2]] = [x.split('-') for x in line.split(',')]
	print(d1,f1,d2,f2)
	if (set(range(int(d1), int(f1)+1)) & set(range(int(d2), int(f2)+1))):
		total += 1
		print("oui")

print(total)