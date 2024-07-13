from calculator import Calculator
``

class calculatorDescriptive(Calculator):
    def __init__(self, n1, n2) -> None:
        super().__init__(n1, n2)

    def sum(self):
        return super().sum()
    
    def subtract(self):
        return super().subtract()
    
    def multiply(self):
        return super().multiply()
    

if __name__ == "__main__":
    
    print(calculatorDescriptive(1,2).sum())
    print(calculatorDescriptive(1,2).subtract())
