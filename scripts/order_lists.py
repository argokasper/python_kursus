
# Eesmärk: skript, mis sorteerib liste
# Tsüklid, if-else, input, casts

# 1. Luua võimekus skriptile ette anda erinevaid sisendeid - TEHTUD
# 2. Tuvastada ära, mis tüüpi (int või str) listiga on tegu. Loome selle jaoks funktsiooni - TEHTUD
# 3. Luua funktsioon, mis tekitab sisendist listi - TEHTUD
# 4. Luua funktsioon, mis sorteerib numbreid  TEHTUD
# 5. Luua funktsioon, mis sorteerib tekste - ei tee
# 6. Printida välja sorteeritud list - TEHTUD

# Funktsioon, mis tuvastab elementide tüübi etteantud sisendist
def detect_list_type(input):
    for letter in input:
        if letter == " " or letter == ",":
            continue

        try:
            checked_letter = int(letter)
        except:
            checked_letter = str(letter)

        if isinstance(checked_letter, int):
            return "int" # hüpatatakse tsüklist välja ning tagastatakse "int"
        else:
            return "str" # hüpatatakse tsüklist välja ning tagastatakse "str"

# Funktsioon, mis võtab sisendiks etteantud teksti ning väljasb sellest listi
def parse_list(input):
    raw_nimekiri = str(input).split(",") # "1, 3, 4, 5, 6" => ["1", " 3", " 4"]
    nimekiri = []
    for element in raw_nimekiri:
        stripped_element = element.strip()
        nimekiri.append(stripped_element)

    return nimekiri

def order_int_list(input_list):
    ordered_list = []
    lowest = None
    for i, x in enumerate(input_list):
        for j, y in enumerate(input_list):
            current_y = int(y)
            if i == j or current_y in ordered_list:
                continue

            if lowest == None or current_y < lowest:
                lowest = current_y

        ordered_list.append(lowest)
        lowest = None
        # input_list.remove(y) # ei kõlba, kuna kaotame indekseid orig. listist
        # return ordered_list


    return ordered_list


sisend = input("Sisesta komaga eraldatud nimekiri väärtustest (ainult tekstid või numbrid, mitte läbisegi): ")
print(detect_list_type(sisend))

list_sisend = parse_list(sisend)
tyyp = detect_list_type(sisend)

if tyyp == "int":
    print(order_int_list(list_sisend))


test = [45, -23, 1, 0, -34, 100]
test.sort()
print(test)
print('test')
