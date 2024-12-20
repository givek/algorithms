from algorithms.data_structures.trees.binary_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, val=None):
        self.root = BinaryTreeNode(val)

    def insert(self, val):
        self.root = self.insert_node(self.root, val)

    def insert_node(self, root: BinaryTreeNode, val):
        if not root:
            return BinaryTreeNode(val)

        if val < root.val:
            root.left = self.insert_node(root.left, val)
        else:
            root.right = self.insert_node(root.right, val)

        return root

    def remove(self, val):
        node = self.search(val)
        return self.remove_node(self.root, node)

    def remove_node(self, root: BinaryTreeNode, node: BinaryTreeNode):
        # case 1: When the node to be removed is a leaf node.
        if not node.left and not node.right:
            parent_node = self.find_parent(self.root, node)

            if not parent_node:
                return None

            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None

            return node

        # case 2: When the node to be removed has only one child.
        if not node.left:
            parent_node = self.find_parent(self.root, node)

            if parent_node.left == node:
                parent_node.left = node.right
            else:
                parent_node.right = node.right

            return node

        if not node.right:
            parent_node = self.find_parent(self.root, node)

            if parent_node.left == node:
                parent_node.left = node.left
            else:
                parent_node.right = node.left

            return node

        # case 3: When the node to be removed has both left and right child.
        if node.left and node.right:
            # find inorder successor in the left subtree.
            successor_node = self.inorder_successor(root.right)
            successor_parent = self.find_parent(root, successor_node)

            if successor_parent.left == successor_node:
                successor_parent.left = None
            else:
                successor_parent.right = None

            root.val = successor_node.val

            return node

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
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)

    def inorder_traversal(self, root: BinaryTreeNode):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)
            print(root.val)


def main():
    tree = BinarySearchTree(6)

    tree.insert(7)
    tree.insert(1)
    tree.insert(9)
    tree.insert(8)
    tree.insert(3)
    tree.insert(5)

    # tree.inorder_traversal(tree.root)
    #
    # print(tree.search(1))
    # print(tree.search(11))

    # tree.remove(5)
    tree.remove(7)
    tree.remove(6)
    tree.inorder_traversal(tree.root)


if __name__ == "__main__":
    main()
