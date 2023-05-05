def find_maximum_number(first_number, second_number, third_number):
   
    maximum_num = first_number

    if second_number > maximum_num:
        maximum_num = second_number
    if third_number > maximum_num:
        maximum_num = third_number
    return maximum_num

def bonus_find_maximum_number(*args):
    maximum_num = args[0]
    for num in args[1:]:
        if num > maximum_num:
            maximum_num = num
    return maximum_num

if __name__ == '__main__':
    print(f'Maximum number: {find_maximum_number(1,22,3)}')
    print(f'Bonus function maximum number: {bonus_find_maximum_number(56,12,89,0,-4)}')

    


    
