class Solution:
    def topKFrequent(self,nums: List[int], k: int) -> List[int]:
        my_dict=Counter(nums)
        sorted_dict = dict(
        sorted(my_dict.items(), key=lambda x: x[1], reverse=True))          
        return list(sorted_dict.keys())[:k]
