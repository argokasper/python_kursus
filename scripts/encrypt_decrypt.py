
factor = 100000

def enrypt(input):
    encrypted = ''
    for letter in input:
        ascii_number = ord(letter)
        encrypted += chr(ascii_number + factor)

    return encrypted

def decrypt(encrypted_input):
    original = ''
    for encrypted_letter in encrypted_input:
        ascii_number = ord(encrypted_letter)
        original += chr(ascii_number - factor)

    return original

tekst = input('Siseta sõna: ')

encrypted_text = enrypt(tekst)
print(encrypted_text) # prindib välja sigri-migri

print(decrypt(encrypted_text)) # prindib välja originaal teksti
