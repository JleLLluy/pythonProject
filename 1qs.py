strochka = input()
simbol = strochka[0]
count = 0
last = ''
count_symbol = 1
for i in range(1, len(strochka) + 1):
    if strochka[i] == '>':
        count_symbol += 1
        last = '>'
    elif strochka[i] == '<':
        count_symbol += 1
        count -= 1
    elif strochka[i] == 'V':
        print(count * ' ' + count_symbol * simbol)
        if last == '>':
            count += count_symbol - 1
            last = ''
        count_symbol = 1