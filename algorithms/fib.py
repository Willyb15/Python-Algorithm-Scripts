# def fib():
#     arr = []
#     x = 0
#     y = 1
#
#     while x < 1000:
#         x, y = y, x+y
#         arr.append(x)
#     return arr
#
# print fib()
#
#
# def rfib(x, y, arr = []):
#     # arr.append(x)
#     if x < 1000:
#         # arr.append(x)
#         return rfib(y, y+x, arr + [x])
#
#     return arr
#
# print rfib(0,1)

def fib():
    array = []
    x = 0
    y = 1
    while x <= 1000:
        x, y = y, x+y
        array.append(x)
    return array

print fib()

def rfib(x,y, arr=[]):
    if x <= 1000:
        return rfib(y, x+y, arr + [x])
    return arr

print rfib(0,1)
