class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:     
      hash_map = defaultdict(int)
      for num in nums:
        hash_map[num] +=1 
      for k,v in hash_map.items():
        if v > 1:
          return True

      return False