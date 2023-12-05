import src.mathtree as m, src.booltree as b, src.variables as v
from re import split as _split, search

math_expressions = ["+", "-", "*", "/", "(", ")"]
bool_expressions = ["||", "&&", "!", ">", ">=", "<", "<="]
numbers = "123456789."
re_ops = r"([\(\)\+\-\*\/])"
re_bool_ops = r"(\()|(\))|(\|\|)|(\&\&)|(\!\=)|(\!)|(\<\=)|(\<)|(\>\=)|(\>)|(\+)|(\-)|(\*)|(\/)|(\=\=)"
re_std_ops = r"([\+\-\*\/])"
is_string_re = r"[\'\"]"
is_number_re = r"[0-9]"
is_bool_re = r"((true)|(false))"

def math_expression_to_ast(expression: str, env: dict):
    # turn expression to list
    expression = expression.replace(" ", "")
    list_expr = []
    
    list_expr = [i for i in _split(re_ops, expression) if i != '']

    print(list_expr)
        
    for i in range(len(list_expr)):
        if list_expr[i] in env:
            list_expr[i] = env[list_expr[i]]

        if list_expr[i] not in math_expressions:
            list_expr[i] = float(list_expr[i])

    return _Math_Parser(list_expr)._parse_AS()


def bool_expression_to_ast(expression: str, env: dict):
    expression = expression.replace(" ", "")
    list_expr = []

    print(_split(re_bool_ops, expression))
    
    list_expr = [i for i in _split(re_bool_ops, expression) if i != None]

    print(list_expr)

    for i in range(len(list_expr)):
        if list_expr[i] in env:
            list_expr[i] = env[list_expr[i]]

        if is_string(list_expr[i]):
            list_expr[i] = str(list_expr[i])

        elif is_number(list_expr[i]):
            list_expr[i] = float(list_expr[i])

        elif is_bool(list_expr[i]):
            if list_expr[i] == "true":
                list_expr[i] = True
            if list_expr[i] == "false":
                list_expr[i] = False

    print(list_expr)



def is_math_expression(expression):
    return bool(search(re_std_ops, expression))

def is_string(expression):
    return bool(search(is_string_re, expression))

def is_number(expression):
    return bool(search(is_number_re, expression)) and not is_string(expression) and not is_math_expression(expression)

def is_bool(expression):
    return bool(search(is_bool_re, expression))

def _multi_split(s, delims):
    
    for deli in delims:
        s = " ".join(s.split(deli))

    return s.split()

def _sum(l):
    output = ""
    for tok in l:
        output += tok
    
    return output

class _Math_Parser:

    def __init__(self, list_expr) -> None:
        self.list_expr = list_expr
        self.index = -1
        self.cur = self._next()

    def _next(self):
        self.index += 1
        self.index %= len(self.list_expr)
        return self.list_expr[self.index]

    def _parse_AS(self):
        node = self._parse_MD()

        while self.cur in ("+", "-"):
            temp = self.cur
            self.cur = self._next()

            if temp == "+":
                node = m.Addition(node, self._parse_MD())

            else:
                node = m.Subtraction(node, self._parse_MD())


        return node

    def _parse_MD(self):
        node = self._parse_P()

        while self.cur in ("*", "/"):
            temp = self.cur
            self.cur = self._next()
            if temp == "*":
                node = m.Multiplication(node, self._parse_P())
            else:
                node = m.Division(node, self._parse_P())

        return node



    def _parse_P(self):
        temp = self.cur
        if temp != "(" and temp != ")":
            self.cur = self._next()
            return v.Value(temp)
        
        else:
            self.cur = self._next()
            node = self._parse_AS()
            self.cur = self._next()
            return node


