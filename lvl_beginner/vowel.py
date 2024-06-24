from globals import vowels
def vowelCheck(x):
    if x in vowels: 
        return True
    else:
        return False


if __name__ == '__main__':
    letter = input("Enter Any alphabet: ").lower()
    if vowelCheck(letter):
       print(f"The Alphabet {letter} is a vowel")
    else:
       print(f"The Alpabet {letter} is a consonent")


# def is_vowel(character: str):
#     return True if character.lower() in vowels else False


# if __name__ == '__main__':
#     print(is_vowel('A'))
#     print(is_vowel('b'))
#     print(is_vowel('I'))
#     print(is_vowel('u'))       