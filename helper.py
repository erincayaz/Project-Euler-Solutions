import math

def getAllDigitsOfNumber(n):
    arr = []
    while n != 0:
        arr.insert(0, n % 10)
        n //= 10

    return arr

def isPrime(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        
        i += 2

    return True