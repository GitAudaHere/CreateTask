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


def traverse(theRoot):
    """
    Prints out all the nodes in the tree.
    """
    print(theRoot.value)
    if theRoot.left != None:
        traverse(theRoot.left)
    if theRoot.right != None:
        traverse(theRoot.right)


def bubbleSort(the_list):
    """
    Uses a bubble sort algorithm to sort a list of integers in ascending order
    """
    for i in range(len(the_list) - 1, 0, -1):
        for j in range(i):
            if the_list[j] > the_list[j + 1]:
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp


values = list(range(199, 0, -1))
bubbleSort(values)
root = sortListToBinaryTree(values, 0, len(values) - 1)
find(root, 100)
find(root, 1)
find(root, 99)
find(root, 300)
traverse(root)

