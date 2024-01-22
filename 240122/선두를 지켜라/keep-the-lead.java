import java.util.Scanner;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int MAX_NUM = 1000000;
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] array_a = new int[MAX_NUM + 1];
        int[] array_b = new int[MAX_NUM + 1];
        
        
        array_a = record_moving(n, array_a);
        array_b = record_moving(m, array_b);

        int cnt = 0;
        outrun(array_a, array_b);
            
    }
    public static int[] record_moving(int n, int[] array) {
        int time = 1;
        for (int i = 0; i < n; i++) {
            int v = scan.nextInt();
            int t = scan.nextInt();
            // System.out.printf("%d %d /", v, t);
            for (int j = 0; j < t; j++) {
                array[time] = array[time-1] + v;
                time ++;
            }
        }
        array[0] = time;
        return array;
    }
    public static void outrun(int[] array_a, int[] array_b) {
        int cnt = 0;
        String[] lead_array = new String[array_a[0]];

        for (int i = 0; i < array_a[0]; i++) {
            if (array_a[i] > array_b[i]) {
                lead_array[i] = "a";
            }
            else if (array_a[i] < array_b[i]) {
                lead_array[i] = "b";
            }
            else {
                lead_array[i] = "ab";
            }
        }
        String leader = "";
        for (int i = 1; i < array_a[0]; i++) {
            if ((lead_array[i] != "ab") && (lead_array[i] != leader)) {
                leader = lead_array[i];
                cnt += 1;
                // System.out.printf("%s", leader);
            }
        }
        System.out.printf("%d", cnt - 1 if cnt > 0);
    }
}