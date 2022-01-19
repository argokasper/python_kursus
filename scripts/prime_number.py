
start = int(input('Sisesta algus: '))
end = int(input('Sisesta lõpp: '))

if start > end:
    print('Algus peab olema väiksem lõpust')
    exit

for x in range(start, end):
    if x > 1:
        for divider in range(2, x):
            if x % divider == 0:  # 4 % 3  == 1  5 % 3 == 2
                break
        else:
            print(x)
