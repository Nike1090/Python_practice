def inversa(word):
    word_length = len(word)
    String_reversed = []
    while word_length !=0:
        String_reversed.append(word[word_length-1])
        word_length-=1
    return "".join(String_reversed)

if __name__ == '__main__':
    print(inversa('babddad'))

# 2nd method
# def inversa(string: str):
#     reversed_string = ""
#     for s in range(len(string), 0, -1):
#         reversed_string += string[s-1]
#     return reversed_string


# if __name__ == '__main__':
#     print(inversa("Hola"))     