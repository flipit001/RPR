import sys
sys.path.append("..")
from src import variables, builtinfuncs, functiontree, booltree, parsing




if __name__ == "__main__":
    env = {"a": "1"}
    # print(mathtree.Add(variables.Value(5), variables.Value(6)).eval())
    # print(booltree.GreatherThanEqual(variables.Value(5), variables.Value(6)).eval())
    # builtinfuncs.Print.eval(variables.Value(6))
    print(parsing.evaluate_math_expression("3 * 5 + 2", env).eval())