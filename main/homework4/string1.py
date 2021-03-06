def donuts(count):
    if count >= 10:
        count = 'many'
    return 'Number of donuts: {0}'.format(count)


def both_ends(s):
    return '' if len(s) <= 2 else s[:2] + s[-2:]


def fix_start(s):
    return s[0]+s[1:].replace(s[0], '*')


def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


def test(got, expected):
    if got == expected:
        prefix = ' OK'
    else:
        prefix = '  X'
    print(f'{prefix} | got: {got} | expected: {expected}')


def main():
    print('donuts')
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('\nboth_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('\nfix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print('\nmix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
    main()