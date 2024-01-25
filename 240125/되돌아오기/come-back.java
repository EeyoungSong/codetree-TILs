import java.util.*;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scan.nextInt();
        int x = 0;
        int y = 0;
        int[] dxs = {1, 0, -1, 0};
        int[] dys = {0, -1, 0, 1};

        int ans = -1;
        int time = 1;
        for (int i = 0; i < n; i++) {
            char d = scan.next().charAt(0);
            int dis = scan.nextInt();
            int dir_num = allot_dir(d);
            for (int j = 0; j < dis; j++) {
                x = x + dxs[dir_num];
                y = y + dys[dir_num];
                // System.out.printf("%d %d \n", x, y);
                if ((ans == -1) && (x == 0) && (y == 0)) {
                    ans = time;
                }
                time += 1;
            }
        }
        System.out.printf("%d", ans);

        // 여기에 코드를 작성해주세요.
    }
    public static int allot_dir(char d) {
        int dir_num;
        if (d == 'E') {
            dir_num = 0;
        }
        else if (d == 'S') {
            dir_num = 1;
        }
        else if (d == 'W') {
            dir_num = 2;
        }
        else {
            dir_num = 3;
        }
        return dir_num;
    }
}