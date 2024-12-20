# Link: https://leetcode.com/problems/find-the-town-judge/
# Time: O(N)
# Space: O(N)


def find_judge(n: int, trust: list[list[int]]) -> int:
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for a, b in trust:
        out_degree[a] += 1
        in_degree[b] += 1

    # judge should be trusted by (n - 1) people: in-degree.
    # judge should trust nobody: out-degree = 0

    for i in range(1, n + 1):
        if in_degree[i] - out_degree[i] == n - 1:
            return i

    return -1


def main():
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]

    print(find_judge(n, trust))


if __name__ == "__main__":
    main()
