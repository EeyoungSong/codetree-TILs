import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String s = scan.next();
            arr.add(s);
        }
        Collections.sort(arr, new Comparator<String>() { //익
            @Override
            public int compare(String A, String B) {
                // 오름차순
            String ab = A + B;
            String ba = B + A;
            int isbig = ab.compareTo(ba);
            if (isbig < 0) {
                return 1;
                } else if (isbig > 0) {
                    return -1;
                } else {
                    return 0;
                }
            }       
        });
        // arr.sort(StringComparator());
        String answer = "";
        for (String s : arr) {
            answer += s;
        }
        System.out.print(answer);
    }
}