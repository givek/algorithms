# Link: https://leetcode.com/problems/binary-search/
# Time: O(LogN)
# Space: O(1)


def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums, target))


if __name__ == "__main__":
    main()
