def find_maximum_number(first_number, second_number, third_number):
    numbers = [first_number, second_number, third_number]

    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers[-1]


def bonus_find_maximum_number(*args):
    numbers = list(args)

    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers[-1]
