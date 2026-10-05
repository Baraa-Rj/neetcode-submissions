class Solution {
   public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.merge(num, 1, Integer::sum);
        }
        int[] result = new int[k];
        Map.Entry<Integer, Integer> maxEntry = null;
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < k; i++) {
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (maxEntry == null || entry.getValue().compareTo(maxEntry.getValue()) > 0) {
                    maxEntry = entry;
                }

            }
            assert maxEntry != null;
            maxValue = maxEntry.getKey();
            map.remove(maxEntry.getKey());
            result[i] = maxValue;
            maxEntry = null;
        }
        return result;
    }


}
