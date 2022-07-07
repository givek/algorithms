# Link: https://leetcode.com/problems/invert-binary-tree/
# Time: O(N)
# Space: O(1)


from algorithms.data_structures.trees.binary_tree_node import (
    BinaryTreeNode,
    create_binary_tree,
)


def invert_tree(root: BinaryTreeNode) -> BinaryTreeNode:
    if not root:
        return root

    # swap left subtree with right subtree.
    root.left, root.right = root.right, root.left

    # do it recursively for all the nodes in the tree.
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def main():
    node_vals = [4, 2, 7, 1, 3, 6, 9]

    root = create_binary_tree(node_vals)

    new_root = invert_tree(root)

    print(f"{new_root.left.val}-{new_root.val}-{new_root.right.val}")


if __name__ == "__main__":
    main()
