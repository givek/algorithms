from typing import List


# Counting Sort is a non-comparison based sorting algorithm, which operates by counting the frequency of elements
# appearing in the array and then arranging them accordingly.


def counting_sort(unsorted_list: List[int]):
    if not unsorted_list:
        return unsorted_list

    max_element = max(unsorted_list)

    freq_count = [0] * (max_element + 1)

    for num in unsorted_list:
        freq_count[num] += 1

    i = j = 0

    while i < len(unsorted_list):
        while freq_count[j] > 0:
            unsorted_list[i] = j
            freq_count[j] -= 1
            i += 1
        j += 1

    return unsorted_list


def main():
    unsorted_list = [6, 9, 2, 10, 8, 6, 4, 1, 5, 9, 4, 6, 9, 6, 1]
    # unsorted_list = []
    # unsorted_list = [5]
    # unsorted_list = [0, 0, 0, 0, 0],
    # unsorted_list = [0, 1, 1, 4, 5, 5, 7, 9]
    # unsorted_list = [9, 7, 5, 5, 4, 1, 1, 0]

    print(counting_sort(unsorted_list))


if __name__ == "__main__":
    main()
