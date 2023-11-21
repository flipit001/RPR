import src.mathtree as m, src.booltree as b, src.variables as v

math_expressions = ["+", "-", "*", "/"]
bool_expressions = ["||", "&&", "!", ">", ">=", "<", "<="]
nums = "123456789."

def evaluate_math_expression(expression: str, env: dict):
    # turn expression to list
    expression = expression.replace(" ", "")
    operators = [i for i in expression if i in math_expressions] + ['']
    nums = _multi_split(expression, math_expressions)
    print(nums)
    for i in range(len(nums)):
        if nums[i] in env:
            nums[i] = env[nums[i]]
        nums[i] = float(nums[i])
    list_expr = [j for i in zip(nums, operators) for j in i][:-1]
    print(list_expr)


    return _Math_Parser(list_expr)._parse_AS()


def _multi_split(s, delims):
    
    for deli in delims:
        s = " ".join(s.split(deli))

    return s.split()

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
        if temp != ")":
            self.cur = self._next()
            return v.Value(temp)
        
        else:
            self.cur = self._next()
            node = self._parse_AS()
            self.cur = self._next()
            return node


