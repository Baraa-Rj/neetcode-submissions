class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> myList = new ArrayList<>();
        ArrayList<String> temp = new ArrayList<>(Arrays.stream(strs).toList());
        for(int i =0;i < strs.length;i++){
            if(temp.contains(strs[i])){
                ArrayList<String> anagramGroup = new ArrayList<>();
                anagramGroup.add(strs[i]);
                temp.remove(strs[i]);
                for(int j = i+1;j < strs.length;j++){
                    char[] str1 = strs[i].toCharArray();
                    char[] str2 = strs[j].toCharArray();
                    Arrays.sort(str1);
                    Arrays.sort(str2);
                    if(Arrays.equals(str1, str2) && temp.contains(strs[j])){
                        anagramGroup.add(strs[j]);
                        temp.remove(strs[j]);
                    }
                }
                myList.add(anagramGroup);
            }
        }
        return myList;
    }
}
