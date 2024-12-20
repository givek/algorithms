# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time: O(LogN)
# Space: O(1)


def binary_search(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def two_sums(numbers, target):
    for i, num in enumerate(numbers):
        j = binary_search(numbers, i + 1, len(numbers) - 1, target - num)

        if j != -1:
            return [i + 1, j + 1]


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sums(numbers, target))


if __name__ == "__main__":
    main()
