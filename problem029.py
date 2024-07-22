all_numbers = set()
for i in range(2, 101):
    for j in range(2, 101):
        all_numbers.add(i**j)

print(len(all_numbers))