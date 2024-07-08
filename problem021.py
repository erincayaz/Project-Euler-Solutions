import math

def sumOfAllDivisors(n):
    d = {1}

    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            d.add(i)
            d.add(n // i)

        i += 1
    
    sum = 0
    for i in d:
        sum += i

    return sum


i = 4
amicable_numbers = {0}
while i < 10000:
    s = sumOfAllDivisors(i)
    if s == i:
        i += 1
        continue

    s2 = sumOfAllDivisors(s)

    if i == s2:
        amicable_numbers.add(i)
        amicable_numbers.add(s)

    i += 1

sum = 0
for i in amicable_numbers:
    sum += i
