import math

primeNumbers = [2, 3]

def isPrime(n):
  i = 0
  while primeNumbers[i] <= math.sqrt(n):
    if n % primeNumbers[i] == 0:
      return False
    
    i += 1

  return True

n = 3
while len(primeNumbers) < 10001:
  n += 2

  if isPrime(n):
    primeNumbers.append(n)

print(n)