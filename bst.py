class Node:
    def __init__(self, value):
        self.data = value
        self.Left = None
        self.Right = None

def insert(root, value):
    if root == None:
        return Node(value)
    if value < root.data:
        root.Left = insert(root.Left, value)
    else:
        root.Right = insert(root.Right, value)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.Right, level + 1)
        print(' ' * 4 * level + '->', root.data)
        print_tree(root.Left, level + 1)

def print_in_order(root):
    if root is not None:
        print_in_order(root.Left)
        print(root.data, end=' ')
        print_in_order(root.Right)

def print_pre_order(root):
    if root is not None:
        print(root.data, end=' ')
        print_pre_order(root.Left)
        print_pre_order(root.Right)

def print_post_order(root):
    if root is not None:
        print_post_order(root.Left)
        print_post_order(root.Right)
        print(root.data, end=' ')

def print_tree_horizontal(root, level=0):
    if root is not None:
        print_tree_horizontal(root.Right, level + 1)
        print(' ' * 4 * level + str(root.data))
        print_tree_horizontal(root.Left, level + 1)

def main():
    Root = None
    n = int(input("How many numbers do you want to enter? "))
    for i in range(n):
        value = int(input("Enter number: "))
        Root = insert(Root, value)
    print("The tree has been created.")
    print("In-order traversal: ", end='')
    print_in_order(Root)
    print("\nPre-order traversal: ", end='')
    print_pre_order(Root)
    print("\nPost-order traversal: ", end='')
    print_post_order(Root)
    print("\nTree in horizontal format:")
    print_tree_horizontal(Root)

if __name__ == "__main__ 
    main()
    #  edit print the tree verticaly also anarrow show the layer