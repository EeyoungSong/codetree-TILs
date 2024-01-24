import java.util.*;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, -1, 0, 1};

        String command = scan.next();
        int n = command.length();
        
        int x = 0;
        int y = 0;
        int dir_num = 3;
        for (int i = 0; i < n; i++) {
            char d = command.charAt(i);
            // System.out.printf("%c", d); 
            if (d == 'F') {
                x = x + dx[dir_num];
                y = y + dy[dir_num];
            }
            else {
                dir_num = change_dir(dir_num, d);
            }
            // System.out.printf("%c %d %d\n",d, x, y);
        }
        System.out.printf("%d %d\n", x, y);

    }
    public static int change_dir(int dir_num, char d) {
        if (d == 'L') {
            dir_num = (dir_num - 1) % 4;
        }
        else {
            dir_num = (dir_num + 1) % 4;
        }
        return dir_num;
    }
}