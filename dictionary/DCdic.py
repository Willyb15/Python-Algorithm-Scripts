class MyDictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert_element(self, key, value):
            # insert element into dictionary
            self.keys.append(key)
            self.values.append(value)


    def find_element(self, key):
        # find the element associated with the key
        # returns none if the element doesnt exist
        for x in range(len(self.keys)):
            if self.keys[x] == key:
                return self.values[x]

        return None

    def remove_element(self, key):
        # find value associated with the element
        # removes element if element is found
        for x in range(len(self.keys)-1):
            if self.keys[x] == key:
                del self.values[x]
                del self.keys[x]


    def get_keys(self):
        return self.keys

    def elements(self):
        return self.values

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.values)






dictionary = MyDictionary()
dictionary.insert_element('email', 'will@gmail.com')
dictionary.insert_element('password', 'chicken_nuggest$')
dictionary.insert_element('phone', '405805066')
print(dictionary.keys)
print(dictionary.values)

print(dictionary.find_element('password'))
dictionary.remove_element('phone')
print(dictionary.isEmpty())

for key in dictionary.get_keys():
    print(key + "\t\t" + dictionary.find_element(key))































