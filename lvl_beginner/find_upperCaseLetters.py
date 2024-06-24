
def no_of_uppercase_letters(string: str): 
    cnt = 0
    for x in string:
        if x.isupper():
            cnt+=1
    return cnt       
        
if __name__ == '__main__':
    sent = input("Enter any sentence:")
    print(no_of_uppercase_letters(sent))  