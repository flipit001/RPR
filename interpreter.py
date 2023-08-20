import RPRbuiltins as builtins

fname = "testing.rpr"

symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']
multi_char_symbols = ["//"]
keywords = ['func', "print"]
ALLKEYS = symbols+multi_char_symbols+keywords
    

# fname = input("filename: \n")
f = open(fname, "r")
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

# print(allines)

usable_lines = "".join(allines).split("\n")
om = builtins.OperationManager()

for i in range(len(usable_lines)):
    om.set_args(usable_lines[i])
    if "=" in usable_lines[i]:
        name = usable_lines[i][:usable_lines[i].index("=")]
        val = usable_lines[i][usable_lines[i].index("=")+1:]
        # print("HELLO")
        print(name, val)
        om.set_vars({name: val})

print(om.vars)
        

