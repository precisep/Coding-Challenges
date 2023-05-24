def find_maximum_number(*args):
    maximum_num = float('-inf')

    for num in args:
        if num > maximum_num:
            maximum_num = num
    return maximum_num


if __name__ == "__main__":
    print(f"Maximum number: {find_maximum_number(1,22,3)}")
    print(f"Bonus function maximum number: {find_maximum_number(56,12,89,0,-4)}")
