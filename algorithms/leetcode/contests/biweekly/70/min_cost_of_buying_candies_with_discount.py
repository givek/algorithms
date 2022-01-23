# Link: https://leetcode.com/contest/biweekly-contest-70/problems/minimum-cost-of-buying-candies-with-discount/
# Time: O(NlogN)
# Space: O(1)
# Score: 0


def minimumCost(cost):
    if len(cost) <= 2:
        return sum(cost)
    cost.sort(reverse=True)
    x = 2
    sum_cost = 0
    for candy_cost in cost:
        if not x:
            x = 2
            continue

        sum_cost += candy_cost
        x -= 1
    return sum_cost


def main():
    pass


if __name__ == "__main__":
    main()
