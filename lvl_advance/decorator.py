def calculate(sum):
    def wrapper( *args, **kwargs):
        print('Inside the function')
        sum(*args, **kwargs)
        print('Finish the function')
    return wrapper

@calculate
def sum_2(n1,n2):
    print(f'sum of {n1} and {n2} is {n1 + n2}')


@calculate
def sum_3(n1, n2, n3):
    print(f'sum of three numbers is {n1 + n2 + n3}')

if __name__ == "__main__":
    sum_2(1,2)
    sum_3(2,3,4)

# – Function: A function in Python is a block of code that performs a specific task, accepts inputs (arguments), processes them, 
# and optionally returns an output.

# – Decorator: A decorator is a higher-order function that takes another function as an argument, adds some functionality, 
# and returns a new function. It allows modifying or extending behavior of functions or methods.
# https://www.geeksforgeeks.org/decorators-in-python/