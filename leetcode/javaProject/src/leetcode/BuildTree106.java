package leetcode;
/*
106. 从中序与后序遍历序列构造二叉树
中等

给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
      3
    /   \
  9      20
        /  \
      15    7

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]


提示:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历
 */


import java.util.Arrays;
import java.util.HashMap;

public class BuildTree106 {

    private HashMap<Integer, Integer> inorderIndexMap;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return myBuildTree(inorder, 0, inorder.length - 1,
                postorder, 0, postorder.length - 1);
    }

    /*
     inorder:  [[左子树], root, [右子树]]
     postorder:[[左子树], [右子树], root]
     */
    public TreeNode myBuildTree(int[] inorder, int inStart, int inEnd,
                                int[] postorder, int postStart, int postEnd) {
        if (inStart > inEnd) return null;

        int root = postorder[postEnd];
        int rootInIndex = inorderIndexMap.get(root);
        int leftSize = rootInIndex - inStart;

        TreeNode rootNode = new TreeNode(root);
        TreeNode leftNode = myBuildTree(inorder, inStart, rootInIndex - 1, postorder, postStart, postStart + leftSize - 1);
        TreeNode rightNode = myBuildTree(inorder, rootInIndex + 1, inEnd, postorder, postStart + leftSize, postEnd - 1);
        rootNode.left = leftNode;
        rootNode.right = rightNode;
        return rootNode;
    }


//    public TreeNode buildTree(int[] inorder, int[] postorder) {
//        if (inorder.length == 0) {
//            return null;
//        }
//        if (inorder.length == 1) {
//            return new TreeNode(inorder[0]);
//        }
//        int len = postorder.length;
//        int root = postorder[len-1];
//        int inRootIndex = getIndex(inorder, root);
//        int postRootIndex = getIndex(postorder, root);
//
//        TreeNode rootNode = new TreeNode(root);
//        int[] leftInOrder = Arrays.copyOfRange(inorder, 0, inRootIndex);
//        int[] leftPostOrder = Arrays.copyOfRange(postorder, 0, inRootIndex);
//        TreeNode leftNode = buildTree(leftInOrder, leftPostOrder);
//
//        int[] rightInOrder = Arrays.copyOfRange(inorder, inRootIndex+1, postRootIndex+1);
//        int[] rightPostOrder = Arrays.copyOfRange(postorder, inRootIndex, postRootIndex);
//        TreeNode rightNode = buildTree(rightInOrder, rightPostOrder);
//
//        rootNode.left = leftNode;
//        rootNode.right = rightNode;
//        return rootNode;
//
//    }
//
//    public int getIndex(int[] nums, int target) {
//        for (int i = 0; i < nums.length;  i++) {
//            if (nums[i] == target) {
//                return i;
//            }
//        }
//        return -1;
//    }
}
