# Link: https://leetcode.com/problems/next-greater-element-i/
# Time: O(N)
# Space: O(N)


def cal_points(ops):
    score_stack = []
    for op in ops:
        if op == "+":
            new_score = score_stack[-1] + score_stack[-2]
            score_stack.append(new_score)
        elif op == "D":
            new_score = score_stack[-1] * 2
            score_stack.append(new_score)
        elif op == "C":
            score_stack.pop()
        else:
            score_stack.append(int(op))
    return sum(score_stack)


def main():
    ops = ["5", "2", "C", "D", "+"]
    print(cal_points(ops))


if __name__ == "__main__":
    main()
