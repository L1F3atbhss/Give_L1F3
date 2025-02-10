public class RC1 {
    public static void main(String[] args) {
        System.out.println("Welcome to RC1");
        
        int[] RC1 = {1, 7, 19, 23, 31};
        System.out.println(RC1[0]);
        //int[][][] RC3 = { {1, 7, 19, 23, 31},  {1, 7, 19, 23, 31}, {1, 7, 19, 23, 31}};

        int[][] RC2 = { {1, 7, 19, 23, 31}, {2, 8, 20, 24, 32} }; 
        System.out.println(RC2[1][1]);

        System.out.println("RC:" + "RC" + RC1[0] + RC2[1][1]);



        int Var = 1;
        int Var1 = 0;
        int Var2 = 2;
        int[] RC3 = {1, 7, 19, 23, 31};
        System.out.println(RC3[Var]);
        System.out.println("RC:" + "RC" + RC1[Var] + "A" + RC2[Var1][Var2] + "G83N");

    }
}
