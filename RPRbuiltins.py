import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '//': operator.floordiv,
    '**': operator.pow,
    '&&': operator.and_,
    '||': operator.or_,
    '!': operator.not_,
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,

}


spaces = [" ", "\t", "\n"]
types = ["string", "int", "bool", "float", "list"] # mayble hashmap eventually
dividers = ["(", ")", "[", "]"]
math_operations = ["+", "-", "*", "/", "%", "//", "**"]
bool_operations = ["==", "!=", "<=", ">=", "<", ">", "!"]
and_or = ["&&", "||"]
activate_tabs = ["if", "else", "elif", "func"]

def _helper_handle_operations(num1, num2, operation):
    return ops[operation](num1, num2)


def multi_split(string, delimiters):
    for delimiter in delimiters:
        string = " ".join(string.split(delimiter))
 
    return string.split()

def handle_operations(args):
    args.replace(" ", "")
    # P E MD AS
    all_nums = multi_split(args, math_operations)
    all_operands = multi_split(args, all_nums)
    return [all_nums, all_operands]
    

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
    
    return [output[-len(multi_split(args, and_or)):], args]



def _helper_handle_expressions(args):
    expressions = args[0]
    original = args[1]
    output = [[]]
    for expression in expressions:
        expression = in_between("(", ")", expression)
        print(expression)
        #bool_operations = ["==", "!=", "<=", ">=", "<", ">", "!"]
        cond, ex, check = expression.partition(bool_operations[0])
        expression = ops[ex](cond, check)

        
        output[0].append(expression)
    
    output.append(original)
    return output

def handle_expressions(args):
    arguments = handle_parantheses(args)
    expressions, original = _helper_handle_expressions(arguments)
    return [expressions, original]


        
    

    

if __name__ == "__main__": # for testing

    # print(find_all("hey bro how are you doing like how?", "h"))
    test = "1+2+2+3+4*5"
    # print("hi")
    print(handle_operations(test))

    # operations = ["+", "-", "*", "/", "%", "//", "**"]
    # num1, num2 = 4, 5
    # for operation in operations:
    #     print(handle_operations(num1, num2, operation))