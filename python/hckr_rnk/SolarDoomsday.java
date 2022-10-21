import java.util.ArrayList;
import java.lang.Math;

public class SolarDoomsday {
    public static void main(String[] args) {
        int[] arr = solution(15324);
        for (int el : arr) {
            System.out.print(el + " ");
        }
        System.out.println();
    }

    public static int[] solution(int num) {
        ArrayList<Integer> intArr = new ArrayList<Integer>();
        int a = num;
        int panel;
        while (a > 0) {
            panel = (int)Math.sqrt(a);
            panel *= panel;
            intArr.add(panel);
            a -= panel;
        }
        int[] arr = intArr.stream().mapToInt(i->i).toArray();

        return arr;
    }
}