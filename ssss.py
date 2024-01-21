sp = {}
n = int(input())
for i in range(n):
    name = input().split()
    if name[2] in sp:
        sp[name[2]].append([name[0], name[1]])
    else:
        sp[name[2]] = [[name[0], name[1]]]
num = int(input())
arr = [input() for _ in range(num)]
for word in arr:
    if word in sp:
        arr = sorted(sp[word], key=lambda x:
(int(x[1]), x[0]))
 st = ''
 for x in arr:
 st += ' '.join(x) + ' '
 print(st.rstrip())
 if word not in sp:
 print(