import java.time.LocalTime;

public class RC5 {
    public static void main(String[] args) {
        LocalTime now = LocalTime.now();
        int minutes = now.getMinute();
        int seconds = now.getSecond();

        int Var1 = seconds % 9;
        int Var2 = seconds % 9;
        int Var3 = seconds % 9;
        int Var4 = seconds % 9;
        int Var5 = seconds % 9;
        int Var6 = seconds % 9;
        int Var7 = seconds % 9;
        int Var8 = seconds % 9;
        int Var9 = seconds % 9;

        int VarA = seconds % 26;
        int VarB = seconds % 26;
        int VarC = seconds % 26;

        int[] RC1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC7 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC8 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        int[] RC9 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};

        String[] L1 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        String[] L2 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        String[] L3 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        
        System.out.println("RC:" + "RC" + RC1[Var1] + L1[VarA] + RC2[Var2] + RC3[Var3] + L2[VarB] + RC4[Var4] + RC5[Var5] + L3[VarC] + RC6[Var6] + RC7[Var7] + RC8[Var8] + RC9[Var9]);
        //System.out.println("RC:RC1A23B45C6789");
        System.out.println(Var1 + 1);
    }
}