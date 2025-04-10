
# Problem:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.

def contains_duplicates(nums):
  """
  Time Complexity: O(n)
  Space Complexity: O(n)
  """
  num_set = set()

  duplicates = False

  for num in nums:
    if num in num_set:
      duplicates = True
      break
    num_set.add(num)

  print(f'Duplicates: {duplicates}')

nums = [1, 2, 3, 4]
print(nums)
contains_duplicates(nums)

print('')

nums = [1, 2, 1, 5]
print(nums)
contains_duplicates(nums)
