# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Time: O(LogN)
# Space: O(1)


# As the given array is rotated sorted, binary search cannot be applied directly.


def search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            return mid

        if nums[start] <= nums[mid]:  # the array is sorted from start to mid.
            if nums[start] <= target < nums[mid]:
                # as the target lies between start and mid, reduce the search window.
                end = mid - 1
            else:
                # if target does not lie between start and mid, search from (mid + 1) - end.
                start = mid + 1
        else:  # here the array is sorted from mid to end.
            if nums[mid] < target <= nums[end]:
                # as the target lies between mid and end, reduce the search window.
                start = mid + 1
            else:
                # the target does not lie between mid and end, search from start - (mid - 1)
                end = mid - 1
    return -1


def main():
    nums = [3, 5, 1]
    target = 3
    print(search(nums, target))


if __name__ == "__main__":
    main()
