package leetcode;

public class Main {
    public static void main(String[] args) {


        // 161 连续天数的最高销售额
//        int[] sales = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
//        System.out.println(new MaxSales161().maxSales(sales));

        // 0402
//        int[] nums = {-10,-3,0,5,9};
//        SortedArrayToBST0402 bst = new SortedArrayToBST0402();
//        TreeNode node = bst.sortedArrayToBST(nums);
//        System.out.println(node);

        // 106
        int[] inorder = {9,3,15,20,7};
        int[] postorder = {9,15,7,20,3};
        BuildTree106 buildTree106 = new BuildTree106();
        TreeNode node = buildTree106.buildTree(inorder, postorder);
        System.out.println(node);
    }
}
