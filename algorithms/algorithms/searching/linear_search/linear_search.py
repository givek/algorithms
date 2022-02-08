# Linear Search Algorithm
# Time: O(N)
# Space: O(1)


def linear_search(unsorted_list, target):
    for i, element in enumerate(unsorted_list):
        if target == element:
            return i
    return -1


def main():
    unsorted_list = [4, 5, 6, 9, 13, 15]
    target = 15
    print(linear_search(unsorted_list, target))


if __name__ == "__main__":
    main()
