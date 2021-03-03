from random import Random
import random

# 冒泡排序
l = [1, 4, 5, 2, 9, 7, 3]
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):  # 我们每循环一次都会将最大的数推到最右边，所以需要将最右边排好的数拿走
        if l[j] > l[j + 1]:  # 前一个数与后一个数依次比较，直到将最大的数推到右边
            l[j], l[j + 1] = l[j + 1], l[j]
    # print(l)
print(l)


# 快排
def quick_sort(arr):
    if len(arr) > 1:
        qsort(arr, 0, len(arr) - 1)


def qsort(arr, start, end):
    base = arr[start]
    pl = start
    pr = end
    while pl < pr:
        while pl < pr and arr[pr] >= base:
            pr -= 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]
        while pl < pr and arr[pl] <= base:
            pl += 1
        if pl == pr:
            break
        else:
            arr[pl], arr[pr] = arr[pr], arr[pl]
    # now l == r
    if pl - 1 > start:
        qsort(arr, start, pl - 1)
    if pr + 1 < end:
        qsort(arr, pr + 1, end)


r = Random()
a = []
for i in range(20):
    a.append(r.randint(0, 100))

print(a)
quick_sort(a)
print(a)

# 堆排序
"""
理论知识：


　　二叉树：度不超过2的树（节点最多有两个叉）

　　满二叉树：一个二叉树，如果每一个层的节点数都达到最大值，则这个二叉树就是满二叉树。

　　完全二叉树：叶节点只能出现在最下层和次下层，并且最下面一层的节点都集中在该层最左边的若干位置的二叉树。

　　大顶堆：一颗完全二叉树，满足任一节点都比其孩子节点大。

　　小顶堆：一颗完全二叉树，满足任一节点都比其孩子节点小。


    
    建堆过程
    　　1.建立堆
    　　2.得到堆顶元素，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
    　　3.堆顶元素为第二大元素
    　　4.重复步骤3，知道堆变空

"""


def sift(li, low, high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:  # 情况2：i已经是最后一层了
        if j + 1 <= high and li[j + 1] > li[j]:  # 右孩子存在并且大于左孩子
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break  # 情况1：j位置比tmp小
    li[i] = tmp


def heap_sort(li):
    # 1.建堆
    n = len(li)
    for low in range(n // 2 - 1, -1, -1):
        sift(li, low, n - 1)
    # 2. 挨个输出 退休-棋子-调整 重复n次或n-1次
    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]
        sift(li, 0, high - 1)


li = list(range(100000))
random.shuffle(li)
heap_sort(li)

import heapq


# priority queue

# li = [5,7,9,8,4,1,6,2,3]
# heapq.heapify(li)
# heapq.heappush(li, 0)
# print(heapq.heappop(li))
#
# print(li)

# print(heapq.nlargest(5, [1,2,5,4,7,8,9,6,3]))


# 构建小顶堆跳转
def sift_s(li, low, higt):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= higt:  # 情况2：i已经是最后一层
        if j + 1 <= higt and li[j + 1] < li[j]:  # 右孩子存在并且小于左孩子
            j += 1
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break  # 情况1：j位置比tmp小
    li[i] = tmp


def top_k(li, k):
    heap = li[0:k]
    # 建堆
    for i in range(k // 2 - 1, -1, -1):
        sift_s(heap, i, k - 1)
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift_s(heap, 0, k - 1)
    # 挨个输出
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_s(heap, 0, i - 1)
    return heap


li = [0, 8, 6, 2, 4, 9, 1, 4, 6]
print(top_k(li, 3))


# 两数之和
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            a = nums[i]
            b = target - a
            if b in d:
                return [d[b], i]
            else:
                d[a] = i
