package leetcode;

import java.util.Arrays;
import java.util.HashMap;

class InventoryManagement158 {
//    public static int inventoryManagement(int[] stock) {
//        HashMap<Integer, Integer> stockMap = new HashMap<>();
//        for (int i: stock){
//            if (!stockMap.containsKey(i)){
//                stockMap.put(i, 1);
//                if (stockMap.get(i) > stock.length / 2){
//                    return i;
//                }
//                continue;
//            }
//            int itemCount = stockMap.get(i);
//            stockMap.put(i, itemCount + 1);
//            if (stockMap.get(i) > stock.length / 2){
//                return i;
//            }
//        }
//        return -1;
//    }

    public static int inventoryManagement(int[] stock) {
        return selectMajorityItem(stock, 0, stock.length - 1);
    }

    public static int selectMajorityItem(int[] nums, int left, int right){
        if (left == right){
            return nums[left];
        }

        int mid = (left + right) / 2;
        int le = selectMajorityItem(nums, left, mid);
        int ri = selectMajorityItem(nums, mid + 1, right);

        if (le == ri){
            return nums[le];
        }
        int[] part = Arrays.copyOfRange(nums, left, right + 1);
        int left_count = (int) Arrays.stream(part).filter(num -> num == le).count();
        int right_count = (int) Arrays.stream(part).filter(num -> num == ri).count();

        return left_count >= right_count ? le : ri;
    }


    public static void main(String[] args){
        int[] stock = {1, 2, 3, 2, 2, 2, 2, 1, 1};
        System.out.println(inventoryManagement(stock));
    }
}