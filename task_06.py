def maximum(*args):
    maximum_num = float('-inf')

    for num in args:
        if num > maximum_num:
            maximum_num = num
    return maximum_num


if __name__ == "__main__":
    print(f"Maximum number: {maximum(1,22,3)}")
    print(f"Maximum number: {maximum(56,12,89,0,-4)}")
