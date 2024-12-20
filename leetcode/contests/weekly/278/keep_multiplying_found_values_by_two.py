# Link: https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/
# Time: O(N)
# Space: O(1)
# Score: 3 / 3


def find_final_value(nums, original):
    if original in nums:
        return find_final_value(nums, original * 2)
    return original


def main():
    nums = [5, 3, 6, 1, 12]
    original = 3

    print(find_final_value(nums, original))


if __name__ == "__main__":
    main()
