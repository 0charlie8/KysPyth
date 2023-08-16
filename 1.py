def main(x, y):
    one = y / 25
    two = pow((81 * y ** 2) - (91 * x ** 3), 2)
    third = pow(47 * (1 + 54 * x**2 + y ** 3), 7)\
        + 4 * (math.sqrt(x)**6)
    f = pow(math.atan(x), 3) + one + two / third
    return f
