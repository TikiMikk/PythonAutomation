def pre_max(arrayNumbers):
    try:
        arrayNumbers.sort()
        maxNumb = arrayNumbers[-1]
    except TypeError as error:
        return arrayNumbers, error
    except IndexError:
        return arrayNumbers

    while True:
        if maxNumb in arrayNumbers:
            arrayNumbers.remove(maxNumb)
        elif len(arrayNumbers) == 0:
            return arrayNumbers
        else:
            return arrayNumbers[-1]
