import java.util.Scanner;

public class Main {
    public static final int OFFSET = 100;
    public static final int MAX_NUM = 200;
    public static int[][] array = new int[MAX_NUM + 1][MAX_NUM + 1];
    public static Scanner scan = new Scanner(System.in);
    public static boolean color = true;

    public static void main(String[] args) {
        int n = scan.nextInt();
        int ans;
        for (int i = 0; i < n; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();
            int d = scan.nextInt();
            for (int j = a; j < c; j++) {
                for (int k = b; k < d; k++) {
                    if (color) {
                        array[j + OFFSET][k + OFFSET] = 1;
                    } else {
                        array[j + OFFSET][k + OFFSET] = 2;
                    }
                }
            }
            color = switching(color);
        }
        System.out.println(count(array));
    }

    public static boolean switching(boolean color) {
        return !color;
    }

    public static int count(int[][] array) {
        int ans = 0;
        for (int i = 0; i < MAX_NUM + 1; i++) {
            for (int j = 0; j < MAX_NUM + 1; j++) {
                if (array[i][j] == 2) {
                    ans++;
                }
            }
        }
        return ans;
    }
}