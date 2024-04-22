import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner scan = new Scanner(System.in);
        String time = scan.next();
        String[] timearr = time.split(":");
        int hours = Integer.parseInt(timearr[0]) + 1;
        System.out.printf("%d:%s", hours, timearr[1]);
    }
    void printarr(String[] arr) {
        for (String elem : arr) {
            System.out.printf("%s ", elem);
        }
    }
}