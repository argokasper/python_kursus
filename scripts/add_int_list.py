
# for loop'i, igal ringil kokku liita praegune element eelmise summaga
def add_int_list(numbers: list, show_step_calc = False):
    """Liidab kokku järjest listis olevaid täisarve.Nt [1, 2, 3, 4, 5, 6, 7] => 28
        Nt koos show_step_calc = True'ga,
        [1, 2, 3, 4, 5, 6, 7]
        print(1) # 1
        print(3) # 3
        print(6) # 6
        print(10) # 10
        print(15) # 15
        print(21) # 21
        print(28) # 28

        print("Summa on: 28") # Summa on: 28

    Args:
        numbers (list): _description_
        show_step_calc (bool, optional): Kui on True, siis kuvad iga tehte vastus terminali. Defaults to False.
    """
    sum = 0
    for number in numbers:
        sum += number
        if show_step_calc:
            print(f"Vahesumma on: {sum}")

    return sum



print(add_int_list([1, 2, 3, 4, 5, 6, 7])) # 28
print(add_int_list([1, 2, 3, 4, 5, 6, 7], True))
