import re

def find_vowels(phrase):
    vowels_regex = re.compile(r'[^aeiou]')
    return vowels_regex.findall(phrase)

def find_vowels_ignore_case(phrase):
    return re.compile(r'[^aeiou]', re.IGNORECASE).findall(phrase)
  

if __name__ == '__main__':
    print(find_vowels('what is going on?'))
    print(find_vowels_ignore_case('HI, What is you Name?'))