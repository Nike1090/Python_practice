from inversa import inversa

def is_Palindrome(word : str):
    return True if inversa(word) == word else False


if __name__ == '__main__':
    word = input("Enter any Word to Check if it's palindrome:")
    if is_Palindrome(word):
        print(f"{word} is a Palindrome")
    else:
        print(f"{word} is not a Palindrome")