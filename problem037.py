def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(n ** 0.5) + 1
    for i in range(3, r, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if len(s) == 1:
        return False
    
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    
    for i in range(len(s)):
        if not is_prime(int(s[:len(s)-i])):
            return False
    return True

truncatable_primes = []
n = 11
while len(truncatable_primes) < 11:
    if is_prime(n) and is_truncatable_prime(n):
        truncatable_primes.append(n)
    n += 2

result = sum(truncatable_primes)
print("Truncatable primes:", truncatable_primes)
print("Sum:", result)