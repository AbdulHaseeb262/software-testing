import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class ListManipulator {
    public static void processAndFilter(List<Integer> numbers) {
        System.out.println("Original list: " + numbers);
        Iterator<Integer> it = numbers.iterator();
        while (it.hasNext()) {
            Integer number = it.next(); // set breakpoint here
            if (number % 2 == 0) {
                it.remove();
                System.out.println("Removed: " + number);
            }
        }
        System.out.println("Final list: " + numbers);
    }

    public static void main(String[] args) {
        List<Integer> data = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
        processAndFilter(data);
    }
}