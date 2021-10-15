string = input('Write the string: ')

medium = int((len(string) + 1) / 2)
newString = string[medium:len(string)] + string[0:medium]

print(newString)
