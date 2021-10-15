a = float(input('Write a: '))
b = float(input('Write b: '))
c = float(input('Write c: '))

while True:
    if a <= b <= c:
        break
    if b < a:
        a, b = b, a
    if c < b:
        b, c = c, b

print(a, b, c)

