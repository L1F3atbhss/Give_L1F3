import java.time.LocalTime;

public class Test {
    public static void main(String[] args) {

        LocalTime now = LocalTime.now();
        //int minutes = now.getMinute();
        int seconds = now.getSecond();
        //int[][] AR = {{1,2,3},{3,4,2}};
        //int var = 1;
        int SV = 0;

        System.out.println("Seconds: " + seconds);

        if (seconds < 10) {
            SV = 1;
        } else if (seconds < 20) {
            SV = 2;
        } else if (seconds < 30) {
            SV = 3;
        } else if (seconds < 40) {
            SV = 4;
        } else if (seconds < 50) {
            SV = 5;
        } else {
            SV = 6;
        }

        System.out.println("SV: " + SV);
    }
}