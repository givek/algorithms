# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Time: O(2N)
# Space: (N)


def reverse_words(s: str) -> str:
    s_list = list(s)

    start = 0
    for i in range(len(s_list)):

        if s_list[i] == " ":

            end = i - 1

            while start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]

                start += 1
                end -= 1

            start = i + 1

    end = len(s_list) - 1

    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]

        start += 1
        end -= 1

    return "".join(s_list)
