def triangle_area(first_side, second_side, third_side):
    semiperimeter = (1 / 2) * (first_side + second_side + third_side)

    area = (
        semiperimeter
        * (
            (semiperimeter - first_side)
            * (semiperimeter - second_side)
            * (semiperimeter - third_side)
        )
    ) ** (1 / 2)

    return area


if __name__ == "__main__":
    print(triangle_area(7, 7, 7))
