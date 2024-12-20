# Link: https://leetcode.com/problems/next-greater-element-i/
# Time: O(N)
# Space: O(N)


# - We use a stack to keep a decreasing sub-sequence, while iterating through `nums1` if we see a number `x` greater
#   than `stack.top()` we pop all elements less than `x` and for all the popped elements, their next greater element
#   is `x`
# - For example `[9, 8, 7, 3, 2, 1, 6]`
#   The stack will first contain `[9, 8, 7, 3, 2, 1]` and then we see `6` which is greater than `1`, `2` and `3`, So we
#   pop them. Thus, their next greater element is `6`.


def next_greater_element(nums1, nums2):
    next_greater = dict()
    dec_stack = []

    for num in nums2:
        while dec_stack and dec_stack[-1] < num:
            next_greater[dec_stack.pop()] = num
        dec_stack.append(num)

    next_greater_list = []
    for num in nums1:
        next_greater_num = next_greater.get(num, -1)
        next_greater_list.append(next_greater_num)
    return next_greater_list
