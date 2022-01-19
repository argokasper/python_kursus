arv1 = int(input('Sisesta esimene arv: ')) # str
arv2 = int(input('Sisesta teine arv: '))

if arv1 > arv2: # '9' > '10'
    print('Esimene arv on väiksem kui teine')
elif arv1 == arv2:
    print('Arvud on võrdsed')
else:
    print('Teine arv on suurem kui esimene')

