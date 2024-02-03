nums = [1, 2, 3, 4, 5, 6, 7, -2]
target = 5


def subset_sum_rec(nums, target, i):
    results = []
    # subset found
    if target == 0:
        return
    if target < 0:
        return
    if i >= len(nums):
        return
    # include nums[i]
    include = subset_sum_rec(nums, target - nums[i], i + 1)
    if include:
        for r in include:
            r.append(i)
        results.extend(include)
    # exclude nums[i]
    exclude = subset_sum_rec(nums, target, i + 1)
    if exclude:
        results.extend(exclude)
    return results
