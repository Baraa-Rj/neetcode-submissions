class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]*len(nums)
        suffix=[1]*len(nums)
        result=[]
        n=1
        for i in range(len(nums)):
                suffix[i]*=n
                n*=nums[i]
        n=1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i]*=n
            n*=nums[i]
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result



        



        