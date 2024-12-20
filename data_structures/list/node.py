class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


from typing import List


def create_list(node_vals: List[int]) -> Node:
    head = temp = Node(node_vals.pop(0))
    for val in node_vals:
        temp.next = Node(val)
        temp = temp.next
    return head
