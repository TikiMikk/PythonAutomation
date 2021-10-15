number = int(input('Write number: '))

if (number % 4 == 0 and number % 100 != 0) or number % 400 == 0:
    result = 'YES'
else:
    result = 'NO'

