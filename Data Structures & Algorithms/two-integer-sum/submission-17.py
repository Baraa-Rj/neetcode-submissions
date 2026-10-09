class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash_map:
                return [hash_map[dif],i]
            else:
                hash_map[nums[i]] = i
        return []