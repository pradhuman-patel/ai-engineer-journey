def contains_duplicate_v1(nums):
    nums_set = set(nums)
    return len(nums_set) != len(nums)


def contains_duplicate_v2(nums):
  
    return False




print(contains_duplicate_v1([1, 2, 3, 1]))
print(contains_duplicate_v2([1, 2, 3, 4]))
print(contains_duplicate_v2([]))