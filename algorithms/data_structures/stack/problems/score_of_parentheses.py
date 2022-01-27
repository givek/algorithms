# Link: https://leetcode.com/problems/score-of-parentheses/
# Time: O(N)
# Space: O(N)


def score_of_parenthesis(s):
    stack = [0]
    for paren in s:
        if paren == "(":
            stack.append(0)
        else:
            last_sum = stack.pop()
            stack[-1] += max(2 * last_sum, 1)
    return stack.pop()


def main():
    s = "(((())))()((()))"
    print(score_of_parenthesis(s))


if __name__ == "__main__":
    main()
