import helper

def compute(arr):
    s = set()
    for i in arr:
        if i == 0 or i in s:
            return False
        else:
            s.add(i)
        
    return len(s) == 9
        
products = set()
sum = 0
for i in range(1, 10000):
    for j in range(1, 10000 // i):
        m = i * j
        arr = helper.getAllDigitsOfNumber(i) + helper.getAllDigitsOfNumber(j) + helper.getAllDigitsOfNumber(m)

        if m not in products and compute(arr):
            sum += m
            products.add(m)

print(sum)