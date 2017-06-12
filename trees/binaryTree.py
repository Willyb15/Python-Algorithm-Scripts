class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child_node = None
        self.right_child_node = None

class MyBinaryTree:
    def __init__(self):
        self.root_node = None

    def add(self,value):
        #add the value into the Tree

        #If no root, then ste value to root
        if self.root_node == None:
            self.root_node = BinaryTreeNode(value)
            return
        if value > self.root_node.value:
            self.root_node.right_child_node = BinaryTreeNode(value)
        else:
            self.root_node.left_child_node = BinaryTreeNode(value)
        print self.root_node

b = MyBinaryTree()
b.add(10)
b.add(11)
