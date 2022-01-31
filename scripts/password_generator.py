# Ülesanne: genereeri random password etteantud pikkusega

# 0. Luua input, millega saame ette anda vajliku parooli pikkuse
# 1. Funktsioon, kus luuakse n-pikkusega tekst, kasutadaes tsüklit  (for in range())
# ja iga sümbol selles paroolis on suvaline

import random


def generate_password(length):
    password = ''
    for i in range(length): # sama nagu range(0, length)
        # tähe/sümboli/numbri leidmiseks ascii aadressi järgi, tuleb kasutada chr(number) funkts.
        # range = [48-110]
        # range = [48-55], [60-120]
        password += chr(random.randint(35, 120))

    return password

length = int(input('Sisesta parooli pikkus: '))
amount = int(input('Mitu parooli soovid saada? ')) # Lisaülesanne, luua võimalus printida korraga rohkem kui 1 parool

for i in range(amount):
    password = generate_password(length)

    print(password)

