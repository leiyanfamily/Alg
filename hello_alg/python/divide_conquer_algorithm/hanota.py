"""
汉诺塔问题
给定三根柱子，记为 A、B 和 C 。起始状态下，柱子 A 上套着
 个圆盘，它们从上到下按照从小到大的顺序排列。我们的任务是要把这
 个圆盘移到柱子 C 上，并保持它们的原有顺序不变（如图 12-10 所示）。在移动圆盘的过程中，需要遵守以下规则。

圆盘只能从一根柱子顶部拿出，从另一根柱子顶部放入。
每次只能移动一个圆盘。
小圆盘必须时刻位于大圆盘之上。

f(n):
将 n - 1 个圆盘借助 C 从 A 移至 B 。
将剩余 1 个圆盘从 A 直接移至 C 。
将 n - 1 个圆盘借助 A 从 B 移至 C 。
"""

def move(src: list, tar: list):
    """移动一个圆盘"""
    # 从src顶部拿一个圆盘
    pan = src.pop()
    # 放到tar的顶部
    tar.append(pan)


def dfs(i: int, src: list, buf: list, tar: list):
    """求解汉诺塔问题"""
    # 若 src 只剩下一个圆盘，则直接将其移动到tar
    if len(src) == 1:
        move(src, tar)
        return
    # 子问题 f(i-1): 将src顶部i-1个圆盘借助 tar 转移到buf上
    dfs(i - 1, src, tar, buf)
    # 子问题f(1): 将src剩余的最后一个圆盘移动到tar上
    move(src, tar)   # 子问题
    dfs(i - 1, buf, src, tar)


def solve_hanota(src: list, buf: list, tar: list):
    n = len(src)
    dfs(n, src, buf, tar)
