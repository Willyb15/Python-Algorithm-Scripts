#from pythonds.basic.stack import Stack

class MyStack:
    data = []

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        return item

    def peek(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0


s = MyStack()
s.push('1')
s.push('2')
print(s.data)

print(s.peek())
print(s.peek())
print(s.pop())
print(s.pop())


stocks = [10,50,30,40,30]
spans = [0,0,0,0,0]

def calcSpan (stocks,spans):
    #Create a stack and push index of fisrst element to it
    stack = MyStack()
    stack.push(0)

    #Span value of first element is always 1

    spans[0] = 1

    #Calcualte Span values for the rest of the elements

    for i in range (1,len(stocks)):
        #pop elements from stack while stack is not
        #empty and top of stack is smaller than the price[i]
        while(not stack.isEmpty() and stocks[stack.peek()] <= stocks[i]):
            stack.pop()

        spans[i] = i + 1 if stack.size() <= 0 else (i - stack.peek())

    #If stack becomes empty, then price[i] is greater than all the elements
    #on the left of it, i.e. price[0], price[1], price[i-1]. Else the price[i] is
    #greater than elements at the top of stack

        #push this element onto the stack

        stack.push(i)
    print(stack)
    print(spans)

calcSpan(stocks, spans)

#array = [1,2,3,4,5]
#print(array)

for i in range (0,len(array)):
    x = 5
    #if array[i] = 2
       # array.push(x)