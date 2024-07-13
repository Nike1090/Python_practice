class Calculator():

    @staticmethod
    def sum(n1, n2):
        return n1 + n2
    
    @staticmethod
    def subtract(n1, n2):
        return n1 - n2
    
    @staticmethod
    def multiply(n1, n2):
        return n1 * n2
    
    @staticmethod
    def divide(n1, n2):
        return n1 / n2
    
if __name__ == '__main__':
    n1 = int(input("Enter the First Number:"))
    n2 = int(input("Enter the Second Number:"))
    print(Calculator.sum(n1, n2))
    print(Calculator.subtract(n1, n2))
    print(Calculator.divide(n1, n2))
    print(Calculator.multiply(n1, n2))
  
  
  