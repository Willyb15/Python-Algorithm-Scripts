def iSort(list):
    #return a sorted list
    pass

my_array = [54,26,93,17,77,31,44,55,20]
# print my_array
for index in range(1, len(my_array)):
    current = my_array[index]
    print "current position %r" % current
    position = index
    print "current index %r" % index
    while position > 0 and my_array[position-1] > current:
        my_array[position] = my_array[position-1]
        print("My array[posisiton] %r" % my_array[position])
        position = position - 1
        print("This is my new position %r" % position)
    my_array[position] = current
print(my_array)
