# Link: https://leetcode.com/problems/search-insert-position/
# Time: O(LogN)
# Space: O(1)


def search_insert_position(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


def main():
    nums = [1, 3, 5, 6]
    target = 7
    print(search_insert_position(nums, target))


if __name__ == "__main__":
    main()
