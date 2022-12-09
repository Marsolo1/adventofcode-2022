#read each line of file in list and removes newline character
def read_file(filename:str)->list[str]:
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

def add_size(dir, p, size):
	cur = dir
	cur["size"] += size
	for i in range(len(p)):
		cur = cur[p[i]]
		cur["size"] += size

def get_dir(p):
	tmp = slash
	for i in range(len(p)):
		tmp = tmp[p[i]]
	return tmp

text = read_file('input.txt')
slash = {'size':0,'name':'slash'}
current = slash
path = []

for line in text:
	elms = line.split()
	if elms[0] == '$':
		if elms[1] == "cd":
			if elms[2] == "..":
				path.pop()
				current = get_dir(path)
			else:
				current[elms[2]] = current.get(elms[2], {"size":0, "name":elms[2]})
				current = current.get(elms[2])
				path.append(elms[2])

	elif elms[0] != "dir":
		add_size(slash, path, int(elms[0]))

def get_size(s, size):
	if len(s) == 1:
		return s["size"] if s["size"] <= size else 0
	else:
		total = s["size"] if s["size"] <= size else 0
		for elm in s:
			if elm != "size":
				total += get_size(s[elm], size)
		return total

checker = {"dir":"slash", "size":slash["size"]}
unused = 70000000-slash["size"]
needed = 30000000-unused
def get_smallest(s):
	if needed <= s["size"] <= checker["size"]:
		checker["size"] = s["size"]
		checker["dir"] = s["name"]

	if len(s) == 1:
		return
	else:
		for elm in s:
			if elm not in ["size", "name"]:
				get_smallest(s[elm])

# print(slash)
get_smallest(slash)
print(checker)
# print(get_size(slash, 100000))