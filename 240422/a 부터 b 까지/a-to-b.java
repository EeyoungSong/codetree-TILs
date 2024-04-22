import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int i = a;
        while (i <= b) {
            System.out.printf("%d ", i);
            if (i % 2 != 0) i *= 2;
            else i += 3;
        }
    }
}