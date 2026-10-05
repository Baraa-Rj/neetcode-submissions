class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        for (String token : tokens) {
            if (isOperator(token)) {
                int b = Integer.parseInt(stack.pop());
                int a = Integer.parseInt(stack.pop());
                stack.push(String.valueOf(apply(token, a, b)));
            } else {
                stack.push(token);
            }
        }
        return Integer.parseInt(stack.pop());
    }

    public boolean isOperator(String s) {
        return s.length() == 1 && "+-*/".indexOf(s.charAt(0)) != -1;
    }

    public int apply(String token, int a, int b) {
        return switch (token) {
            case "+" -> a + b;
            case "-" -> a - b;
            case "*" -> a * b;
            case "/" -> a / b;
            default -> 0;
        };
    }
}
