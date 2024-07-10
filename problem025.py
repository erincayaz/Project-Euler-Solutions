prev, cur = 1, 1
i = 2
while len(str(cur)) < 1000:
    prev, cur = cur, prev + cur
    i += 1

print(i)