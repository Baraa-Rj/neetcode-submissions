class Solution {
    public boolean hasDuplicate(int[] nums) {
        if(nums == null)
            return false;
        Arrays.sort(nums);
        for (int i =1; i<nums.length;i++){
            if(nums[i-1] == nums[i])
                return true;
        }
        return false;
    }
}