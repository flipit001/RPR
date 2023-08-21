import RPRbuiltins as builtins
fname = "testing.rpr"

symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '\n', ':', ',']
symbols_no_str = "{([.\n:,])}"
ok = "~!@#$%^&*()_+{}|:\"<>?,./;\'\][=-``]] "
multi_char_symbols = ["//"]
builtin_funcs = {"print": print}
ALLKEYS = symbols+multi_char_symbols
    

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

# print(allines)

final = []

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
    # print(usable_lines[i])
    if usable_lines[i].startswith("//"):
        continue
    for k, v in om.vars.items():
        if i <= v[1]:
            continue

        # print(k)
        # print(om.find_all(k, before_comments))
        l = om.find_all(k, before_comments)
        for index in range(len(l)):
            # print(before_comments[l[index] + len(k)+1])
            # print(l, l[index])
            # print(before_comments[l[index-1]])
            if l[index] == -1:
                # print("here")
                break
            # print(before_comments[l[index] + len(k)+1])
            # print("this is cool")
            if (index+len(k)+1 >= len(before_comments) or before_comments[l[index] + len(k)+1] in ok) and (l[index] == 0 or before_comments[l[index]-1] in ok):
                before_comments = f"{before_comments[:l[index]]}{v[0]}{before_comments[l[index]+len(k):]}"
                l = om.add_to_list(l, abs(len(k) - (len(v[0]))))
                # print(abs(len(k) - (len(v[0])+2)))
                print(before_comments)
            else:
                # print("here")
                continue


    # print(before_comments)
    final.append(before_comments)

# print(final)
# print(final)
for i in range(len(final)):
    final[i] = "".join(final[i])

# print(final)

for i in range(len(final)):
    line = final[i] + " "

    for funcname, func in builtin_funcs.items():
        try:
            index = final[i].index(funcname)
        except ValueError:
            continue
        if (index == 0 or line[index-1] in ok) and line[index+1] in ok:
            print("here")
            args = om.in_between("(", ")", line)
            # print(args)
            try:
                func(args)

            except:
                raise Exception("sorry, your arguments were wrong")


    
                

# print(om.vars["one"])
        

