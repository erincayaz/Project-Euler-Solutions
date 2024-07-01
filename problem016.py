import math

n = str(int(math.pow(2, 1000)))
sum = 0
for digit in n:
  sum += int(digit)

print(sum)
