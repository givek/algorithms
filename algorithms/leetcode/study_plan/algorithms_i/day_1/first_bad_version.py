# Link: https://leetcode.com/problems/first-bad-version/
# Time: O(LogN)
# Space: O(1)


def first_bad_version(n):
    first_ver, last_ver = 0, n
    while first_ver <= last_ver:
        mid = (first_ver + last_ver) // 2
        if not isBadVersion(mid - 1) and isBadVersion(mid):
            return mid
        elif not isBadVersion(mid) and isBadVersion(mid + 1):
            return mid + 1
        elif not isBadVersion(first_ver) and isBadVersion(mid):
            last_ver = mid - 1
        else:
            first_ver = mid + 1
    return -1
