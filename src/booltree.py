from src.variables import Value, Variable, Expression

class Or(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} || {self.right}"
    
    def eval(self):
        return self.left.eval() or self.right.eval()
    
class And(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} && {self.right}"
    
    def eval(self):
        return self.left.eval() and self.right.eval()
    
class Not:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"!{self.value}"
    
    def eval(self):
        return not self.value

class Equal(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self) -> str:
        return f"{self.left} == {self.right}"
    
    def eval(self):
        return self.left.eval() == self.right.eval()
    
class NotEqual(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self):
        return f"{self.left} != {self.right}"
    
    def eval(self):
        return self.left.eval() == self.right.eval()
    
class GreaterThan(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self):
        return f"{self.left} > {self.right}"
    
    def eval(self):
        return self.left.eval() > self.right.eval()

class GreatherThanEqual(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self):
        return f"{self.left} >= {self.right}"
    
    def eval(self):
        return self.left.eval() >= self.right.eval()
    
class LessThan(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self):
        return f"{self.left} < {self.right}"
    
    def eval(self):
        return self.left.eval() < self.right.eval()
    
class LessThanEqual(Expression):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __str__(self):
        return f"{self.left} <= {self.right}"
    
    def eval(self):
        return self.left.eval() <= self.right.eval()

