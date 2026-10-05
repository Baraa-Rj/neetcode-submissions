class Solution {
      public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null) {
            return new ArrayList<>();
        }
        Map<String, ArrayList<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] charS = s.toCharArray();
            Arrays.sort(charS);
            String string = String.valueOf(charS);
            map.putIfAbsent(string, new ArrayList<>());
            map.get(string).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
