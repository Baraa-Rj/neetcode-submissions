class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Left pass: calculate prefix products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Right pass: calculate suffix products and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
