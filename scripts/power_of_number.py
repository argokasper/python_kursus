# funktsioon, mille sisenditeks on baasarv ja astendaja
# ja väljundiks on astendus(vastus), power(2, 2) => 4, power(3,3) => 27, power(5,2) => 25

def power(base, pow):
    result = base ** pow
    return result

def power_alt(base, pow):
    result = base
    for i in range(1, pow):
        result *= base
    return result

print(power(2, 2))
print(power(3, 3))
print(power(2, 5))
print(power(5, 2))
print(power(4, 3))
print(power(6, 2))

print('-----')

print(power_alt(2, 2))
print(power_alt(3, 3))
print(power_alt(2, 5))
print(power_alt(5, 2))
print(power_alt(4, 3))
print(power_alt(6, 2))