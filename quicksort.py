def quicksort(nums):
  if not nums:
    return []
  if len(nums) == 1:
    return [nums[0]]
  pivot = nums[0]
  return quicksort([i for i in nums[1:] if i < pivot]) + [pivot] + quicksort([i for i in nums[1:] if i >= pivot])

a = [1,2,0,3,6,9,3,2,4,7]
print quicksort(a)
