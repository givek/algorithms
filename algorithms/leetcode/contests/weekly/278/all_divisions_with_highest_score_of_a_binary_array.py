# Link: https://leetcode.com/contest/weekly-contest-278/problems/all-divisions-with-the-highest-score-of-a-binary-array/
# Time: O(N)
# Space: O(N)
# Score: 4 / 4


from typing import List


def max_score_indices(nums: List[int]):
    zero_total = one_total = 0
    for num in nums:
        if num == 0:
            zero_total += 1
        else:
            one_total += 1

    if not zero_total:
        return [len(nums)]
    if not one_total:
        return [0]

    max_score = max(zero_total, one_total)

    last_score = [one_total]
    last_zero_score = 0
    for i in range(1, len(nums)):
        if nums[i - 1] == 0:
            last_score.append(last_score[i - 1] + (last_zero_score + 1))
        else:
            last_score.append((last_score[i - 1] - 1) + last_zero_score)

        max_score = max(last_score[i], max_score)

    last_score.append(zero_total)
    return [i for i, num in enumerate(last_score) if num == max_score]


def main():
    nums = [0, 0, 0]
    print(max_score_indices(nums))


if __name__ == "__main__":
    main()
