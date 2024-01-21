import src.mathtree as m, src.booltree as b, src.variables as v
from re import split as _split, search

math_expressions = ["+", "-", "*", "/", "(", ")"]
bool_expressions = ["||", "&&", "!", ">", ">=", "<", "<=", "=="]
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

    # print(_split(re_bool_ops, expression))
    
    list_expr = [i for i in _split(re_bool_ops, expression) if i != None]

    # print(list_expr)

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

    print(_multi_list_split(list_expr, bool_expressions))

def _astify(listexp): # listexp: [Value, 'OPERATION', Value] listexp or: [Value, Operation, None]
    v1, v2 = listexp[0], listexp[2]
    op = listexp[1]

    match op:
        case '+':
            return m.Addition(v1, v2)
        case '-':
            return m.Subtraction(v1, v2)
        case '*':
            return m.Multiplication(v1, v2)
        case '/':
            return m.Division(v1, v2)
        case '||':
            return b.Or(v1, v2)
        case '&&':
            return b.And(v1, v2)
        case '==':
            return b.Equal(v1, v2)
        case '!=':
            return b.NotEqual(v1, v2)
        case '>':
            return b.GreaterThan(v1, v2)
        case '>=':
            return b.GreatherThanEqual(v1, v2)
        case '<':
            return b.LessThan(v1, v2)
        case '<=':
            return b.LessThanEqual(v1, v2)
        case '!':
            return b.Not(v1)
        case _:
            raise ValueError(f"_astify; operation '{op}' does not exist")


def _list_split(l, delim):
    res = []
    t = []
    for i in l:
        if i == delim:
            res.append(t)
            res.append([i])
            t = []
        else:
            t.append(i)
        # print(t)
    res.append(t)
    return res

def _multi_list_split(l, delims):
    res = []
    t = []
    for i in l:
        if i in delims:
            res.append(t)
            res.append([i])
            t = []
        else:
            t.append(i)
    res.append(t)
    return res

def _multi_split(s, delims):
    
    for deli in delims:
        s = " ".join(s.split(deli))

    return s.split()

def _sum(l):
    output = ""
    for tok in l:
        output += tok
    
    return output


def is_math_expression(expression):
    return bool(search(re_std_ops, expression))

def is_string(expression):
    return bool(search(is_string_re, expression))

def is_number(expression):
    return bool(search(is_number_re, expression)) and not is_string(expression) and not is_math_expression(expression)

def is_bool(expression):
    return bool(search(is_bool_re, expression))


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


