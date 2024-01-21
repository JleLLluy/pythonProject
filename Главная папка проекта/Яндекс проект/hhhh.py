f = []
g = [[0, 0, 0]]
n = True
for a in range(12):
    f.clear()
    n = True
    f.append(a)
    for b in range(12):
        f.append(b)
        for c in range(12):
            f.append(c)
            f = sorted(f)
            for i in g:
                if f == i:
                    n = False
            if n:
                g.append(f)
print(len([' '.join(map(str, x)) for x in g]))

