class Solution {
      public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(i, nums[i]);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsValue(complement)) {
                for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                    if (entry.getValue() == complement && entry.getKey() != i) {
                        return new int[]{i, entry.getKey()};
                    }
                }
            }
        }
        return null;
    }
}
