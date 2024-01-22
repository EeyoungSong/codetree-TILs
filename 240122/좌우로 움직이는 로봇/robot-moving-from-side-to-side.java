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

        int time_a = array_a[0];
        int time_b = array_b[0];
        if (time_a > time_b) {
            for (int i = 0; i < time_a; i++) {
                if (i >= time_b) array_b[i] = array_b[time_b-1];
            }
        }
        else {
            for (int i = 0; i < time_b; i++) {
                if (i >= time_a) array_a[i] = array_a[time_a-1];
            }
        }
        // print_arr(array_a, 0, array_b[0]);
        // print_arr(array_b, 0, array_b[0]);

        int cnt = 0;
        for (int i = 2; i < ((time_a > time_b) ? time_a : time_b); i++) {
            if ((array_a[i-1] != array_b[i-1]) && (array_a[i] == array_b[i])) {
                cnt += 1;
            } 
        }
        System.out.printf("%d", cnt);
        

        
        //count_outrun(array_a, array_b);
            
    }
    public static int[] record_moving(int n, int[] array) {
        int time = 1;
        for (int i = 0; i < n; i++) {
            int t = scan.nextInt();
            String d = scan.next();
            // System.out.printf("%d %d /", v, t);
            for (int j = 0; j < t; j++) {
                array[time] = array[time-1] + ((d.equals("R")) ? 1 : -1);
                time ++;
            }
        }
        array[0] = time;
        return array;
    }
    public static void print_arr(int[] arr, int a, int b) {
        for (int i = a; i < b; i++) {
            System.out.printf("%d ", arr[i]);
        }
        System.out.printf("\n");
    }
        
    
}