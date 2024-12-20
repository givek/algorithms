# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Time: O(N)
# Space: O(N)


# def sorted_squares(nums):
#     j = 0
#     while nums[j] < 0:
#         j += 1

#     i = j - 1

#     for x, num in enumerate(nums):
#         nums[x] = num * num

#     result = []

#     while i >= 0 and j < len(nums):
#         if nums[i] < nums[j]:
#             result.append(nums[i])
#             i -= 1
#         else:
#             result.append(nums[j])
#             j += 1

#     while i >= 0:
#         result.append(nums[i])
#         i -= 1

#     while j < len(nums):
#         result.append(nums[j])
#         j += 1

#     return result


def sorted_squares(nums):
    start, end = 0, len(nums) - 1
    result = [0] * len(nums)

    for i in reversed(range(len(nums))):
        if abs(nums[start]) < abs(nums[end]):
            result[i] = nums[end] * nums[end]
            end -= 1
        else:
            result[i] = nums[start] * nums[start]
            start += 1
    return result


def main():
    nums = [-4, -1, 0, 3, 10]
    print(sorted_squares(nums))


if __name__ == "__main__":
    main()
