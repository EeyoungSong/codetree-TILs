import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> m = new HashMap<>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String c = sc.next();
            
            if (c.equals("add")) {
                Integer k = sc.nextInt();
                Integer v = sc.nextInt();
                m.put(k, v);
            } else if (c.equals("find")) {
                Integer k = sc.nextInt();
                System.out.println(m.containsKey(k) ? m.get(k):"None");
            } else {
                Integer k = sc.nextInt();
                m.remove(k);
            }
        }
    }
}