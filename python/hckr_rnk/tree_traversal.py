class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrder(root):
    print(root.data, end=' ')
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None:
        preOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.data, end=' ')



tree = BinarySearchTree()
arr = [1, 2, 5, 3, 6, 4]
    #  1
    #   \
    #    2
    #     \
    #      5
    #     /  \
    #    3    6
    #     \
    #      4  

for el in arr:
    tree.create(el)

preOrder(tree.root)
print()
postOrder(tree.root)
print()