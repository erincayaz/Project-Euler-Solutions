# Formula used:
# ---------------------------------------
# Total number of natural numbers between (a, b): (b - a) / d + 1
# d is the difference between two consecutive numbers
# ---------------------------------------
# Sum of all numbers between (a, b): ((a + b) * n) / 2
# n is number of natural numbers between (a, b)

sum = ((3 + 999) * ((999 - 3) / 3 + 1) + (5 + 995) * ((995 - 5) / 5 + 1) - (15 + 990) * ((990 - 15) / 15 + 1)) / 2

print(int(sum))