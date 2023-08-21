import operator
# import ast
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
            # print(k, v)
            expression = expression.replace(k, v)
        return bool(eval(expression))
    
    def set_args(self, args):
        self.args = args

    def get_type(self, value):
        try: 
            return self.is_true(value)
        except ValueError:
            pass
        try: 
            list(value)
        except ValueError:
            pass
        try: 
            int(value)
        except ValueError:
            pass
        
    def handle_operation(self, expression, typ=int):
        return eval(expression)

    def multi_split(self, string, delimiters):
        for delimiter in delimiters:
            string = " ".join(string.split(delimiter))
    
        return string.split()

    def in_between(self, del1, del2, string):
        _, _, after = string.partition(del1) # after del1
        before, _, _ = after.partition(del2) # before del2 after del1
        return before

    def find_all(self, ch, string=None):
            if len(ch) == 1:
                if not string:
                    string = self.args
                res = [i for i, letter in enumerate(string) if letter == ch]
                if res:
                    return res
                return [-1]
            else:
                index = 0
                res = []
                if index == -1:
                    return [-1]
                while index != -1:
                    res.append(index)
                    index = string.find(ch, index+1, -1)

                return res



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
    
    def add_to_list(self, l, num):
        return [i+num for i in l]

if __name__ == "__main__":
    om = OperationManager()
    om.args = """
any func nice() {
    any func wrapper{
    yeah this is cool
                    }
}

"""
    print(om.is_true("(?1) || (2 == 1)"))
    # print(om.handle_operation("1 + 2 * 3")) #unforunately unless i find a better way to do this i have to use eval()
    # om.handle_brackets("{}")
    # try:
    #     print(om.handle_operation("20", "1000000", "**"))
    # except ValueError:
    #     raise ValueError("too big bruh")
    # om.set_vars({"yup": "not nice"})
    # print(om.vars["yup"])
    # om.set_vars({"yup": "nice"})
    # print(om.vars["yup"])


