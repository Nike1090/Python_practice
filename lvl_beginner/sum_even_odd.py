def isEvenOrOdd(num):
    sum = 0
    for x in str(num): 
        sum=sum+int(x)
    if sum%2 == 0:
        return True
    else: 
        return False

if __name__ == '__main__':
    if isEvenOrOdd(1111):
        print("Its Even")
    else:
        print("Its Odd")


# def par_impar(n1: str):
#     # devuelvo lista de n casteado a int recorriendo n1
#     num_list = [int(n) for n in n1]
#     sum_num = 0
#     for n in num_list:
#         sum_num += n
#     return sum_num % 2 == 0


# if __name__ == '__main__':
#     number = input("Introduce un numero: ")
#     print(par_impar(number))