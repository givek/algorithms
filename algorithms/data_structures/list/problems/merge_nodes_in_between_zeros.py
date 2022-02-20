# Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Time: O(N)
# Space: O(1)


from algorithms.data_structures.list.node import Node, create_list


# def merge_nodes(head: Node) -> Node:
#     if not head or not head.next:
#         return None
#
#     temp = new_head = Node(0)
#     curr_node, nodes_sum = head.next, 0
#
#     while curr_node:
#         if curr_node.val == 0:
#             temp.next = Node(nodes_sum)
#             temp = temp.next
#             nodes_sum = 0
#         nodes_sum += curr_node.val
#         curr_node = curr_node.next
#     return new_head.next


def merge_nodes(head: Node) -> Node:
    if not head or not head.next:
        return None

    # maintain a `curr_node` pointer to traverse the list and `nodes_sum` to store the sum of nodes inbetween zeros.
    curr_node, nodes_sum = head.next, 0

    # maintain a `prev_node` pointer, which points to the previous merged node.
    prev_node = head

    while curr_node:
        nodes_sum += curr_node.val  # add the value to each node to `nodes_sum`.

        # zero indicates the end of previous interval and start of new interval.
        if curr_node.val == 0:
            curr_node.val = nodes_sum  # replace `curr_node.val`(0) with `nodes_sum`.
            prev_node.next = curr_node  # skip all the nodes inbetween.
            prev_node = curr_node  # set `curr_node` as new previous.
            nodes_sum = 0  # reset the `nodes_sum` as a new interval starts.

        curr_node = curr_node.next
    return head.next


def main():
    head = create_list([0, 3, 1, 0, 4, 5, 2, 0])

    new_head = merge_nodes(head)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("X")


if __name__ == "__main__":
    main()
