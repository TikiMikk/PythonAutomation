def match_ends(words):
    count = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count


def front_x(words):
    arr = []
    xArr = []
    for word in words:
        if word.startswith('x'):
            xArr.append(word)
        else:
            arr.append(word)
    return sorted(xArr) + sorted(arr)


def sort_last(tuples):
    newTuples = sorted(tuples, key=lambda newTuple: newTuple[-1])
    return newTuples


def test(got, expected):
    if got == expected:
        prefix = ' OK'
    else:
        prefix = ' X'
    print('{0} | got: {1} | expected: {2}'.format(prefix, got, expected))


def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\n', 'front_x', sep='')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\n', 'sort_last', sep='')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
