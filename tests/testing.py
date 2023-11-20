import sys
sys.path.append("..")
from src import variables, builtinfuncs, functiontree, booltree




if __name__ == "__main__":
    # print(mathtree.Add(variables.Value(5), variables.Value(6)).eval())
    print(booltree.GreatherThanEqual(variables.Value(5), variables.Value(6)).eval())
    # builtinfuncs.Print.eval(variables.Value(6))