import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 여기에 코드를 작성해주세요.
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();

            if (numToIndex.containsKey(num)) numToIndex.put(num, numToIndex.get(num)+1);
            else numToIndex.put(num, 1);
        }

        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();
            if (numToIndex.containsKey(num)) {
                System.out.print(numToIndex.get(num) + " ");
            } else System.out.print("0 ");
        }

        
    }
}