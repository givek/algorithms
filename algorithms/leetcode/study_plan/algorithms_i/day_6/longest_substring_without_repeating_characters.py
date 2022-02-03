# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: O(N)
# Space: O(1)


def length_of_longest_substring(s):
    start = end = max_len = 0
    letter_set = set()
    while end < len(s):
        if not (s[end] in letter_set):
            letter_set.add(s[end])
            max_len = max(max_len, len(letter_set))
            end += 1
        else:
            letter_set.remove(s[start])
            start += 1
    return max_len


def main():
    s = "abcabcbb"
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()
