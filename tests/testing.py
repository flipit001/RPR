import sys
sys.path.append("..")
from src import variables, mathtree




if __name__ == "__main__":
    print(mathtree.Add(variables.Value(5), variables.Value(6)).eval())