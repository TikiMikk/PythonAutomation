a = int(input('Write a: '))
b = int(input('Write b: '))
c = int(input('Write c: '))

if a == b and b == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')
