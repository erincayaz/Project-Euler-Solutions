import math
from functools import lru_cache
from datetime import datetime

@lru_cache(None) # Not neccessary but makes the execution time faster
def isPrime(n):
    if n % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
    
        i += 2

    return True

max_count = 0
max_product = 0
for i in range(-999, 1000, 2):
    for j in range(-999, 1000, 2):
        k = 0
        while True:
            cur_value = k**2 + i*k + j
            if cur_value > 0 and isPrime(cur_value):               
                k += 1
            else:
                if k > max_count:
                    max_count = k
                    max_product = i * j

                break


print(max_product)
  