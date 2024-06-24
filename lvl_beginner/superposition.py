def superposition(list1: list, list2: list):
    cnt = 0
    for x in range(len(list1)): 
        temp = list1[x]
        if temp in list2: 
            cnt = 1
    return True if cnt == 1 else False

if __name__ == '__main__':
    list1 = ['a', 'c', '4', 5]
    list2 = ['b', 2, '1', 6]
    print(superposition(list1, list2))

#     def superposicion(list_1, list_2):
#     same_member = False
#     for l1 in list_1:
#         for l2 in list_2:
#             if l1 == l2:
#                 same_member = True
#                 break
#     return same_member


# if __name__ == '__main__':
#     print(superposicion([1, 2], [1, 3]))
#     print(superposicion([1, 2], [4, 3]))
#     print(superposicion([1, 2, 3, 4], [1, 5, 3]))