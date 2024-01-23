import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int N, K, P, T;
        N = scan.nextInt();
        K = scan.nextInt();
        P = scan.nextInt();
        T = scan.nextInt();
        int[][] input_array = new int[T][3];

        for (int i = 0; i < T; i++) {
            int t, x, y;
            t = scan.nextInt();
            x = scan.nextInt()-1;
            y = scan.nextInt()-1;
            input_array[i][0] = t;
            input_array[i][1] = x;
            input_array[i][2] = y;
        }
        
        Arrays.sort(input_array, (o1, o2) -> {
            return o1[0] - o2[0];
        });

        // print_2d_array(input_array);

        int[] confection_able = new int[N];
        int[] confected = new int[N];
        confected[P-1] = 1;

        for (int i = 0; i < T; i++) {
            int t = input_array[i][0];
            int x = input_array[i][1];
            int y = input_array[i][2];
            // System.out.printf("%d %d %d   ", t, x, y);
            if ((confected[x] == 1) && (confection_able[x] < K)) {
                if(confected[y] == 1) confection_able[y]++;
                confected[y] = 1;
                confection_able[x]++;
                
            }
            else if ((confected[y] == 1) && (confection_able[y] < K)) {
                if (confected[x] == 1) confection_able[x]++;
                confected[x] = 1;
                confection_able[y]++;
            }
            // System.out.printf("전염가능성 : ");
            // print_array(confection_able);
            // System.out.printf("전염된 : ");
            // print_array(confected);
        }
        // print_array(confection_able);
        print_array(confected);

        


    }
    void confection(int[] array) {

    }

    public static void print_2d_array(int[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.printf("%d ", array[i][j]);
            }
            System.out.printf(" ");
        }
        
    }
    public static void print_array(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.printf("%d", array[i]);
        }
        System.out.printf("\n");
    }
}