import java.util.Scanner;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int MAX_NUM = 1000000;
        int n = scan.nextInt();
        int m = scan.nextInt();

        int[] array_a = new int[MAX_NUM];
        int[] array_b = new int[MAX_NUM];

        array_a = record_num(n, array_a);
        array_b = record_num(m, array_b);

        int time_a = array_a[0];
        int time_b = array_b[0];

        int ans = -1;
        for (int i = 1; i < time_a; i++) {
            if (array_a[i] == array_b[i]) {
                ans = i;
                break;
            }
        }
        System.out.printf("%d\n", ans);



    }

    public static int[] record_num(int n, int[] array) {
        // Scanner scan = new Scanner(System.in);
        int time = 1;
        for (int i = 0; i < n; i++) {
            String d = scan.next();
            int t = scan.nextInt();
            for (int j = 0; j < t; j++) {
                if (d.equals("R")) {
                    array[time] = array[time - 1] + 1;
                }
                else {
                    array[time] = array[time - 1] - 1;
                }
                time += 1;
            }
        }
        array[0] = time;
        return array;
    }
}