import random
from random import choice
from string import ascii_uppercase


def generate_random_string(stringLength):
    return ''.join(choice(ascii_uppercase) for i in range(stringLength))


def generate_random_integer_list(arrayLength, minRange=-10, maxRange=10):
    array = []
    for i in range(arrayLength):
        array.append(random.randint(minRange, maxRange))

    return array


def find_min(yourArray):
    minimum = yourArray[0]
    for i in yourArray:
        if i < minimum:
            minimum = i
    return minimum
