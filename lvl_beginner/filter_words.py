
def long_word_in_list(lst, n): 
    words = []
    for x in lst:
        if len(x) > n:
            words.append(x)
    return words
        
if __name__ == '__main__':
    print(long_word_in_list(['star', 'mindful' , 'damrdsdsdsdsd', 'hamburger'], 4))  