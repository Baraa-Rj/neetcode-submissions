from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        sett = set(nums)
        for num in sett:
            if num-1 not in sett:
                current =1 
                while num+1 in sett:
                    current +=1
                    num = num+1
                longest = max(current,longest)
        return longest
     
