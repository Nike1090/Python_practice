from max_in_list import max_in_list
def long_word_in_list(lst): 
    word_lens = []
    for x in lst:
        word_lens.append(len(x))   
    for word in lst:
        if max_in_list(word_lens) == len(word):
           longest_word = word
           break   
    return longest_word

if __name__ == '__main__':
    print(long_word_in_list(['star', 'mindful' , 'damrdsdsdsdsd', 'hamburger']))   