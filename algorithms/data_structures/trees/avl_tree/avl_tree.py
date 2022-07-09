class AVLNode:
    def __init__(self, val, height=0, left=None, right=None):
        self.val = val
        self.height = height
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class AVL:
    def __init__(self, val):
        self.root = AVLNode(val)

    @staticmethod
    def height(node: AVLNode):
        if not node:
            return -1
        return node.height

    def balance_factor(self, root: AVLNode):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)

    def left_rotate(self, root: AVLNode):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        if root == self.root:
            self.root = new_root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root

    def right_rotate(self, root: AVLNode):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        if root == self.root:
            self.root = new_root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root

    def insert(self, val):
        self.root = self.insert_node(self.root, val)

    def insert_node(self, root: AVLNode, val):
        if not root:
            return AVLNode(val)

        if val < root.val:
            root.left = self.insert_node(root.left, val)
        else:
            root.right = self.insert_node(root.right, val)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_factor = self.balance_factor(root)

        if balance_factor > 1:  # left heavy

            if self.balance_factor(root.left) == 1:  # left-left imbalance
                return self.right_rotate(root)
            else:  # left-right imbalance
                root.left = self.left_rotate(
                    root.left
                )  # update left subtree of root node.
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.balance_factor(root.right) == -1:  # right-right imbalance
                return self.left_rotate(root)
            else:  # right-left imbalance
                root.right = self.right_rotate(
                    root.right
                )  # update right subtree of root node.
                return self.left_rotate(root)

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

            if not root.right:
                temp = root.left
                root = None
                return temp

            # if node has both left and right
            right_min_val_node = self.min_value(root.right)
            root.val = right_min_val_node.val
            root.right = self.remove_node(root.right, right_min_val_node.val)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_factor = self.balance_factor(root)

        if balance_factor > 1:  # left heavy

            if self.balance_factor(root.left) >= 0:  # left-left imbalance
                return self.right_rotate(root)
            else:  # left-right imbalance
                root.left = self.left_rotate(
                    root.left
                )  # update left subtree of root node.
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.balance_factor(root.right) <= 0:  # right-right imbalance
                return self.left_rotate(root)
            else:  # right-left imbalance
                root.right = self.right_rotate(
                    root.right
                )  # update right subtree of root node.
                return self.left_rotate(root)

        return root

    def min_value(self, root: AVLNode):
        if not root or not root.left:
            return root
        return self.min_value(root.left)

    def preorder_traversal(self, root: AVLNode):
        if root:
            print(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


def main():
    # avl = AVL(20)
    #
    # avl.insert(4)
    # avl.insert(26)
    # avl.insert(3)
    # avl.insert(9)
    #
    # avl.insert(15)
    #
    # avl.preorder_traversal(avl.root)
    #
    # print(avl.root, avl.root.left, avl.root.right)

    avl = AVL(2)

    avl.insert(1)
    avl.insert(4)
    avl.insert(3)
    avl.insert(5)

    root = avl.remove(1)

    avl.remove(4)

    avl.preorder_traversal(avl.root)


if __name__ == "__main__":
    main()
