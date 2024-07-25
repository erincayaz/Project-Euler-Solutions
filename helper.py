def getAllDigitsOfNumber(n):
    arr = []
    while n != 0:
        arr.insert(0, n % 10)
        n //= 10

    return arr