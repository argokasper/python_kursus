# Kaks sisendit, int tüüpi
# Kui üks arvudest on 10, siis prindime/return'ime välja "JEE!"
# Kui kahe arvu summa on 10, siis prindime/return'ime välja "SUMMA!"
import mass_inputs

def special_10(a, b):
    if  a == 10 or b == 10:
        # print('JEE!')
        return 'JEE!'

    sum = a + b

    if sum == 10:
        # print('SUMMA!')
        return 'SUMMA!'



mass_inputs.randomInputs(special_10)
