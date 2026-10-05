class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hash_map = set()
        for num in nums:
            if num in hash_map:
                return True
            hash_map.add(num)
        return False