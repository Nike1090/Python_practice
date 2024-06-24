from globals import vowels
def count_vowels(string: str):
    cnt = 0
    for x in string:
       if x in vowels:
           cnt+=1
    return cnt
    
if __name__ == '__main__':
    print(count_vowels("what are you doing"))    