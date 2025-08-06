"""
构建树
给定一棵二叉树的前序遍历和中序遍历，请从中构建二叉树，返回二叉树的根节点，假设二叉树中没有重复的节点

判断是否为分治问题：
1. 问题分解: 将原问题分解成两个子问题，构建左子树，构建右子树，再加上一步操作，初始化根节点。
    对于每棵子树，仍然可以复用以上划分方法，将其划分成更小的子树
2. 子问题独立：左子树和右子树是相互独立的，他们之间没有交集。
3. 子问题的解可以合并：一旦得到左子树和有子树，就可以将他们连接到根节点，得到原问题的解
"""


class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int = 0):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


def dfs(
        preorder: list[int],
        inorder_map: dict[int, int],
        i: int,
        l: int,
        r: int,
) -> TreeNode | None:
    """构建二叉树：分治"""
    # 子树区间为空时终止
    if r - l < 0:
        return None
    # 初始化根节点
    root = TreeNode(preorder[i])
    # 查询 m ，从而划分左右子树
    m = inorder_map[preorder[i]]
    # 子问题：构建左子树
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    # 子问题：构建右子树
    # root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)
    root.right = dfs(preorder, inorder_map, i + 2, m + 1, r)
    # 返回根节点
    return root


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引的映射
    inorder_map = {val: i for i, val in enumerate(inorder)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root


"""Driver Code"""
if __name__ == "__main__":
    preorder = [3, 9, 2, 1, 7]
    inorder = [9, 3, 1, 2, 7]
    print(f"前序遍历 = {preorder}")
    print(f"中序遍历 = {inorder}")
    root = build_tree(preorder, inorder)
    print(root)
