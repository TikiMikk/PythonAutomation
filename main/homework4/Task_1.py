def sum_or_concatenation(value1, value2):
    try:
        result = value1 + value2
    except TypeError:
        result = str(value1) + str(value2)
    return result


print(sum_or_concatenation(32, 'heh'))

