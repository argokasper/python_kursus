# Listide liitmine valitud indeksi kohale
# kaks listi [1, 4, 6], [12, 46, 3]
# liidame teise listi esimesse listi kohale indeks=1  (teine element: 0, 1, 2, ....)

def concat_lists(list1, list2, position = 0):
    tmp_list = list(list1) # list() - see on vajalik, et kopeerida 'list1' uuele muutujale ka mälus
    elements_from_position = tmp_list[position:]
    tmp_list[position] = list2
    tmp_list[position + 1:] = elements_from_position

    final_list = []

    for element in tmp_list:
        if isinstance(element, list):
            for sub_element in element:
                final_list.append(sub_element)
        else:
            final_list.append(element)

    return final_list



first = [1, 34, 65, 23, 97, 44]
second = ['car', 'house', 'park', 'bird', 'animal']

print(concat_lists(first, second))
print(concat_lists(first, second, 2))
