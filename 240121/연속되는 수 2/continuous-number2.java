import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] array = new int[n];
        int cnt = 1;
        int max_num = 0;
        for (int i = 0; i < n; i++) {
            int num = scan.nextInt();
            array[i] = num;
            if (i == 0 || array[i] != array[i-1]) {
                cnt = 1;
                // System.out.printf("%d", array[i]);
            }
            else {
                cnt += 1;
            }
            if (cnt > max_num) {
            max_num = cnt;
        }
        
        }
        System.out.printf("%d\n", max_num);
    }
}