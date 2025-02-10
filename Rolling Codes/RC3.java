import java.time.LocalTime;
public class RC3 {
    public static void main(String[] args) {
        LocalTime now = LocalTime.now();
        int minutes = now.getMinute();
        int seconds = now.getSecond();

        // Ensure values stay within valid index ranges
        int Var1 = minutes % 2;  // Row index (0 or 1)
        int Var2 = seconds % 2;  // Row index (0 or 1)

        int[] RC1 = {1, 7, 2};
        int[] RC2 = {89, 23, 15};
        int[] RC3 = {27, 48, 28};
        int[] RC4 = {37, 47, 38};
        int[] RC5 = {25, 26, 49};

        // Generate "random" letters using time-based values
        char letter1 = (char) ('A' + (minutes % 26));
        char letter2 = (char) ('A' + (seconds % 26));
        char letter3 = (char) ('A' + ((minutes + seconds) % 26));

        // System output: RC:
        System.out.println("RC:RC" + RC1[Var1] + letter1 + RC2[Var1] + letter2 + RC3[Var2] + letter3 + RC4[Var1] + RC5[Var2]);
    }
}