class BinaryNode(object):
    """
    Has an integer value and a left and right node.
    """
    def __init__(self, value):
        """
        Initializes with an integer value and left and right nodes
        set to None.
        """
        self.value = value
        self.left = None
        self.right = None


def sortListToBinaryTree(values, start, finish):
    """
    Sorts a list of integer values into a binary tree.
    """
    if start > finish:
        return None
    else:
        mid = int((start + finish) / 2)
        key = BinaryNode(values[mid])

        key.left = sortListToBinaryTree(values, start, mid - 1)
        key.right = sortListToBinaryTree(values, mid + 1, finish)

        return key


def find(theRoot, target):
    print("Current:", theRoot.value)
    if target == theRoot.value:
        print(theRoot.value)
    elif target < theRoot.value and theRoot.left != None:
        find(theRoot.left, target)
    elif target > theRoot.value and theRoot.right != None:
        find(theRoot.right, target)
    else:
        print("Number not found")


def traverse(theRoot, inorder=False):
    """
    Prints out all the nodes in the tree.
    """
    if inorder == True:
        print(theRoot.value)
    if theRoot.left != None:
        traverse(theRoot.left, inorder=inorder)
    if inorder == False:
        print(theRoot.value)
    if theRoot.right != None:
        traverse(theRoot.right, inorder=inorder)

values = list(range(1, 1000000))
root = sortListToBinaryTree(values, 0, len(values) - 1)
# traverse(root, inorder=False)
find(root, 500000)
find(root, 1)
input("Press ENTER to exit")
