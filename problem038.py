def is_pandigital(s):
  return len(s) == 9 and set(s) == set('123456789')

max_number = 0
for i in range(1, 10000):
    concatenated = ''
    j = 1
    while len(concatenated) < 9:
        concatenated += str(i * j)
        j += 1
    if is_pandigital(concatenated):
        num = int(concatenated)
        if num > max_number:
            max_number = num

print("Max pandigital number is:", max_number)