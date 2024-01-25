import java.util.*;

public class Main {
    static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < m; i++) {
            int r = scan.nextInt() - 1;
            int c = scan.nextInt() - 1;
            int ans = comfort_state(grid, r, c);
            System.out.printf("%d\n", ans);
            grid[r][c] = 1;
        }
    }
    public static boolean in_range(int n, int r, int c) {
        return (((r >= 0) && (r < n)) && ((c >= 0) && (c < n)));
    }
    public static int comfort_state(int[][] grid, int r, int c) {
        int state = 0;
        int cnt = 0;
        int[] drs = new int[] {0, 1, 0, -1};
        int[] dcs = new int[] {1, 0, -1, 0};

        for (int i = 0; i < 4; i++) {
            int nr = r + drs[i];
            int nc = c + dcs[i];
            if ((in_range(grid.length, nr, nc)) && grid[nr][nc] == 1) {
                cnt += 1;
            }
        }
        if (cnt == 3) state = 1;
        return state;
    }
}