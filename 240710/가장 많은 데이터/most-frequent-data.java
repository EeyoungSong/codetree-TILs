import java.util.Collections;
import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        HashMap<String, Integer> m = new HashMap<>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String color = sc.next();
            if (m.containsKey(color)) m.put(color, m.get(color)+1);
            else m.put(color, 1);
        }
        System.out.print(Collections.max(m.values()));
    }
}