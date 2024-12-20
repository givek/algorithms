class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right

    def __str__(self):
        left_val = right_val = None
        if self.left:
            left_val = self.left.val
        if self.right:
            right_val = self.right.val
        return f"({left_val} {self.val} {right_val})"

    def __repr__(self):
        left_val = right_val = None
        if self.left:
            left_val = self.left.val
        if self.right:
            right_val = self.right.val
        return f"({left_val} {self.val} {right_val})"


from typing import List


def create_binary_tree(node_vals: List[int]) -> BinaryTreeNode:
    """Creates a binary tree from the given list and returns the root node of the binary tree."""

    # if value for root node is None, return None.
    if not node_vals[0]:
        return None

    root = BinaryTreeNode(node_vals.pop(0))
    tree_node_queue = [root]

    while node_vals:
        left_val = right_val = None
        if node_vals:
            left_val = node_vals.pop(0)
        if node_vals:
            right_val = node_vals.pop(0)

        curr_root = tree_node_queue.pop(0)

        if left_val:
            curr_root.left = BinaryTreeNode(left_val)
            tree_node_queue.append(curr_root.left)

        if right_val:
            curr_root.right = BinaryTreeNode(right_val)
            tree_node_queue.append(curr_root.right)

    return root
