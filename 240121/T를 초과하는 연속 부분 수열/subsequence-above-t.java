import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] array = new int[n];
        int t = scan.nextInt();
        int cnt = 0;
        int max_num = 0;
        for (int i = 0; i < n; i++) {
            int num = scan.nextInt();
            array[i] = num;
            if (array[i] <= t) {
                    cnt = 0;
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