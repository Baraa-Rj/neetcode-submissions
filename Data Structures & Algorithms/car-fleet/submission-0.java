
public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Car[] cars = new Car[n];
        for (int i = 0; i < n; i++) {
            cars[i] = new Car(position[i], speed[i]);
        }
        // Sort by starting position descending (closest to target first)
        Arrays.sort(cars, (a, b) -> Integer.compare(b.position, a.position));

        Deque<Double> stack = new ArrayDeque<>();
        for (Car car : cars) {
            double time = (double)(target - car.position) / car.speed;
            // If stack is empty or this car cannot catch up to fleet ahead → new fleet
            if (stack.isEmpty() || time > stack.peek()) {
                stack.push(time);
            }
            // else: this car catches up to fleet ahead → merges, do nothing
        }
        return stack.size();
    }

    private static class Car {
        int position;
        int speed;
        Car(int p, int s) {
            position = p;
            speed = s;
        }
    }
}
