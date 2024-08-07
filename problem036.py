sum = 0
for i in range(1000000):
    d_n = str(i)
    b_n = bin(i)[2:]

    if d_n == d_n[::-1] and b_n == b_n[::-1]:
        sum += i

print(sum)