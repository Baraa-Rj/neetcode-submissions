class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        heap = []
        for key in counter:
            heapq.heappush(heap, (-counter[key], key))
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans