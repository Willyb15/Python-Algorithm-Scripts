# Binary Search
# step 1: mid = len(a)/2 //
# step 2: see if it equals target
# step 3: Define new start /end/midpoint
#         (midpoint = end-start //2) + start


a = [1,2,3,4,5,6,7,8,9,10]

# def search (array, target):
#     start = 0
#     end = len(array)
#     mid = (len(array) // 2)
#     guess = input("Guess a number ")
#     if guess == target:
#         print "You guessed the number!!"
#     if guess < target:
#         input("Your guess was too low...Guess Again")
#         mid = guess
#     elif guess > target:
#         input("Your guess was too high...Guess again")
# search(a, 7)




def binary_search(array, target):
    # Return the index of the target if the value exists
    #Return none if the value does not exist

    start = 0
    end = len(array)
    while start < end:
        mid = start + ((end - start) // 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            #Reassign start value to what
            end = mid - 1
        elif array[mid] < target:
            #Reassign end value to what
            start = mid + 1
    # return None

print binary_search([1,3,8,10],10)
print binary_search([1,3,8,10],1)
print binary_search([1,3,8,10],8)
print binary_search([1,3,8,10],20)







# asdlfkjasld
