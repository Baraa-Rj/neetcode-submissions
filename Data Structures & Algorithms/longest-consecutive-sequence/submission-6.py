class Solution:
     def longestConsecutive(self,nums: list[int]) -> int:
        if not nums:
            return 0

        sorted_arr = sorted(nums)
        count = 1
        result = 1

        for i in range(len(sorted_arr) - 1):
            if sorted_arr[i] == sorted_arr[i + 1]:
                continue

            if sorted_arr[i] + 1 == sorted_arr[i + 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1

        return max(result, count)
        