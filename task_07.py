def convert_fahrenheit_to_celsius(temperature):
    temperature = 0.56 * temperature - 17.92

    return temperature


def convert_celsius_to_fahrenheit(temperature):
    temperature = 1.80 * temperature + 32

    return temperature


if __name__ == "__main__":
    print(convert_fahrenheit_to_celsius(77))
    print(convert_celsius_to_fahrenheit(25))
