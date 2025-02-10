import java.time.LocalTime;

public class RC2 {
    public static void main(String[] args) {
        LocalTime now = LocalTime.now();
        int minutes = now.getMinute();
        int seconds = now.getSecond();

        // Ensure values stay within valid index ranges (0 or 1 for row, 0-2 for column)
        int Var = minutes % 2;  // Row index (0 or 1)
        int Var1 = seconds % 2;  // Row index (0 or 1)
        int Var2 = (minutes + seconds) % 3;  // Column index (0, 1, or 2)

        int[][] RC1 = {{1, 2, 3}, {4, 5, 6}};
        int[][] RC2 = {{7, 8, 9}, {10, 11, 12}};
        int[][] RC3 = {{13, 14, 15}, {16, 17, 18}};
        int[][] RC4 = {{19, 20, 21}, {22, 23, 24}};
        int[][] RC5 = {{25, 26, 27}, {28, 29, 30}};

        System.out.println("RC:" + "RC" + RC1[Var][Var2] + "A" + RC2[Var1][Var2] + "G" + RC3[Var][Var2] + "N" + RC4[Var][Var2] + RC5[Var][Var2]);
    }
}