
public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Car[] cars = new Car[n];
        for (int i = 0; i < n; i++) {
            cars[i] = new Car(position[i], speed[i]);
        }
        Arrays.sort(cars, (a, b) -> Integer.compare(b.position, a.position));
        int fleets =0;
        double minTime =0;
        for (Car car : cars) {
            double time = (double)(target - car.position) / car.speed;
            if(time>minTime){
                fleets++;
                minTime = time;
            }
            }
        return fleets;
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
