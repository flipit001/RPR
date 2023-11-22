import sys
sys.path.append("..")
from src import variables, builtinfuncs, functiontree, booltree, parsing




if __name__ == "__main__":
    env = {"pi": "3.14"}
    # print(mathtree.Add(variables.Value(5), variables.Value(6)).eval())
    # print(booltree.GreatherThanEqual(variables.Value(5), variables.Value(6)).eval())
    # builtinfuncs.Print.eval(variables.Value(6))
    # print(parsing._Math_Parser(["(", 1, "+", 2, ")", "*", 3])._parse_AS().eval())
    print(parsing.evaluate_math_expression("pi * 18 / (18 + 1)", env))