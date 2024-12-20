# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Time: O(N/2)
# Space: O(1)


from algorithms.data_structures.list.node import create_list


# Traverse two nodes at a time with the fast pointer, and a single node with the slow pointer.
# When the fast pointer reaches the end of the list, slow will point to the middle node.


def middle_node(head):
    slow = fast = head
    while fast and fast.next:  # check if fast and fast.next exist.
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    head = create_list([1, 2, 3, 4, 5, 6])
    mid_node = middle_node(head)
    print(mid_node)


if __name__ == "__main__":
    main()
