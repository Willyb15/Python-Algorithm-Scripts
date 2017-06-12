# Linear Search of n complexity
# e, linear search or sequential search is a method for finding a
# target value within a list. It sequentially checks each element of
# the list for the target value
#  until a match is found or until
#  all the elements have been searched.

def search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            print "the list was found at %r" % list[i]
            return

    print "the target was not found in the index"

array = [1,2,3,4,5,6]

search(array,5)
search(array,10)
search(array,3)
