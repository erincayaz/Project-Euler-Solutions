f = open("./input/0022_names.txt", "r")
b = f.read()
arr = b.split(',')
arr.sort()

total_score = 0
for i in range(len(arr)):
    s = 0
    for j in arr[i]:
        if j == '\"':
            continue

        s += ord(j) - ord('A') + 1

    total_score += (i + 1) * s

print(total_score)
    