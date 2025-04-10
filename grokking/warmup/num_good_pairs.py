
# Problem Statement:
# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def goodPairs(nums):
  num_map = {}
  num_pairs = 0

  for i, num in enumerate(nums):
    if num not in num_map:
      num_map[num] = []

    num_map[num].append(i)

  for k, v in num_map.items():
    if len(v) > 1:
      num_pairs += (len(v) * (len(v) - 1)) // 2

  return num_pairs

nums = [1,2,3,1,1,3]
print(goodPairs(nums))

nums = [1,1,1,1]
print(goodPairs(nums))

nums = [1,2,3]
print(goodPairs(nums))
