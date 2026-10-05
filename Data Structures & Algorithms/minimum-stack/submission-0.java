class MinStack {
    private LinkedList<Integer> stack;
    private LinkedList<Integer> minStack;

    public MinStack() {
        stack = new LinkedList<>();
        minStack = new LinkedList<>();
    }

    public void push(int val) {
        stack.addFirst(val);
        if (minStack.isEmpty() || val <= minStack.getFirst()) {
            minStack.addFirst(val);
        } else {
            // repeat current min so stacks stay aligned
            minStack.addFirst(minStack.getFirst());
        }
    }

    public void pop() {
        stack.removeFirst();
        minStack.removeFirst();
    }

    public int top() {
        return stack.getFirst();
    }

    public int getMin() {
        return minStack.getFirst();
    }
}
