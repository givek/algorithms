# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Time: O(N)
# Space: O(1)

from algorithms.data_structures.list.node import Node


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    fifth_node = Node(5)
    fourth_node = Node(4, fifth_node)
    third_node = Node(3, fourth_node)
    second_node = Node(2, third_node)
    head = Node(1, second_node)

    print(middle_node(head))


if __name__ == "__main__":
    main()
