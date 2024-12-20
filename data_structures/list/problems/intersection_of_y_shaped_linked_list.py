# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/


# Solution 1:

# Time: O(N)
# Space: O(N)


# Traverse the list from `head_a` and add all the nodes to a set. Then again traverse the list from head_b, while
# traversing check if the node is present in the set. If present return that node.


# def get_intersection_node(head_a, head_b):
#     list_nodes = set()
#     temp_a, temp_b = head_a, head_b
#     while temp_a:
#         list_nodes.add(temp_a)
#         temp_a = temp_a.next
#
#     while temp_b:
#         if temp_b in list_nodes:
#             return temp_b
#         temp_b = temp_b.next
#     return temp_b


# Solution 2:

# Time: O(N)
# Space: O(1)


def list_size(head):
    size = 0
    while head:
        head = head.next
        size += 1
    return size


# Calculate the size of both lists, then get the difference between the size of lists.
# Skip `size_diff` nodes from the longer list, so that now both pointers will traverse equal number of nodes.


def get_intersection_node(head_a, head_b):
    temp_a, temp_b = head_a, head_b
    size_a, size_b = list_size(temp_a), list_size(temp_b)

    size_diff = abs(size_a - size_b)

    if size_a < size_b:
        while size_diff != 0:
            temp_b = temp_b.next
            size_diff -= 1
    else:
        while size_diff != 0:
            temp_a = temp_a.next
            size_diff -= 1

    while temp_a and temp_b:
        if temp_a == temp_b:  # if both pointers point to the same node,
            return temp_a  # return that node, as that is the intersecting point.
        temp_a = temp_a.next
        temp_b = temp_b.next

    return None


def main():
    pass


if __name__ == "__main__":
    main()
