

array = [45,7,43,9,12,3,65,78,21,3,0,1,-5,-8,100,-45,34]

def sort(list2sort):
    for i in range(len(list2sort)):
        minVal = i
        for j in range(i, len(list2sort)):
            if list2sort[minVal] > list2sort[j]:
                minVal = j
        temp = list2sort[minVal]
        list2sort[minVal] = list2sort[i]
        list2sort[i] = temp
    return array

print sort(array)
