def calculated_area(base, height, shape):
    if shape == "rectangle":
        area = base * height
        return area
    else:
        area = (1/2) * base * height
        return area


def print_pattern(i):
    for m in range(1, i+1):
        print('*'*m)


pole = calculated_area(5, 3, "ectangle")
print(pole)
print_pattern(5)
