import operator
# import string

# all_chars = string.ascii_letters+'`~-_[{}]\\|;:\'\"'


ops = { # define operator module
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
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
    '+=': operator.iadd,
    "-=": operator.isub,
    '//=': operator.ifloordiv,
    '/=': operator.itruediv,
    '%=': operator.imod,
    "*=": operator.imul,
    "**=": operator.ipow,
    "?": operator.truth
}

conversion_chart = {
    '&&': " and ",
    "||": " or ",
    "!": " not ",
    "?": ""

}

class OperationManager:
    def __init__(self, args=None):
        self.args = args
        self.functions = {}
        self.vars = {}

    def get_before(self, string, ch):
        res,_,_ = string.partition(ch)
        return res
    
    def is_true(self, expression):
        for k, v in conversion_chart.items():
            expression.replace(k, v)
        return bool(conversion_chart)
    
    def set_args(self, args):
        self.args = args

    def get_type(self, value):
        try: 
            return self.is_true(value)
        except ValueError:
            pass
        try: 
            list(value)
        except:
            pass
        try: 
            int(value)
        except:
            pass
        
    def handle_operation(self, num1, num2, operation):
        return ops[operation](int(num1), int(num2))

    def multi_split(self, string, delimiters):
        for delimiter in delimiters:
            string = " ".join(string.split(delimiter))
    
        return string.split()

    def in_between(self, del1, del2, string):
        _, _, after = string.partition(del1) # after del1
        before, _, _ = after.partition(del2) # before del2 after del1
        return before

    def find_all(self, ch, string=None):
        if not string:
            string = self.args
        return [i for i, letter in enumerate(string) if letter == ch]

    def handle_brackets(self, char):
        args = self.args
        args.replace(" ", "")
        firsts = self.find_all(char[0])
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
                # print(temp)
                if args[first] == char[0]:
                    # print(args[first])
                    temp += 1
                    ctemp = 0
                if args[first] == char[1]:
                    temp -= 1
                    ctemp = 0
                first += 1
                # count += 1
            pair[cfirst] = first

        #testing
        output = []
        for k, v in pair.items():
            output.append(args[k:v])

        print(output)
        
        return [output, args]
    
    # def set_function(self, func, *args):
    #     self.functions[func] = args

    def set_vars(self, adict):
        for k, v in adict.items():
            self.vars[k] = v

    def remove_all_2d(self, l, N):
        return [[ele for ele in sub if ele != N] for sub in l]

if __name__ == "__main__":
    om = OperationManager()
    om.args = """
any func nice() {
    any func wrapper{
    yeah this is cool
                    }
}

"""
    print(om.is_true("(?1)"))
    # om.handle_brackets("{}")
    # try:
    #     print(om.handle_operation("20", "1000000", "**"))
    # except ValueError:
    #     raise ValueError("too big bruh")
    # om.set_vars({"yup": "not nice"})
    # print(om.vars["yup"])
    # om.set_vars({"yup": "nice"})
    # print(om.vars["yup"])


