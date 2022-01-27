# Link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# Time: O(N)
# Space: O(N)


def reverse_parentheses(s):
    stack, queue = [], []

    for char in s:
        if char == ")":
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()  # remove '('

            while queue:
                stack.append(queue.pop(0))
        else:
            stack.append(char)

    return "".join(stack)


def main():
    s = "(ed(et(oc))el)"
    print(reverse_parentheses(s))


if __name__ == "__main__":
    main()
