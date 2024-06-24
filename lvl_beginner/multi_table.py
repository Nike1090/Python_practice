def multi_table(num):
    # i = 1
    # while i < 10:
    #     print(int(num)*int(i))
    #     i+=1 
    for i in range(1, 11):
        print(f"{num}*{i} = {int(num)*i}")

if __name__ == '__main__':
    inp = input("Enter any Number:")
    multi_table(inp)