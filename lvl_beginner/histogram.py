def histogram(list):
    for list_item in list: 
        print(list_item*'*')


if __name__ == '__main__':
    histogram([5, 2, 3, 4])    

# def histogram(numbers):
#     stars = ""
#     for n in numbers:
#         stars += "*" * n + "\n"
#     return stars


# if __name__ == '__main__':
#     print(histogram([4, 9, 7]))
#     print(histogram([1, 2, 3, 4, 5, 2, 2]))