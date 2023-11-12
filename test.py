strng = ''

with open('input.txt', 'r', encoding='utf-8') as inputfile:
    line = inputfile.readline()
    print(line.strip())
    for line in inputfile:
        strng += line.strip()
        print(line.strip())

