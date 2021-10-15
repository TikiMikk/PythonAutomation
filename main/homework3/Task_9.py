# 1
def is_leap_year(number):
    if (number % 4 == 0 and number % 100 != 0) or number % 400 == 0:
        return True
    else:
        return False


yourNumber = int(input('Write number: '))

print(is_leap_year(yourNumber))


# 2
def is_triangle(sideA, sideB, sideC):
    if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
        return True
    else:
        return False


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(is_triangle(a, b, c))
