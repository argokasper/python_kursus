import mass_inputs

# funktsioon, mis võtab vastu kaks argumenti (mõlemad on int)
# need kaks numbrit liidetakse alati kokku
# va kui on kaks ühesugust arvu add(5, 5) => 1. liidame kokku 2. võtame vastuse ruutu

def add(a, b):
    if a == b:
        sum = a + b
        print('Võrdsed liidetavad [{0}]'.format(a))
        return sum * sum

    return a + b



mass_inputs.randomInputs(add)