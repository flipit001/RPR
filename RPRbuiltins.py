
spaces = [" ", "\t", "\n"]
types = ["string", "int", "bool", "float", "list"] # mayble hashmap eventually
dividers = ["(", ")", "[", "]"]
math_operations = ["+", "-", "*", "/", "%", "//", "**"]
bool_operations = ["==", "!=", "<=", ">=", "<", ">", "!"]
and_or = ["&&", "||"]
activate_tabs = ["if", "else", "elif", "func"]


def handle_operations(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "%":
        return num1 % num2
    elif operation == "//":
        return num1 // num2
    elif operation == "**":
        return num1 ** num2
    
def multi_split(string, delimiters):
    for delimiter in delimiters:
        string = " ".join(string.split(delimiter))
 
    return string.split()

def in_between(del1, del2, string):
    _, _, after = string.partition(del1) # after del1
    before, _, _ = after.partition(del2) # before del2 after del1
    return before

def find_all(string, ch):
    return [i for i, letter in enumerate(string) if letter == ch]

def lists_2_dict(list1, list2):
    return dict(zip(list1, list2))

def handle_parantheses(args):
    args.replace(" ", "")
    firsts = find_all(args, "(")
    # print(len(args))
    pair = {}
    for i in range(len(firsts)):
        first = firsts[i]
        cfirst = first
        temp = 0
        ctemp = 1
        # count = 0
        while (temp != ctemp):
            # print(first)
            ctemp = 0
            # print(temp)
            if args[first] == "(":
                # print(args[first])
                temp += 1
            if args[first] == ")":
                temp -= 1
            first += 1
            # count += 1
        pair[cfirst] = first

    #testing
    output = []
    for k, v in pair.items():
        output.append(args[k:v])
    
    return output[-len(multi_split(args, and_or)):], args


def handle_operations(args):
    expressions = args[0]
    original = args[1]
    for expression in expressions:
        expression = in_between("(", ")", expression)
        #bool_operations = ["==", "!=", "<=", ">=", "<", ">", "!"]
        for i in range(len(bool_operations)):
            if bool_operations[i] in expression:
                condition, ex, check = expression.partition(bool_operations[0])
                

        
    

    

if __name__ == "__main__": # for testing

    # print(find_all("hey bro how are you doing like how?", "h"))
    test = "(((1+1==2)&&(2+2!=3))||(54+2==56))"
    # print("hi")
    print(handle_parantheses(test))

    # operations = ["+", "-", "*", "/", "%", "//", "**"]
    # num1, num2 = 4, 5
    # for operation in operations:
    #     print(handle_operations(num1, num2, operation))