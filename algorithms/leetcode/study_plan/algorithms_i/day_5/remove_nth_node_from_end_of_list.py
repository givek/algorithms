# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Time: O(N)
# Space: O(1)

from algorithms.data_structures.list.node import Node


def len_list(head):
    size = 0
    while head:
        head = head.next
        size += 1
    return size


def remove_nth_node_from_end(head, n):
    if not head or not head.next:
        return None

    size = len_list(head)
    if size == n:
        return head.next

    temp = head
    for _ in range(size - n - 1):
        temp = temp.next

    temp.next = temp.next.next
    return head


def main():
    fifth_node = Node(5)
    fourth_node = Node(4, fifth_node)
    third_node = Node(3, fourth_node)
    second_node = Node(2, third_node)
    head = Node(1, second_node)

    new_head = remove_nth_node_from_end(head, 2)

    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print("X")


if __name__ == "__main__":
    main()
