import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner scan = new Scanner(System.in);
        scan.useDelimiter("-");
        int m = scan.nextInt();
        int d = scan.nextInt();
        int y = scan.nextInt();
        System.out.printf("%d.%d.%d", y, m, d);        
    }
}