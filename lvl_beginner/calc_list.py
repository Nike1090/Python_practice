def calculate_length(x):
    cnt = 0
    for i in x:
        cnt+=1
    return cnt    

if __name__ == '__main__':
    x = ['ddd', 'ss']
    y = "dfd dfdf"
    print(calculate_length(x))
    print(calculate_length(y))