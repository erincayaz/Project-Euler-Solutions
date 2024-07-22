sum = 0
for i in range(1001, 1, -2):
    for j in range(4):
        sum += i**2 - j * (i - 1)

print(sum + 1)