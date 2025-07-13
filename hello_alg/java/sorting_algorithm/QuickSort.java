package sorting_algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QuickSort {
    public Integer partition(Integer[] nums, int left, int right) {
        int i = left, j = right;
        while (i < j) {
            while (i < j && nums[j] >= nums[left]) {
                j--;
            }
            while (i < j && nums[i] <= nums[right]) {
                i++;
            }
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        int temp = nums[left];
        nums[left] = nums[i];
        nums[i] = temp;
        return i;
    }

    public void quickSort(Integer[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int pivot = this.partition(nums, left, right);
        quickSort(nums, left, pivot - 1);
        quickSort(nums, pivot + 1, right);
    }

}
