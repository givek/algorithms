class AVLNode:
    def __init__(self, val, height=0, left=None, right=None):
        self.val = val
        self.height = height
        self.left = left
        self.right = right


class AVL:
    def __init__(self, val=None):
        self.root = AVLNode(val)

    @staticmethod
    def height(node: AVLNode):
        if not node:
            return -1
        return node.height

    def balance_factor(self, node: AVLNode):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotation(self, node: AVLNode):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        if node == self.root:
            self.root = new_root

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root

    def right_rotation(self, node: AVLNode):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        if node == self.root:
            self.root = new_root

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root

    def insert(self, val):
        self.root = self.insert_node(self.root, val)

    def insert_node(self, root: AVLNode, val):
        if not root:
            return AVLNode(val)

        elif root.val < val:
            root.right = self.insert_node(root.right, val)
        else:
            root.left = self.insert_node(root.left, val)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_factor = self.balance_factor(root)

        if balance_factor > 1:
            if self.balance_factor(root.left) == 1:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)
        elif balance_factor < -1:
            if self.balance_factor(root.right) == -1:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

    def remove(self, val):
        return self.remove_node(self.root, val)

    def remove_node(self, root: AVLNode, val):
        if not root:
            return root

        if val < root.val:
            root.left = self.remove_node(root.left, val)
        elif val > root.val:
            root.right = self.remove_node(root.right, val)
        else:  # val == root.val

            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.inorder_successor(root.right)
            root.val = temp.val

            root.right = self.remove_node(root.right, temp.val)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_factor = self.balance_factor(root)

        if balance_factor > 1:
            if self.balance_factor(root.left) >= 0:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)
        elif balance_factor < -1:
            if self.balance_factor(root.right) <= 0:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)

        return root

    def inorder_successor(self, root):
        if not root or not root.right:
            return root
        return self.inorder_successor(root.right)

    def find_parent(self, root, node):
        if root == node:
            return None

        if root.left == node or root.right == node:
            return root

        if root.val < node.val:
            return self.find_parent(root.right, node)
        else:
            return self.find_parent(root.left, node)

    def search(self, val):
        return self.search_node(self.root, val)

    def search_node(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root

        if root.val < val:
            return self.search_node(root.right, val)
        else:
            return self.search_node(root.left, val)

    def preorder_traversal(self, root):
        if root:
            print(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


def main():
    avl = AVL(2)

    avl.insert(1)
    avl.insert(4)
    avl.insert(3)
    avl.insert(5)

    avl.preorder_traversal(avl.root)

    root = avl.remove(1)

    print()
    print(avl.root.val, root.val)
    print()

    avl.preorder_traversal(avl.root)


if __name__ == "__main__":
    main()
