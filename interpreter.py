import RPRbuiltins as builtins
fname = "testing.rpr"

symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']
ok = "~!@#$%^&*()_+{}|:\"<>?,./;\'\][=-``]] "
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
                # print(reading)
                allines.append(reading)
                reading = ''

# print(allines)

usable_lines = "".join(allines).split("\n")
om = builtins.OperationManager()

for i in range(len(usable_lines)):
    before_comments, _, _ = usable_lines[i].partition("//")
    # print(before_comments)
    om.set_args(before_comments)

    if "=" in before_comments:
        name = before_comments[:before_comments.index("=")]
        val = before_comments[before_comments.index("=")+1:]
        # print("HELLO")
        # print(name, val)
        om.set_vars({name: [val, i]})

for i in range(len(usable_lines)):
    before_comments, _, _ = usable_lines[i].partition("//")
    before_comments += " "
    for k, v in om.vars.items():
        if i <= v[1]:
            continue

        # print(k)
        # print(om.find_all(k, before_comments))
        for index in om.find_all(k, before_comments):
            if index == -1:
                print("here")
                break
            if before_comments[index + len(k)+1] in ok:
                before_comments = f"{before_comments[:index]}{v[0]}{before_comments[:len(v[0])+index]}"
                print(before_comments)
            else:
                continue

    
                

# print(om.vars["one"])
        

