# Link: https://leetcode.com/problems/path-sum-ii/
# Time: O(N)
# Space: O(N), excluding the space required to the answer.


from algorithms.data_structures.trees.binary_tree_node import create_binary_tree


def binary_tree_sum(root, curr_sum, curr_list, target_sum):
    if not root:
        return []

    curr_list.append(root.val)

    # Leaf node
    if not root.left and not root.right:

        if root.val + curr_sum == target_sum:
            return [curr_list]

        return []

    ans = []

    if root.left:
        left_list = binary_tree_sum(
            root.left, curr_sum + root.val, curr_list, target_sum
        )

        if left_list:
            for path in left_list:
                # Append deep-copy of the path list (curr_list), as we pop values out of it as we continue.
                ans.append(list(path))

        if curr_list:
            # Remove the last value while traversing back through the recursion.
            curr_list.pop()

    if root.right:
        right_list = binary_tree_sum(
            root.right, curr_sum + root.val, curr_list, target_sum
        )

        if right_list:
            for path in right_list:
                # Append deep-copy of the path list (curr_list), as we pop values out of it as we continue.
                ans.append(list(path))

        if curr_list:
            # Remove the last value while traversing back through the recursion.
            curr_list.pop()

    return ans


def path_sum(root, target_sum):
    return binary_tree_sum(root, 0, [], target_sum)


def main():
    # node_vals = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    # target_sum = 22

    node_vals = [1, -2, -3, 1, 3, -2, None, -1]
    target_sum = 2

    root = create_binary_tree(node_vals)

    print(path_sum(root, target_sum))


if __name__ == "__main__":
    main()
