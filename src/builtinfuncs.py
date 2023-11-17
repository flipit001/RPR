from src.functiontree import Function

class Print(Function):
    name = "print"
    
    def eval(token):
        print(str(token.eval()))