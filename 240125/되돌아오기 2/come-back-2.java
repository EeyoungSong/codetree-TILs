import java.util.*;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        String command = scan.next(); 
        int n = command.length();
        int x = 0;
        int y = 0;
        int[] dxs = {1, 0, -1, 0};
        int[] dys = {0, -1, 0, 1};

        int dir_num = 3;

        int ans = -1;
        int time = 1;
        for (int i = 0; i < n; i++) {
            char d = command.charAt(i);
            if (d != 'F') {
                dir_num = allot_dir(dir_num, d);
            }
            else {
                x = x + dxs[dir_num];
                y = y + dys[dir_num];
            }
            // System.out.printf("%d %d \n", x, y);
            if ((ans == -1) && (x == 0) && (y == 0)) {
                ans = time;
            }
            time += 1;
            // System.out.printf("%d\n", ans);
        }
        System.out.printf("%d", ans);

        // 여기에 코드를 작성해주세요.
    }
    public static int allot_dir(int dir_num, char d) {
        if (d == 'R') {
            dir_num = (dir_num + 1) % 4;
        }
        else if (d == 'L') {
            dir_num = (((dir_num - 1) % 4) >= 0) ? ((dir_num - 1) % 4) : 4 + ((dir_num - 1) % 4);
        }
        // System.out.printf("%d\n", dir_num);
        return dir_num;
    }
}