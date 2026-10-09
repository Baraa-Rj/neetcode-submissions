class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      array_set = set()
      for i in range(len(nums)):
        if nums[i] in array_set:
          return True
        else:
          array_set.add(nums[i])
      
      return False