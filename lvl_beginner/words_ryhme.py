def isRyhme(word1: str, word2: str):
    if word1[::-1][0:3] == word2[::-1][0:3]:
        return "They rhyme"
    elif word1[::-1][0:2] == word2[::-1][0:2]:
        return "They slightly rhyme"
    else: 
        return "They don't rhyme"
if __name__ == '__main__':
 
    print(isRyhme("wetc", "matc"))
    