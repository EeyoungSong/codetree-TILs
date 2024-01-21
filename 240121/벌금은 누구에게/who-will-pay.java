import java.util.Scanner;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int n, m, k;
        n = scan.nextInt();
        m = scan.nextInt();
        k = scan.nextInt();

        int[] array = new int[n+1];
        int ans = -1;

        for (int i = 0; i < m; i++) {
            int s = scan.nextInt();
            array[s] += 1;
            if (array[s] >= k) {
                ans = s;
                break;
            }
        }
        System.out.printf("%d\n", ans);
    }
}