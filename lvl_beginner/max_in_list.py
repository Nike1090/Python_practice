def max_in_list(list): 
    num_max = list[0]
    for x in list:
        if x > num_max:
           num_max = x
    return num_max    


if __name__ == '__main__':
    print(max_in_list([4, 7, 3, 9]))   