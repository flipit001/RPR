from src.variables import Expression, Value, Variable

class Function:
    def __init__(self, name, params, code) -> None:
        self.name = name
        self.params = params
        self.code = code

    def __str__(self) -> str:
        return f"{self.name}{self.params} {self.code}"
    
    def eval(self):
        return self.code.eval()
    