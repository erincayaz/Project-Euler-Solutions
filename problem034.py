import math
import helper

factorials = [math.factorial(i) for i in range(10)]
UPPER_BOUND = 2540160
sum_factorials = 0
for i in range(10, UPPER_BOUND + 1):
    all_digits = helper.getAllDigitsOfNumber(i)
    
    sum = 0
    for d in all_digits:
        sum += factorials[d]
        if sum > i:
            break

    if sum == i:
        sum_factorials += i

print(sum_factorials)