# Link: https://leetcode.com/problems/palindrome-linked-list/
# Time: O(N)
# Space: O(1)


from algorithms.data_structures.list.node import Node, create_list


def check_palindrome(head: Node, tail: Node) -> (Node, bool):
    if not tail.next:
        if head.val == tail.val:
            return head.next, True
        return head.next, False

    head_next, is_equal = check_palindrome(head, tail.next)

    if not is_equal:
        return head_next.next, False

    if head_next.val == tail.val:
        return head_next.next, True

    return head_next.next, False


def is_palindrome(head: Node):
    _, is_equal = check_palindrome(head, head)
    return is_equal


def main():
    node_vals = [1, 5, 2, 1]

    head = create_list(node_vals)

    print(is_palindrome(head))


if __name__ == "__main__":
    main()
