# Link: https://leetcode.com/problems/add-two-numbers/
# Time: O(N)
# Space: O(N)


from algorithms.data_structures.list.node import Node, create_list


def add_two_numbers(l1: Node, l2: Node) -> Node:
    carry = 0

    curr_node = new_head = Node(0)

    while l1 and l2:
        total = l1.val + l2.val + carry

        carry = total // 10
        curr_node.next = Node(total % 10)

        l1 = l1.next
        l2 = l2.next

        curr_node = curr_node.next

    while l1:
        total = l1.val + carry

        carry = total // 10
        curr_node.next = Node(total % 10)

        l1 = l1.next

        curr_node = curr_node.next

    while l2:
        total = l2.val + carry

        carry = total // 10
        curr_node.next = Node(total % 10)

        l2 = l2.next

        curr_node = curr_node.next

    if carry == 0:
        return new_head.next

    curr_node.next = Node(carry)
    return new_head.next


def main():
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])

    new_head = add_two_numbers(l1, l2)

    while new_head:
        print(new_head.val, end=" -> ")

        new_head = new_head.next

    print("X")


if __name__ == "__main__":
    main()
