class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
        return root
    if node.value < root.value:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root


def preorder(rootnode):
    if rootnode:
        print(rootnode.value)
        preorder(rootnode.left)
        preorder(rootnode.right)


def inorder(rootnode):
    if rootnode:
        inorder(rootnode.left)
        print(rootnode.value)
        inorder(rootnode.right)


def postorder(rootnode):
    if rootnode:
        postorder(rootnode.left)
        postorder(rootnode.right)
        print(rootnode.value)


def get_minimum(root) -> int:
    if root:
        while root.left is not None:
            root = root.left
        print(root.value)
        return root.value


def delete_node(root: 'Node', value: int) -> 'Node':
    if root is None:
        return root
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is not None:
            return root.right
        elif root.right is not None:
            return root.left
        else:
            temp = get_minimum(root.right)
            root.value = temp
            delete_node(root.right, temp)
    return root


root_node = Node(10)
insert(root_node, Node(9))
insert(root_node, Node(11))
insert(root_node, Node(4))
insert(root_node, Node(14))
insert(root_node, Node(10))
# preorder(root)
# inorder(root)
# postorder(root_node)
get_minimum(root_node)
node = delete_node(root_node, 9)
postorder(root_node)
