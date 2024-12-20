# Link: https://leetcode.com/problems/find-original-array-from-doubled-array/
# Time: O(NLogN)
# Space: O(N)


from typing import List


def find_original_array(changed: List[int]) -> List[int]:
    # If the size of the list is an odd integer,
    # it has not been doubled because every integer multiplied by 2 produces an even result.
    if len(changed) % 2 != 0:
        return []

    nums_freq = dict()

    for num in changed:
        nums_freq[num] = nums_freq.get(num, 0) + 1

    original = []

    # Iterate over the list in sorted order, as we need to check for doubles of the smaller numbers first.
    # If we iterate through the list in any random order,
    # there is a chance that the double of a lower number may be treated as the original element.
    # eg: [4, 4, 16, 20, 8, 8, 2, 10]
    for num in sorted(changed):

        if nums_freq.get(num, 0) > 0 and nums_freq.get(num * 2, 0) > 0:

            # remove the current element.
            nums_freq[num] -= 1

            # check if the double exits after removing the original element.
            # eg: double of 0 is 0 * 2 = 0
            if nums_freq.get(num * 2, 0) > 0:
                nums_freq[num * 2] -= 1
                original.append(num)

            # As the element removed was the double as well add it back, as we need two such element to treat them as,
            # original and double.
            else:
                nums_freq[num] += 1

    if len(original) == len(changed) // 2:
        return original

    return []


def main():
    changed = [1, 3, 4, 2, 6, 8]
    print(find_original_array(changed))


if __name__ == "__main__":
    main()
