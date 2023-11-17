class Value:
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self):
        return str(self.value)

    def eval(self):
        return self.value
    
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}={self.value}"
    
    def eval(self):
        return self.value