# Link: https://leetcode.com/problems/reverse-string/
# Time: O(N)
# Space: O(N)


def reverse_string(s):
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s)


def reverse_words(s):
    s_words = s.split(" ")
    for i, word in enumerate(s_words):
        s_words[i] = reverse_string(list(word))
    return " ".join(s_words)


def main():
    s = "Let's take LeetCode contest"
    print(reverse_words(s))


if __name__ == "__main__":
    main()
