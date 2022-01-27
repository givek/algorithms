# Link: https://leetcode.com/problems/validate-stack-sequences/
# Time: O(N)
# Space: O(N)


# def validate_stack_sequences(pushed, popped):
#     stack, i = [], 0
#     while stack or popped:
#         if i < len(pushed):
#             stack.append(pushed[i])
#         elif stack[-1] != popped[0]:
#             return False

#         while stack and popped and stack[-1] == popped[0]:
#             stack.pop()
#             popped.pop(0)
#         i += 1

#     return (not stack) and (not popped)


def validate_stack_sequences(pushed, popped):
    stack, i = [], 0

    for element in pushed:
        stack.append(element)

        while stack and stack[-1] == popped[i]:
            i += 1
            stack.pop()

    return not stack


def main():
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(validate_stack_sequences(pushed, popped))


if __name__ == "__main__":
    main()
