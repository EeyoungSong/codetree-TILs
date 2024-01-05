import java.util.Scanner;

public class Main {
    public static final int MAX_R = 100;
    public static int[] Arr = new int[MAX_R + 1]; 
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int n;
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            for (int j = a; j < b+1; j++) {
                Arr[j] += 1;
            }

        }
        int max_num = 0;
        for (int i = 0; i < (MAX_R + 1); i++) {
            if (Arr[i] > max_num) {
                max_num = Arr[i];
            }
        }
        System.out.printf("%d\n", max_num);
    }
}