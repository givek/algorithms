# Selection Sort Algorithm
# Time: O(N^2)
# Space: O(1)


# * Selection sort is an in-place sorting algorithm.
# * The algorithm divides the list into two parts: a sorted sub-list of elements which is built up from left to right
#   and sub-list of remaining unsorted elements
# * Initially, the sorted sub-list is empty. The algorithm **selects** the minimum element from the unsorted sub-list
#   and swaps it with the leftmost unsorted element.


from typing import List


def selection_sort(unsorted_list: List[int]) -> List[int]:
    list_size = len(unsorted_list)

    # `i` keeps track of the leftmost unsorted element.
    for i in range(list_size):
        # `j` iterates through the list to find the minimum element in the unsorted sub-list.
        for j in range(i + 1, list_size):
            # if element < `unsorted[i]` is found, swap.
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


def main():
    unsorted_list = [2, 1, 4, 3, 9, 5]
    sorted_list = selection_sort(unsorted_list)
    print(sorted_list)


if __name__ == "__main__":
    main()
