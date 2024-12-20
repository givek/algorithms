# Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Time: O(N^2)
# Space: O(N)


def concatenated_binary(n: int):
    binary_str = ""

    for i in range(n):  # N
        binary_str += str(bin(i + 1))[2:]

    return int(binary_str, 2) % (10**9 + 7)


def main():
    print(concatenated_binary(3))


if __name__ == "__main__":
    main()
