# Link: https://leetcode.com/contest/biweekly-contest-82/problems/evaluate-boolean-binary-tree/
# Time: O(N)
# Space: O(1)
# Score: 3


def evaluate_tree(root):
    if not root.left and not root.right:
        # leaf nodes can only have val = 0 or 1.
        if root.val == 1:  # 1 == True
            return True
        else:  # 0 == False
            return False

    left_val = evaluate_tree(root.left)
    right_val = evaluate_tree(root.right)

    # non-leaf nodes can only have val = 2 or 3.
    if root.val == 2:  # 2 == OR
        return left_val or right_val
    else:  # 3 == AND
        return left_val and right_val
