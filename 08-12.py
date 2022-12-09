#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def visible(i, j, d):
	if i == 0 or j == 0 or i == n-1 or j == n-1:
		return True

	a = int(text[i][j])
	if d == 0:
		j+=1
		while j < n:
			if a <= int(text[i][j]):
				return False
			
			j += 1

	elif d == 1:
		i+=1
		while i < n:
			if a <= int(text[i][j]):
				return False
		
			i += 1

	elif d == 2:
		j-=1
		while j >= 0:
			if a <= int(text[i][j]):
				return False
		
			j -= 1

	elif d == 3:
		i-=1
		while i >= 0:
			if a <= int(text[i][j]):
				return False
		
			i -= 1
	
	return True

def score(i, j, d):
	a = int(text[i][j])
	vis = 0
	if d == 0:
		j+=1
		while j < n:
			vis += 1
			if a <= int(text[i][j]):
				return vis
			j += 1

	elif d == 1:
		i+=1
		while i < n:
			vis += 1
			if a <= int(text[i][j]):
				return vis
		
			i += 1

	elif d == 2:
		j-=1
		while j >= 0:
			vis += 1
			if a <= int(text[i][j]):
				return vis
		
			j -= 1

	elif d == 3:
		i-=1
		while i >= 0:
			vis += 1
			if a <= int(text[i][j]):
				return vis
		
			i -= 1
	
	return vis

text = read_file('input.txt')
n = len(text)
total = 0
i=0
while i < len(text):
	j = 0
	while j < len(text):
		# if visible(i, j, 0) or visible(i, j, 1) or visible(i, j, 2) or visible(i, j, 3):
		# 	total += 1
		vision = score(i, j, 0) * score(i, j, 1) * score(i, j, 2) * score(i, j, 3)
		if vision > total:
			total = vision

		j += 1
	
	i+= 1

# print(text)
print(total)