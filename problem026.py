def isCycled(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    
    return n != 1

def cycleLen(n):
    remainders = {}
    value = 1
    i = 0
    while value not in remainders:
        remainders[value] = i
        value = (value * 10) % n
        i += 1

    return i - remainders[value]
            

max_cycle_len, max_cycle_num = 0, 0
for i in range(2, 1001):
    if isCycled(i):
        cycle_len = cycleLen(i)

        if cycle_len > max_cycle_len:
            max_cycle_len = cycle_len
            max_cycle_num = i

print(max_cycle_num)
