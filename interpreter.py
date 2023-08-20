symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']
multi_char_symbols = ["//"]
keywords = ['list', 'func', 'float', 'string', 'int', "any"]
ALLKEYS = symbols+multi_char_symbols+keywords
    

# fname = input("filename: \n")
f = open(input("filename:\n"), "r")
source = f.read()
f.close()
# print(source)
source += "\n"


reading = ""
ignore = ("\t", " ")
allines = []



for i, char in enumerate(source):
    if char not in ignore:
        reading += char
    if (i+1 < len(source)): 
        if source[i+1] in ignore or source[i+1] in ALLKEYS or reading in ALLKEYS: # if next char == ' '
            if reading != '':
                print(reading)
                allines.append(reading)
                reading = ''

print(allines)
