# Ülesanne
# 1. Loome 4 funktsiooni: liida, lahuta, korruta, jaga - TEHTUD
# 2. Loome inputid kahe arvu jaoks: input(), jälgige andmetüüpe! - TEHTUD
# 3. Loome liida() funktsiooni sisu: see funktsioon
#    võtab vastu 2 parameetrit - TEHTUD
# 4. Loome lahuta() funktsiooni sisu - TEHTUD
# 5. Loome funktsiooni sisud ka korruta() ja jaga() funktsioonidele - TEHTUD
# 6. Kutsume välja kõik loodud funktsioonid - TEHTUD
# 7. Kuvame kõikide tehete vastused (funtsioonide tulemused) skripti lõpus: print() - TEHTUD

def liida(x, y):
    sum = x + y
    return sum

def lahuta(x, y):
    substract = x - y
    return substract

def korruta(x, y):
    multiply = x * y
    return multiply

def jaga(x, y):
    divide = x / y
    return divide

#on vaja cast'ida arvutüübiks: int, float, complex
arv1 = float(input('Sisesta esimene arv: '))
arv2 = float(input('Sisesta teine arv: '))

summa = liida(arv1, arv2)
lahutis = lahuta(arv1, arv2)
korrutis = korruta(arv1, arv2)
jagatis = jaga(arv1, arv2)

print('Summa on: ' + str(summa))
print('Lahutis on: ' + str(lahutis))
print('Korrutis on: ' + str(korrutis))
print('Jagatis on: ' + str(jagatis))