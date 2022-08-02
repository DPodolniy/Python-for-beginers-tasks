from math import sqrt


def solve(a, b, c):
    x1, x2 = 0, 0
    d = b**2 - (4 * a * c)
    if d > 0:
        x1 = (b * -1 + sqrt(d)) / (2 * a)
        x2 = (b * -1 - sqrt(d)) / (2 * a)
    return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = 1, -4, -5

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)