import pandas

fail = pandas.read_excel('kategooriad.xlsx', 'Sheet1', skiprows=0) # Skipime päiserea, ehk alustame excel faili lugemist 2. reast


summad = {} # {'Toidukaubad': 30, 'Mänguasjad': 1000, ...}

for rida in range(0, fail.shape[0]):
    kategooria = fail.iat[rida, 0]
    summa = 0

    for tulp in range(1, fail.shape[1]):
        vaartus = fail.iat[rida, tulp]
        if summa == 0:
            summa = vaartus
        else:
            summa *= vaartus
    summad[kategooria] = summa
    summa = 0

print(summad)