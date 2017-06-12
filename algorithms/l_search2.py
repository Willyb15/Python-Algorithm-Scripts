def search(values, target):
    for i in range(len(values)):
        if target == values[i]:
            return 1
    return -1

array = [1,2,3,4,5,6,7,8]
print search(array,2)
