def sumOfDigits(n):
    product = 0
    while n >= 1:
        product += (n % 10) ** 5
        n //= 10
    
    return product

sum = 0
for i in range(2, 354295): # 354294 is 9^5 x 6
    p = sumOfDigits(i)

    if p == i:
        sum += p

print(sum)