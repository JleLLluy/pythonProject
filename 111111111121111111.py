solution = []
g = 8
for d in range(30):
    for a in range(30):
        for b in range(30):
            for g in range(30):
                if a + b + v + g + d == 30 and b + g == a + v + d and a == v + d:
                    print(str(a) + '_' + str(b) + '_' + str(v) + '_' + str(g) + str(d))