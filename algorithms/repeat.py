def repeat(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashcount = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    indexes = []
    for x in word:
        index = alphabet.index(x)
        hashcount[index] +=1
        indexes.append(index)

    wordindex = 0
    for x in indexes:
        if hashcount[x] == 0:
            return word[wordindex]
        wordindex +=1

    return -1



x = "digitalcrafts"
y = "hirewire"
z = "atlanta"
a = "Atlanta"
b = "racecar"
print repeat(x)
print repeat(y)
print repeat(z)
print repeat(z)
print repeat(b)
