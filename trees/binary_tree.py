class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order(self, root):
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        arr.append(root.value)

        if root.left:
            arr += self.pre_order(root.left)
        if root.right:
            arr += self.pre_order(root.right)
        return arr

    def in_order(self, root):
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        if root.left:
            arr += self.in_order(root.left)

        if root:
            arr.append(root.value)

        if root.right:
            arr += self.in_order(root.right)
        return arr

    def post_order(self,root):
        if root is None:
            raise ValueError("Tree is empty")
        arr = []
        if root.left:
            arr += self.post_order(root.left)
        if root.right:
            arr += self.in_order(root.right)
        if root:
            arr.append(root.value)
        return arr
    

class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                return

    def contains(self, value):
        if self.root is None:
            return False

        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False
