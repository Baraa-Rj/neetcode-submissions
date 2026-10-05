class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [0]*(k)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in range(0,k):
            max_element = max(count,key = count.get)
            res[i] = max_element
            count.pop(max_element)
        return res
