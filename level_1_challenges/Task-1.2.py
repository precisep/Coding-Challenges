def check_for_3_or_multiples(first_number,second_number):

    if (first_number == 3 or second_number == 3) and ((sum([first_number, second_number])) % 3 == 0):
        return print(True)
    else:
         return print(False)

