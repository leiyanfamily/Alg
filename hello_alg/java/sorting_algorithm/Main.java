package sorting_algorithm;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Integer[] nums = {5, 4, 6, 3, 8, 2, 0, 0, 7};
        QuickSort quickSort = new QuickSort();
        quickSort.quickSort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }
}
