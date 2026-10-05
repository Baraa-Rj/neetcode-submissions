class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        Arrays.fill(output, 1);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                for (int j = 0; j < nums.length; j++) {
                    if (i != j) {
                        output[i] *= nums[j];
                    }
                }
                continue;
            }
            for (int num : nums) {
                output[i] *= num;
            }
            if (nums[i] != 0)
                output[i] /= nums[i];
        }
        return output;
    }
}  
