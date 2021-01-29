def powerful(x: int, y: int, bound: int) -> []:
    h = set()
    for i in range(20):
        for j in range(20):
            v = x**i + y**j
            if v <= bound:
                h.add(v)
    return h



x = 3
y = 5
bound = 15

print(powerful(x,y, bound))

