# Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next_node=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next_node
        self.child = child


# Algorithm 1:
# Time: O(N), where N is total number of nodes in the list.
# Space: O(C), where C is number of nodes with child pointers.

# NOTE: This algorithm will not work if more than one node have a child node at the same level.


# * use a stack keep track of the next node when a node has a child node.
# * make the child node the next node and push the next node on the stack.
# * once the temp pointer reaches the last node of the last level, pop the last next node from the stack and set that
#   sub-list as the next of that last node.
# * do this till the stack is empty.


# def flatten(head: Node) -> Node:
#     if not head:
#         return head
#
#     temp = head
#     next_node_stack = deque()
#
#     while temp and (temp.next or temp.child):
#         if temp.child:
#             next_node_stack.append(temp.next)
#             temp.next = temp.child
#             temp.next.prev = temp
#             temp.child = None
#         temp = temp.next
#
#     while temp and next_node_stack:
#         temp.next = next_node_stack.pop()
#         if temp.next:
#             temp.next.prev = temp
#
#         while temp.next:
#             temp = temp.next
#
#     return head


# Algorithm 2:
# Time: O(N), where N is total number of nodes in the list.
# Space: O(L), where L is total number of levels.


# 1---2---3---4---5---6--NULL
#         |
#         7---8---9---10--NULL
#             |
#             11--12--NULL

# [1]
# [ ]   , 1
# [2]   , 1
# [ ]   , 1 -> 2
# [3]   , 1 -> 2
# [ ]   , 1 -> 2 -> 3
# [4, 7], 1 -> 2 -> 3       (first add the next and then add the child node.)
# [4]   , 1 -> 2 -> 3 -> 7  (as we are using a stack the child node will be popped first.)
# ...


def flatten(head: Node) -> Node:
    if not head:
        return head

    # initialize the stack with head node and prev node as None.
    node_stack, prev = [head], None

    while node_stack:
        curr = node_stack.pop()  # get the curr node from the stack.

        # push the next and child nodes of the curr node onto the stack if it has any.
        if curr.next:
            node_stack.append(curr.next)
        if curr.child:
            node_stack.append(curr.child)

        # reset the curr pointer of the prev and prev pointer the curr node.
        # set the child pointer of the curr node to None.
        if prev:
            prev.next = curr
        curr.prev = prev
        curr.child = None
        prev = curr  # for the next iteration set the curr node as prev.

    return head


def main():
    head = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    head.next, two.prev = two, head
    two.next, three.prev = three, two
    three.next, four.prev = four, three
    four.next, five.prev = five, four
    five.next, six.prev = six, five

    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)

    three.child = seven
    five.child = nine

    seven.next, eight.prev = eight, seven
    # eight.next, nine.prev = nine, eight
    nine.next, ten.prev = ten, nine

    new_head = flatten(head)

    while new_head:
        print(new_head.val)
        new_head = new_head.next


if __name__ == "__main__":
    main()
