import math

# Will use combination for this problem:
# There are 40 steps to be taken and 20 of them will be right
# So the problem is how many different combinations I have for choosing the right step
# For 2x2, 4 steps will be taken and 2 of them will be right step, so when I compute its combination:
# RRDD RDRD RDDR DRRD DRDR DDRR, we see that combination formula holds

print(math.comb(40, 20))