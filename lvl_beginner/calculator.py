ops = ['a', 's', 'm', 'd']
op = ''

n1, n2 = input("Enter any two numbers: ").split()

while op not in ops: 
    op = input("Enter the operation from given following: Subtraction(s), Addition(a), Multiplication(m), division(d) :")

    if op == 'a':
        print(f"Addition of {n1} and {n2} is {int(n1)+int(n2)}")
    if op == 's':
        print(f"Subtraction of {n1} and {n2} is {int(n1)-int(n2)}")
    if op == 'm':
        print(f"Multiplication of {n1} and {n2} is {int(n1)*int(n2)}")
    if op == 'd':
        print(f"Division of {n1} and {n2} is {int(n1)/int(n2)}")    