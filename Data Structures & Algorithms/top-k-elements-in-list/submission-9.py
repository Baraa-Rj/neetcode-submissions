class Solution:
    def topKFrequent(self,nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = [(v, key) for key, v in freq_map.items()]
        heapq.heapify_max(heap)
        result = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            result.append(key)
            heapq.heapify_max(heap)
        return result