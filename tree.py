# 1.Question:
# Insert the following numbers into an empty BST in the given order.


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Example Usage
root = None
numbers = [50, 30, 70, 20, 40, 60]
for num in numbers:
    root = insert(root, num)

print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
