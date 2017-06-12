# from pythonds.basic.stack import Stack
# s = Stack()
# s.push('1')
# s.push('2')
# print(self.data)
#
# print(s.peek())
# print(s.peek())
# print(s.pop())
# print(s.pop())
#
class MyStack:
    data = []
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[len(self.data)-1]
        print(item)
        del self.data[len(self.data)-1]
        return item

    def peek(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.data)
s.pop()
print(s.data)
print(s.peek())
print(s.size())
print(s.isEmpty())



# array = [1,2,3,4]
# print(array)
# array.pop(2)
# print(array)