class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        n=1
        for i in range(len(nums)):
                result[i]=n
                n*=nums[i]
        n=1
        for i in range(len(nums) - 1, -1, -1):
            result[i]*=n
            n*=nums[i]
        return result



        



        