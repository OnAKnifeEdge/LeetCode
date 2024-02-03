from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, combination, start):
            if remain == 0:
                results.append(combination[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                pick = candidates[i]
                combination.append(pick)
                backtrack(remain - pick, combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return results

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(remain, combination, start):
            if remain == 0:
                results.append(combination[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                pick = candidates[i]
                if remain - pick > target:
                    break
                combination.append(pick)
                backtrack(remain - pick, combination, i + 1)
                combination.pop()

        backtrack(target, [], 0)
        return results


def subsetSums(nums, target):
    nums = sorted(nums)
    results = []

    def backtrack(remain, candidates, start):
        if remain == 0:
            results.append(candidates[:])
            return
        if remain <= 0:
            return
        for i in range(start, len(nums)):
            candidates.append(nums[i])
            backtrack(remain - nums[i], candidates, i + 1)
            candidates.pop()

    backtrack(target, [], 0)
    return results


# candidates = [2, 3, 6, 7]
# target = 7
#
# print(subsetSums([1, 2], 3))

# solution = Solution()
# print(solution.combinationSum(candidates=candidates, target=target))

# https://leetcode.com/problems/combination-sum/solutions/429538/general-backtracking-questions-solutions-in-python-for-reference/


def canFormTriangle(sticks):
    if (len(sticks)) < 3:
        return False
    total_length = sum(sticks)
    if total_length % 3 != 0:
        return False
    target = total_length // 3
    if max(sticks) > target:
        return False
    sides = [0] * 3
    sticks.sort(reverse=True)

    def backtrack(start):
        if start == len(sticks) and all(side == target for side in sides):
            return True
        for i in range(3):
            if sides[i] + sticks[start] > target:
                continue
            sides[i] += sticks[start]
            if backtrack(start + 1):
                return True
            sides[i] -= sticks[start]
            if sides[i] == 0:
                break
        return False

    return backtrack(0)


# [1,1,1]
# true
#
# [1,2,3,4]
# true
#
# [1,2,3,1]
# false
#
# [1,1]
# false
#
# []
# false

# print(canFormTriangle([1, 2, 3, 4]))


def formPolygon(sticks, n):
    # Write Code Here
    if len(sticks) < n:
        return False
    total_length = sum(sticks)
    if total_length % n != 0:
        return False
    target = total_length // n
    if max(sticks) > target:
        return False
    sticks.sort(reverse=True)
    sides = [0] * n

    def backtrack(start):
        if start == len(sticks) and all(side == target for side in sides):
            return True
        for i in range(n):
            if sides[i] + sticks[start] > target:
                continue
            sides[i] += sticks[start]
            if backtrack(start + 1):
                return True
            sides[i] -= sticks[start]
            if sides[i] == 0:
                break
        return False

    return backtrack(0)


# print(formPolygon([1, 1, 1, 1], 4))


def luckyNumbers(num, target):
    result = []

    def recursion(temp: str, start: int, current: int, last: int):
        if start == len(num) and current == target:
            result.append(temp)
            return
        for i in range(start, len(num)):
            if num[start] == '0' and i != start:
                break
            m = num[start: i + 1]
            n = int(m)
            if start == 0:
                recursion(temp + m, i + 1, n, n)
            else:
                recursion(f'{temp} + {m}', i + 1, current + n, n)
                recursion(f'{temp} - {m}', i + 1, current - n, -n)
                recursion(f'{temp} * {m}', i + 1, current - last + last * n, last * n)
                if n != 0 and last % n == 0:
                    recursion(f'{temp} / {m}', i + 1, current - last + last / n, last / n)

    recursion("", 0, 0, 0)
    return result


print(luckyNumbers('123456', 1))
