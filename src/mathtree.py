from src.variables import Value, Variable


class Expression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        pass

    def eval(self):
        pass

class Add(Expression):
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
    

