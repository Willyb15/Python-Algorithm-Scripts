class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        bucket_index = self.my_hash(value)
        # print bucket_index
        # initialize bucket as an array, if the bucket is none
        # first time inserts only
        # bucket = [self.buckets[bucket_index]]
        if self.buckets[bucket_index] == None:
            self.buckets[bucket_index] = []
        # actually append the value
        bucket = self.buckets[bucket_index]
        # print bucket
        bucket.append(value)
        # print bucket

    def exists(self, value):
        # Returns true if the value exists in the bucket.
        # print value
        bucket_index = self.my_hash(value)
        bucket = self.buckets[bucket_index]
        if bucket == None:
            return False
        for v in self.buckets[bucket_index]:
            if v == value:
                return True

        return False





hash_table = MyHashTable()
hash_table.insert('Abe')
hash_table.insert('Hello World')
hash_table.insert('Happy')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')
#
print(hash_table.exists('Hello World'))
#
# print(hash_table.buckets)
