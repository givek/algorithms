# Binary Search Algorithm
# Time: O(LogN)
# Space: O(1)


def binary_search(sorted_list, start, end, target):
    if start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            return binary_search(sorted_list, mid + 1, end, target)
        else:
            return binary_search(sorted_list, start, mid - 1, target)
    return -1


def main():
    sorted_list = [4, 5, 6, 9, 13, 15]
    target = 15
    print(binary_search(sorted_list, 0, len(sorted_list) - 1, target))


if __name__ == "__main__":
    main()
