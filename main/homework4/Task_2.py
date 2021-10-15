import re


# 1
def write_number():
    while True:
        try:
            number = float(input('Write number: '))
        except ValueError as error:
            print(error, "!!! Try again !!!")
        else:
            return number


# 2
def space_remove(string):
    return string.strip()


# 3
def what_a_triangle(sideA, sideB, sideC):
    if sideA + sideB > sideC and sideB + sideC > sideA and sideA + sideC > sideB:
        if sideA == sideB == sideC:
            return print('Equilateral triangle')
        elif sideA == sideB or sideB == sideC or sideA == sideC:
            return print('Isosceles triangle')
        else:
            return print('Versatile triangle')
    else:
        return print('Not a triangle')


# 4
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


# 5.1
def remove_not_a_string(string):
    newString = ''
    for i in string:
        if i.isalpha():
            newString += i
    return newString


# 5.2
def remove_not_a_Latin_re(string):
    return re.sub("[^a-zA-Z]", "", string)

