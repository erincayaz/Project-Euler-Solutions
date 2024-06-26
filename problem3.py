num = 600851475143
i = 1

while True:
    if num % i == 0:
        num = num / i
        if i > num:
            break
    i += 2

print(i)