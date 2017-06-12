def checkWord(word):
    l = len(word)
    # print l
    for i in range (0,len(word)/2):
        if word[i] != word[l-1-i]:
            return False

    return True


word = "racecar"
word2 = "madam"
print checkWord(word)
print checkWord(word2)
