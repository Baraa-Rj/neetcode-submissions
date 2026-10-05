class Solution {

  
    private String encode(List<String> list){
        StringBuilder builder = new StringBuilder();
        for (String item : list) {
            builder.append(item.length()).append('#').append(item);
        }
        return builder.toString();
    }

    private List<String> decode(String string){
        List<String> myList = new ArrayList<>();
        int index = 0;
        while (index < string.length()) {
            int j = index;
            // read number until '#'
            while (j < string.length() && string.charAt(j) != '#') j++;
            if (j == string.length()) break; // malformed
            int len = Integer.parseInt(string.substring(index, j));
            int start = j + 1;
            int end = start + len;
            if (end > string.length()) break; // malformed
            myList.add(string.substring(start, end));
            index = end;
        }
        return myList;
    }
}
