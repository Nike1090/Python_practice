# def max_number(x, y):
#     if x>y: 
#         return x
#     else:
#         return y
    

# x, y = input("Enter the any two numbers: ").split()
# print(max_number(int(x),int(y)))

def max_num(n1, n2):
    return n1 if n1 > n2 else n2


if __name__ == '__main__':
    print(max_num(1, 2))
    print(max_num(4, 1))