class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA =0
        l , r = 0 , len(height)-1
        while l<r :
            width = r-l 
            area = (width) * (min(height[l],height[r]))
            maxA = max(maxA,area)
            if height[l]> height[r]:
                r -=1
            else:
                l +=1
        return maxA
        