
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        int i = 0;
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(':
                case '{':
                case '[':
                    stack.push(c);
                    break;
                case '}':
                case ')':
                case ']':
                    if (stack.isEmpty())
                        return false;
                    if (!((stack.peek() == '{' && c == '}') || (stack.peek() == '(' && c == ')') || (stack.peek() == '[' && c == ']')))
                        return false;
                    else stack.pop();
            }

        }
        if(!stack.isEmpty())
        return false;
        return true;
    }

    
}
