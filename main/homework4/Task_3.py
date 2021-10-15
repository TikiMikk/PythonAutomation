def generate_music(howManyLines=3, howManyLaInLines=3, isEnd=0):
    noteLa = 'la'
    line = ''
    music = ''

    for i in range(howManyLaInLines):
        if line == '':
            line += noteLa
        else:
            line += '-' + noteLa

    for i in range(howManyLines):
        if music == '':
            music += line
        else:
            music += '\n' + line

    if isEnd == 0:
        music += '.'
    elif isEnd == 1:
        music += '!'

    return print(music)

