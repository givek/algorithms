# Link: https://leetcode.com/problems/permutation-in-string/
# Time: O(N)
# Space: O(1)


# - add count of all letters in `s1` to `dict`
#
# - maintain a sliding window of len(s1), move from beginning to end of `s2`.
#
# - when a letter enters the sliding window, decrease the letter count of that letter by 1 in the `dict`.
#
# - when a letter leaves the sliding window, increase the letter count of that letter by 1 in the `dict`.
#
# - at any point if all values in the `dict` are equal to zero, return True
#
# - because we initially add count of elements of `s1` to dict, if `s2` contains a permutation of  `s1`
#   they will cancel each other and all values of dict will be zero.


def check_inclusion(s1: str, s2: str):
    len_s1, len_s2 = len(s1), len(s2)

    if len_s1 > len_s2:
        return False

    letter_count = dict()

    # add count of all letters in `s1` to `dict`.
    # create window on `s2` from 0 -> len(s1). Thus decrease the letter count of letters entering window.
    for i in range(len_s1):
        letter_count[s1[i]] = letter_count.get(s1[i], 0) + 1
        letter_count[s2[i]] = letter_count.get(s2[i], 0) - 1

    # check if all values in the `dict` are equal to zero.
    if all(value == 0 for value in letter_count.values()):
        return True

    # iterate from len_s1 -> len_2, as we already iterated from 0 -> len_1 in previous loop.
    for i in range(len_s1, len_s2):
        # calculate start and end of sliding window.
        start, end = i - len_s1, i

        # decrease count by 1 for elements entering the window
        letter_count[s2[end]] = letter_count.get(s2[end], 0) - 1
        # increase count by 1 for elements leaving the window
        letter_count[s2[start]] = letter_count.get(s2[start], 0) + 1

        if all(value == 0 for value in letter_count.values()):
            return True
    return False


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    print(check_inclusion(s1, s2))


if __name__ == "__main__":
    main()
