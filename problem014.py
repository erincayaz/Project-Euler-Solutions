from functools import lru_cache

@lru_cache(None)
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)

max_count = 1
max_number = 1
for i in range(1, 1000000):
    c = collatz(i)
    if c > max_count:
        max_count = c
        max_number = i

print(max_number)