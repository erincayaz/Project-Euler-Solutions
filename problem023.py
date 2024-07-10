def get_proper_divisors_sum(n):
    proper_divisors_sum = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            proper_divisors_sum += i
            if i != n // i:
                proper_divisors_sum += n // i
    return proper_divisors_sum

def is_abundant(n):
    return get_proper_divisors_sum(n) > n

abundant_numbers = [i for i in range(12, 28124) if is_abundant(i)]

abundant_sums = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum <= 28123:
            abundant_sums.add(abundant_sum)

non_abundant_sum = 0
for n in range(1, 28124):
    if n not in abundant_sums:
        non_abundant_sum += n

print(non_abundant_sum)
