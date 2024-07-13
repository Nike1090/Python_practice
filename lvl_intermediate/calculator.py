class Calculator:
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def sum(self):
        return self.n1 + self.n2
    
    def subtract(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
    
    def divide(self):
        return self.n1 / self.n2
    
if __name__ == '__main__':
    calc = Calculator(5,6)
    print(calc.sum())
    print(calc.subtract())
    print(calc.divide())
    print(calc.multiply())