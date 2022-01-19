import random # https://www.w3schools.com/python/module_random.asp


def helloWorld():
    print('Hello world!')

# helloWorld() # nüüd kutsume välja funktsiooni



# Väljundiga funktsioon
def printRandomNumbers():
    number = random.randint(1, 30)
    print('Suvaline number on: ' + str(number))
    return number

# printRandomNumbers()

# funktsiooni_vaartus = printRandomNumbers()
# print('Siin on randomiks: ' + str(funktsiooni_vaartus))




def compareIntegers(num1, num2):
    if num1 > num2:
        # print('Esimene arv on suurem kui teine')
        return 1
    elif num1 < num2:
        # print('Esimene arv on väisem kui teine')
        return -1
    else:
        # print('Arvud on võrdsed')
        return 0



for n in range(0, 10):
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)

    output = compareIntegers(random1, random2)
    if output > 0:
        print('Esimene arv(' + str(random1) + ') on suurem kui teine(' + str(random2) + '). output=' + str(output))
    elif output < 0:
        print('Esimene arv(' + str(random1) + ') on väisem kui teine(' + str(random2) + '). output=' + str(output))
    else:
        print('Arvud on võrdsed(' + str(random1) + '). output=' + str(output))



