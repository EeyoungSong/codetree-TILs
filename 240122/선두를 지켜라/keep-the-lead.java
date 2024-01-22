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
        count_outrun(array_a, array_b);
            
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
    public static void count_outrun(int[] array_a, int[] array_b) {
        int cnt = 0;
        String[] lead_array = new String[array_a[0]];

        String leader = "";
        if (array_a[1] > array_b[1]) {
            leader = "a";
        }
        else if (array_a[1] < array_b[1]) {
            leader = "b";
        }
        for (int i = 2; i < array_a[0]; i++) {
            String temp;
            if (array_a[i] > array_b[i]) {
                temp = "a";
            }
            else if (array_a[i] < array_b[i]) {
                temp = "b";
            }
            else {
                temp = "same";
            }
            if ((!temp.equals("same")) && (leader != temp)) {
                leader = temp;
                cnt += 1;
            }
        }
        System.out.printf("%d", cnt);
        
        
    }
}