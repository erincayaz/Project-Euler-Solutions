f = open("./input/0067_triangle.txt", "r")
b = f.read()

r = b.split('\n')
t = [[59]]
for i in range(1, len(r)):
    c = r[i].split(' ')
    nc = []
    for j in range(len(c)):
        if j == 0:
            nc.append(t[i - 1][0] + int(c[0]))
        elif j == len(c) - 1:
            nc.append(t[i - 1][j - 1] + int(c[j]))
        else:
            a = t[i - 1][j - 1] + int(c[j])
            b = t[i - 1][j] + int(c[j])

            nc.append(max(a, b))

    t.append(nc)

print(max(t[-1]))