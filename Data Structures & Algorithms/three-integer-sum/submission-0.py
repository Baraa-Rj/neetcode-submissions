
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize res as a list, not a defaultdict
        res = []  # This should be a list, not a defaultdict
        
        # Sort the input array
        nums.sort()
        
        for left in range(len(nums) - 2):
            # Skip duplicates for left pointer
            if left > 0 and nums[left] == nums[left - 1]:
                continue
                
            mid = left + 1
            right = len(nums) - 1
            
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                
                if total < 0:
                    mid += 1
                elif total > 0:
                    right -= 1
                else:
                    # When we find a triplet that sums to zero
                    res.append([nums[left], nums[mid], nums[right]])
                    
                    # Skip duplicates for mid and right pointers
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    mid += 1
                    right -= 1
                    
        return res