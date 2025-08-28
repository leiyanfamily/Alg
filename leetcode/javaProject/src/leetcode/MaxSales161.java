package leetcode;

/**
 * 思路和算法

 * 这个分治方法类似于「线段树求解最长公共上升子序列问题」的 pushUp 操作。 也许读者还没有接触过线段树，没有关系，方法二的内容假设你没有任何线段树的基础。
 * 当然，如果读者有兴趣的话，推荐阅读线段树区间合并法解决多次询问的「区间最长连续上升序列问题」和「区间最大子段和问题」，还是非常有趣的。

 * 我们定义一个操作 get(a, l, r) 表示查询 a 序列 [l,r] 区间内的最大子段和，那么最终我们要求的答案就是 get(sales, 0, sales.size() - 1)。
 * 如何分治实现这个操作呢？对于一个区间 [l,r]，我们取 m=(l+r)/2，对区间 [l,m] 和 [m+1,r] 分治求解。当递归逐层深入直到区间长度缩小为 1 的时候，递归「开始回升」。
 *  这个时候我们考虑如何通过 [l,m] 区间的信息和 [m+1,r] 区间的信息合并成区间 [l,r] 的信息。最关键的两个问题是：
 * 我们要维护区间的哪些信息呢？
 * 我们如何合并这些信息呢？
 * 对于一个区间 [l,r]，我们可以维护四个量：

 * lSum 表示 [l,r] 内以 l 为左端点的最大子段和
 * rSum 表示 [l,r] 内以 r 为右端点的最大子段和
 * mSum 表示 [l,r] 内的最大子段和
 * iSum 表示 [l,r] 的区间和
 * 以下简称 [l,m] 为 [l,r] 的「左子区间」，[m+1,r] 为 [l,r] 的「右子区间」。
 * 我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 [l,r] 的信息）？对于长度为 1 的区间 [i,i]，四个量的值都和 sales[i] 相等。对于长度大于 1 的区间：

 * 首先最好维护的是 iSum，区间 [l,r] 的 iSum 就等于「左子区间」的 iSum 加上「右子区间」的 iSum。
 * 对于 [l,r] 的 lSum，存在两种可能，它要么等于「左子区间」的 lSum，要么等于「左子区间」的 iSum 加上「右子区间」的 lSum，二者取大。
 * 对于 [l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
 * 当计算好上面的三个量之后，就很好计算 [l,r] 的 mSum 了。我们可以考虑 [l,r] 的 mSum 对应的区间是否跨越 m——它可能不跨越 m，
 * 也就是说 [l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；它也可能跨越 m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。
 * 这样问题就得到了解决。
 */


public class MaxSales161 {

    public static class Status {
        public int lSum, rSum, mSum, iSum;

        public Status(int lSum, int rSum, int mSum, int iSum) {
            this.lSum = lSum;
            this.rSum = rSum;
            this.mSum = mSum;
            this.iSum = iSum;
        }
    }

    public int maxSales(int[] sales) {
        return getInfo(sales, 0, sales.length - 1).mSum;
    }

    public Status getInfo(int[] a, int l, int r) {
        if (l == r) {
            return new Status(a[l], a[l], a[l], a[l]);
        }
        int m = (l + r) >> 1;
        Status lSub = getInfo(a, l, m);
        Status rSub = getInfo(a, m + 1, r);
        return pushUp(lSub, rSub);
    }

    public Status pushUp(Status l, Status r) {
        int iSum = l.iSum + r.iSum;
        int lSum = Math.max(l.lSum, l.iSum + r.lSum);
        int rSum = Math.max(r.rSum, r.iSum + l.rSum);
        int mSum = Math.max(Math.max(l.mSum, r.mSum), l.rSum + r.lSum);
        return new Status(lSum, rSum, mSum, iSum);
    }

    /**
     前缀和
     计算区间 [L, R]的和（闭区间）：
     sum(L, R) = prefix[R+1] - prefix[L]。
     示例：
     数组 arr = [1, 2, 3, 4]→ 前缀和 prefix = [0, 1, 3, 6, 10]。
     查询 [1, 3]的和：prefix[4] - prefix[1] = 10 - 1 = 9（即 2+3+4=9）。
     prefix第一个未固定元素0。
     **/
    public int maxSubArray(int[] nums) {
        int min = 0;  // 当前最小和
        int ans = Integer.MIN_VALUE;  // 当前最大子序列和
        int num = 0;  // 到当前元素的所有元素之和
        for(int i = 0 ; i < nums.length ; i ++){
            num += nums[i];
            ans = Math.max(ans , num - min);  // min是指到i为止，前面元素连续多天的最小和，num - min，表示最小和之后的元素到i之间的和
            if(num<min){
                min = num;
            }
        }
        return ans;
    }
}
