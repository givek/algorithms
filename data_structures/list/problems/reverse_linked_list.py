# Link: https://leetcode.com/problems/reverse-linked-list/
# Time: O(N)
# Space: O(1)


from algorithms.data_structures.list.node import Node, create_list


# Iterative:

# use three pointer approach to reverse a linked list iteratively

# def reverse_list(head: Node) -> Node:
#     prev_node, curr_node = None, head

#     while curr_node:
#         next_node = curr_node.next

#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node

#     return prev_node


# Recursive:

# To reverse a linked list recursively, create a helper function which take prev_node and curr_node as arguments.


def reverse_list(head: Node) -> Node:
    if not head or not head.next:
        return head

    def reverse(prev_node: Node, curr_node: Node) -> Node:
        if not curr_node:
            return prev_node

        next_node = curr_node.next  # store reference to next_node.
        curr_node.next = prev_node  # reverse the link from curr_node -> prev_node.

        return reverse(curr_node, next_node)

    # initially pass argument for prev_node as None, as last node should point to None.
    return reverse(None, head)


def main():
    head = create_list([1, 2, 3, 4, 5])

    new_head = reverse_list(head)

    while new_head:
        print(new_head.val, end=" -> ")

        new_head = new_head.next

    print("X")


if __name__ == "__main__":
    main()
