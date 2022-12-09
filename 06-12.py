#read each line of file in list and removes newline character
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def check_rec(arr):
	n = len(arr)
	if n <= 1:
		return True
	if arr[0] in arr[1:n]:
		return False
	else:
		return check_rec(arr[1:n])


i = 0
mess_len = 14
line = read_file('input.txt')[0]
while i+mess_len <= len(line):
	if check_rec(line[i:i+mess_len]):
		i += mess_len
		break
	else:
		i += 1

print(i)
# print(read_file('input.txt'))