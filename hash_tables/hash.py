class HT:
    def __init__(self):
        self.bucket = [None] * 26
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def hash1(self, value):
        letter = value[0]
        return self.alphabet.index(letter)

    def social(self, value):
        x = type(int(value[:3]))
        return x

    def name(self,value):
        # splitname = fullname.split()
        # for i in range(len(splitname)):
        #     splitname[i] = splitname[i][0].lower()
        # for j in range(len(splitname[][0]))
        #
        # first = self.alphabet.index(splitname[0][0])
        # last = self.alphabet.index(splitname[1][0])
        # full = first * last

        words = value.split()
        first_letters = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_indices = []
        for word in words:
            first_letter = word[0]
            first_letters.append(first_letter.lower())
            alphabet_indices.append(index)

        for letter in first_letters:
            alphabet_indices.append(alphabet.index(letter))

        product = alphabet_indices[0]
        for i in range(1, len(alphabet_indices)):
            product *= alphabet_indices[i]
        return product
x = HT()
name = "will"
print x.hash1(name)
# print name
# print x.bucket
# print x.store(name)
soc = "2607894545"
print x.social(soc)
fullname = "will bryant"
# splitname = fullname.split(" ")
# print splitname
# print splitname[0][0] + splitname[1][0]
# print x.name(fullname)
# print x.name("bob bmith")





string_input = "1,23,4,55,,1,,,,333,  ,3,,5,103,  74,3"
# find the hiest value and assign the highest value to a vraibale
# print the highest value

split_values = string_input.split(",")
print split_values
for i in range(len(split_values)):
    split_values[i] = split_values[i].strip()
highest = 0
for v in split_values:
    if len(v) != 0:
        n = int(v)
        if n > highest:
            highest = n
print highest

# take this and do it 1 loopds
