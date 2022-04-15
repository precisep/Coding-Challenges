def check_for_65_or_equivalent_sum(first_number, second_number):

    if first_number == 65 or second_number == 65 or sum([first_number, second_number]) == 65:
        return print(True)
    else:
        return print(False)
