# Sisendiks üks sõna / fraas
# Funktsiooni väljundiks peab tulema uus sõna / fraas,
# kus esimene ja viimane täht on vahetunud


def swap_first_last(text):
    mid = text[1:-1]
    first = text[0]
    last = text[-1]

    return "{0}{1}{2}".format(last, mid, first)



x = "Maja"
y = "Loodus"
z = "Linn"

a = "lammas"
b = "aias"

print(swap_first_last(x))

print(swap_first_last(y))

print(swap_first_last(z))

print(swap_first_last(a))

print(swap_first_last(b))
