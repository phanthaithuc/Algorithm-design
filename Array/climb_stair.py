n = 5
res = [0] * (n + 2)
res[0] = 1
res[1] = 1

for i in range(2, n + 1):
    res[i] = res[i - 1] + res[i - 2]

print(res[n])


def countway(n, m=2):
    temp = 0
    res = [1]
    for j in range(1, n + 1):
        s = j - m - 1
        e = j - 1
        if s >= 0:
            temp -= res[s]
        temp += res[e]
        res.append(temp)
    return res[n]


print(countway(5))
