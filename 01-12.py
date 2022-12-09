elves = []
i = 0
# input while
while True:
    try:
        x = input()
        if x != "":
            i += int(x)
        else:
            elves.append(i)
            i = 0
    except:
        break

print(elves)

total3 = 0
top1 = max(elves)
print(top1)
total3 += top1
elves.pop(elves.index(top1))
top2 = max(elves)
print(top2)
total3 += top2
elves.pop(elves.index(top2))
top3 = max(elves)
print(top3)
total3 += top3
print(total3)
