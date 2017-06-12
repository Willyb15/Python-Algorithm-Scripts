def reverse(array,i):
    l = len(array)
    print l
    if i < int(l/2):
        array[i], array[l-1-i]=[array[l-1-i],array[i]]
        return reverse(array, i+1)
    return array



sample = [1,2,3,4,5,6]
sample2= [1,2,3,4,5,6,7]
print reverse(sample,0)
print reverse(sample2,0)
