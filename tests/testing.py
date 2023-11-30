import sys
sys.path.append("..")
from src import variables, builtinfuncs, functiontree, booltree, parsing




if __name__ == "__main__":
    env = {"pi": "3.14", "x": "7"}
    # print(mathtree.Add(variables.Value(5), variables.Value(6)).eval())
    # print(booltree.GreatherThanEqual(variables.Value(5), variables.Value(6)).eval())
    # builtinfuncs.Print.eval(variables.Value(6))
    # print(parsing._Math_Parser(["(", 1, "+", 2, ")", "*", 3])._parse_AS().eval())
    expr = "2 + 3 * x"
    # print(parsing.evaluate_math_expression(expr, env))
    # print(parsing.is_math_expression(expr))
    print(parsing.math_expression_to_ast(expr, env))