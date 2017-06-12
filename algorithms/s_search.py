
# min = 2
# swap the 2 and the 10
def search(list2sort):
    for i in range(len(list2sort)):
        minimum = i
        for j in range(i, len(list2sort)):
            if list2sort[j] < list2sort[minimum]:
                minimum = j
        placeholder = list2sort[minimum]
        list2sort[minimum] = list2sort[i]
        list2sort[i] = placeholder
    return list2sort



myList = [10,2,7,4,13,-1,45,23]
print search(myList)


# arr = [5,4,3,1,6,8,10,9] # array not sorted
#
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if(arr[i] > arr[j]):
#             arr[i], arr[j] = arr[j], arr[i]
#
# print arr

array = [10,2,4,8,3,98,45,3]

def search(values):
    for i in range (len(values)):
        minimum = i
        for j in range (i, len(values)):
            if values[j] < values[minimum]:
                minimum = j
        temp = values[minimum]
        values[minimum] = values[i]
        values[i] = temp
    return values

print search(array)


# a = [1,43,6,97,3,-1,25,4]
#
#
# def search(list2sort):
#     for i in range (len(list2sort)):
#         minVal = i
#         for j in range (i, len(list2sort)):
#             if list2sort[j] < list2sort[minVal]:
#                 minVal = j
#         temp = list2sort[minVal]
#         list2sort[minVal] = list2sort[i]
#         list2sort[i] = temp
#     return list2sort
#
# print search(a)
#
#
# def s(list2sort):
#     for i in range(len(list2sort)):
#         minimum = i
#         for j in range(i, len(list2sort)):
#             if list2sort[j] < list2sort[minimum]:
#                 minimum = j
#         placeholder = list2sort[minimum]
#         list2sort[minimum] = list2sort[i]
#         list2sort[i] = placeholder
#     return list2sort
#
#
#
# myList = [10,2,7,4,13,-1,45,23]
# print s(myList)
# print s(a)
