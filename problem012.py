import math

def prime_factors(n):
    factors = {}
    count = 0

    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors[2] = count

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factors[i] = count

    if n > 2:
        factors[n] = 1
    
    return factors

def number_of_divisors(n):
    factors = prime_factors(n)
    divisor_count = 1
    for count in factors.values():
        divisor_count *= (count + 1)
    return divisor_count

def find_triangle_with_divisors(min_divisors):
    n = 1
    i = 2

    while number_of_divisors(n) <= min_divisors:
        n += i
        i += 1

    return n

result = find_triangle_with_divisors(500)
print(result)