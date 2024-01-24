import java.util.*;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, -1, 0, 1};
        
        Map<String, String> dir_dic = new HashMap<String, String>();
        dir_dic.put("E", "0");
        dir_dic.put("S", "1");
        dir_dic.put("W", "2");
        dir_dic.put("N", "3");

        int n = scan.nextInt();

        int x = 0;
        int y = 0;
        for (int i = 0; i < n; i++) {
            String d = scan.next();
            int dis = scan.nextInt();
            int dir_num = Integer.parseInt(dir_dic.get(d));
            x = x + dx[dir_num] * dis;
            y = y + dy[dir_num] * dis;
        }

        System.out.printf("%d %d", x, y);
    }
}