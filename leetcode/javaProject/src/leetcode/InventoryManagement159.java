package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

class InventoryManagement159 {

    public static int[] inventoryManagement(int[] stock, int cnt) {
        int[] allStock = mergeSorted(stock, 0, stock.length - 1);
        return Arrays.copyOfRange(allStock, 0, cnt);
    }

    public static int[] mergeSorted(int[] nums, int left, int right) {
        if (left >= right) {
            return new int[0];
        }
        int mid = (left + right) / 2;
        mergeSorted(nums, left, mid);
        mergeSorted(nums, mid+1, right);
        merge(nums, left, mid, right);
        return nums;
    }

    public static void merge(int[] nums, int left, int mid, int right) {
        ArrayList<Integer> result  = new ArrayList<>();
        int i  = left;
        int j = mid + 1;
        while (i <= mid && j <= right){
            if (nums[i] < nums[j]) {
                result.add(nums[i]);
                i++;
            } else {
                result.add(nums[j]);
                j++;
            }
        }
        if (i <= mid){
            int[] leftPart = Arrays.copyOfRange(nums, i, mid + 1);
            ArrayList<Integer> leftP = Arrays.stream(leftPart).boxed().collect(Collectors.toCollection(ArrayList::new));
            result.addAll(leftP);
        }
        if (j <= right){
            int[] rightPart = Arrays.copyOfRange(nums, j, right + 1);
            ArrayList<Integer> rightP = Arrays.stream(rightPart).boxed().collect(Collectors.toCollection(ArrayList::new));
            result.addAll(rightP);
        }
        int index = 0;
        for (int item: result){
            nums[left + index] = item;
            index++;
        }
    }

    public static void main(String[] args){
        int[] stock = {1, 2, 3, 2, 2, 2, 2, 1, 1};
        System.out.println(Arrays.toString(inventoryManagement(stock, 2)));
    }
}