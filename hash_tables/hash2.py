# class HT:
#     def __init__(self):
#         self.bucket = [None] * 26
#
#     def name(self, name):
#         words = name.split()
#         alphabet = "abcdefghijklmnopqrstuvwxyz"
#         first_letters = []
#         alphabet_indices = []
#         for word in words:
#             first_letter = word[0]
#             first_letters.append(first_letter.lower())
#             print first_letter
#             print first_letters
#
#         for letter in first_letters:
#             alphabet_indices.append(alphabet.index(letter))
#             print alphabet_indices
#
#         product = alphabet_indices[0]
#         for i in range(1, len(alphabet_indices)):
#             print str(alphabet_indices[i]) + "this is the index"
#             product *= alphabet_indices[i]
#             print product
#
#
#
# x = HT()
# name = "will steen gryant"
# print x.name(name)


string_input = "1,23,4,55,,1,,,,333,  ,3,,5,103,  74,3"
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
