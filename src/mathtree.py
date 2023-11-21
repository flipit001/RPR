from src.variables import Value, Variable, Expression

class Addition(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} + {self.right}"
    
    def eval(self):
        return self.left.eval() + self.right.eval()
    
class Subtraction(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} - {self.right}"
    
    def eval(self):
        return self.left.eval() - self.right.eval()
    
class Multiplication(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} * {self.right}"
    
    def eval(self):
        return self.left.eval() * self.right.eval()
    
class Division(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} / {self.right}"
    
    def eval(self):
        return self.left.eval() / self.right.eval()
    

