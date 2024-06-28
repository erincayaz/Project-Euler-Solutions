sumEven = 2

prev = 2
cur = 3

while cur < 4000000:
  prev, cur  = cur, prev + cur

  if cur % 2 == 0:
    sumEven += cur

print(sumEven)