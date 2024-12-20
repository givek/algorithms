# Link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Time: O(N)
# Space: O(1)


from algorithms.data_structures.list.node import Node, create_list


# Recursive Approach

# By swapping every two adjacent nodes, we will be able to achieve the desired result.
#
# 1 2 3 4
# | |
# h t, where h: head and t: temp
#
# But before we set 2.next to 1, we need to swap the last pair in the list and return the pointer to the last node in
# that pair.
#
# 1 2 3 4
#     | |
#     h t
#
# We get head.next = 4, as the next head does not have a next pointer.
# Now, we can swap the nodes and return pointer to the last node in the pair (4, in this case).


def swap_pairs(head: Node) -> Node:
    if not head or not head.next:
        return head

    temp = head.next
    head.next = swap_pairs(head.next.next)
    temp.next = head
    return temp


def main():
    head = create_list([1, 2, 3, 4])

    new_head = swap_pairs(head)

    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next

    print("X")


if __name__ == "__main__":
    main()
