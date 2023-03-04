nonLatinLetters = {
    'A': 'А', 'B': 'Β', 'C': 'С', 'E': 'Е', 'H': 'Н', 'K': 'К',
    'M': 'М', 'N': 'Ν', 'O': 'О', 'P': 'Р', 'T': 'Т', 'X': 'Х',
    'Y': 'Υ', 'a': 'а', 'c': 'с', 'e': 'е', 'o': 'о', 'p': 'р',
    's': 'ѕ', 'x': 'х'
}

# Change the replaceable latin characters for nonlatin ones from a string
def modifyLine(line):
    output = []

    for token in line:
        newToken = nonLatinLetters.get(token)

        if newToken:
            output.append(newToken)
        else:
            output.append(token)
    
    return output

def printModifiedText(lines):
    print()
    for line in lines:
        for char in line:
            print(char, end='')
    print()

with open("input.txt", mode="r", encoding="utf-8") as inputFile:
    inputLines = inputFile.readlines()

outputLines = []

for line in inputLines:
    outputLines.append( modifyLine(line) )

with open("output.txt", mode="w", encoding="utf-8") as file:
    for line in outputLines:
        for token in line:
            file.write(token)

printModifiedText(outputLines)
