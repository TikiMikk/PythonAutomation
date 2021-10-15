# 1)
def delete_list_first_numbers(array):
    while len(array) > 0:
        print(array.pop(0))


# 2) **
def delete_list_first_strings(string):
    array = list(string)
    print(array)
    while len(array) > 0:
        print(array.pop(0))


# 3)
def delete_min_values(array):
    while len(array) > 0:
        array.sort()
        print(array[0])
        array.remove(array[0])


# 4) **
def duplicate_array_values(array):
    length, newLength, duplicateLength = 1, 1, 1
    first, newFirst, duplicateFirst = 0, 0, 0

    for index, el in enumerate(array):
        if array[index] == array[index - 1]:
            if length == 1:
                first = index - 1
            length += 1
            if length > newLength:
                newLength = length
                newFirst = first
            elif length == newLength:
                duplicateLength = length
                duplicateFirst = first
        else:
            length = 1

    mainResult = array[newFirst:newFirst + newLength]

    if duplicateLength == newLength:
        duplicate = array[duplicateFirst:duplicateFirst + duplicateLength]

        return {'Values': [mainResult, duplicate],
                'Indexes': [str(newFirst) + ':' + str(newFirst-1 + newLength),
                            str(duplicateFirst) + ':' + str(duplicateFirst-1 + duplicateLength)],
                'Length': newLength}
    else:
        return {'Value': mainResult,
                'Indexes': str(newFirst) + ':' + str(newFirst-1 + newLength),
                'Length': newLength}




