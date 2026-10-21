def two_sums(nums: list[int], target: int) -> list[int]:
    """Return the indexes of the two numbers that add up to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i
    return []



print(two_sums([2, 7, 11, 15], 9))
print(two_sums([3, 2, 4], 6))
print(two_sums([3, 3], 6))