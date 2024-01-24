import java.util.*;

public class Main {
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scan.nextInt();
        int[][] grid = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = scan.nextInt();
             }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (count_one(n, grid, i, j) >= 3) ans += 1;
             }
        }
        // System.out.printf("%b\n", in_range(n, 0, 9));
        System.out.printf("%d\n", ans);


        
    }
    public static boolean in_range(int n, int x, int y) {
        return (((x >= 0) && (x < n)) && ((y >= 0) && (y < n)));
    }
    public static int count_one(int n, int[][] grid, int x, int y){
        int cnt = 0;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, -1, 0, 1};
        for (int i = 0; i < 4; i++) {
            int tx = x + dx[i];
            int ty = y + dy[i];
            // System.out.printf("%d %d %b ",tx, ty, in_range(grid.length, tx, ty));
            if (in_range(n, tx, ty) && grid[tx][ty] == 1) {
                cnt += 1;
            } 
        }
        //System.out.printf("%d\n", cnt);
        return cnt;
    }
}