from max_num import max_num

def max_num_three(n1, n2, n3):
    # if n1 > n2 and n1 > n3:
    #     return n1
    # elif n2 > n1 and n2 > n3:
    #     return n2
    # else:
    #     return n3
    res = max_num(n1,n2)
    return res if res>n3 else n3

        
if __name__ == '__main__':
    print(max_num_three(1, 2, 4))
    print(max_num_three(6, 1, 4))
    