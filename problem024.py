import math

MAX_NUMBER_OF_PERMUTATION = 1000000

cur_permutation = ""
number_of_permutation = 0
i = 9
cur_number = 0
while len(cur_permutation) < 10:
    temp_number_permutation = number_of_permutation + math.factorial(i)
    if temp_number_permutation < MAX_NUMBER_OF_PERMUTATION:
        cur_number += 1
        while str(cur_number) in cur_permutation:
            cur_number += 1

        number_of_permutation = temp_number_permutation
    elif temp_number_permutation >= MAX_NUMBER_OF_PERMUTATION:
        cur_permutation += str(cur_number)
        cur_number = 0
        i -= 1

print(cur_permutation)
