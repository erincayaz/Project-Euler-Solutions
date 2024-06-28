import math

primeNumbers = [2, 3]

def isPrime(n):
  i = 0
  while primeNumbers[i] <= math.sqrt(n):
    if n % primeNumbers[i] == 0:
      return False
    
    i += 1

  return True

sum = 5
for i in range(5, 2000000, 2):
  if isPrime(i):
    primeNumbers.append(i)
    sum += i

print(sum)