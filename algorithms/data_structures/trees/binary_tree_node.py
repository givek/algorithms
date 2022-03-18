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
