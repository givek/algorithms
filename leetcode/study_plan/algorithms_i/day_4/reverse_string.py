# Link: https://leetcode.com/problems/reverse-string/
# Time: O(N/2)
# Space: O(1)


def reverse_string(s):
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def main():
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)


if __name__ == "__main__":
    main()
