# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 13:44
# @Author  : ward
# @File    : run.py


l = [1, 3, 4, 5]

for i in range(len(l) - 1):
    for j in range(len(l) - i - 1):
        if l[j] <= l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(l)


def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        a = nums[i]
        b = target - a
        if b in d:
            return [d[b], i]
        else:
            d[a] = i


res = two_sum(l, 6)
print(res)


def func(data, left, right):
    temp = data[left]
    while left < right and data[right] >= temp:
        right -= 1
    data[left] = data[right]
    while left < right and data[left] <= temp:
        left += 1
    data[right] = data[left]
    data[left] = temp
    return left


def quick_sort(data, left, right):
    if left < right:
        mid = func(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


data = [3, 45, 67, 2, 45, 1]
quick_sort(data, 0, len(data) - 1)
print(data)


def two_sun_2(nums, target):
    d = {}
    for i, num in enumerate(nums):
        a = nums[i]
        b = target - a
        if b in d:
            return [d[b], i]
        else:
            d[a] = i


print(two_sun_2(data, 3))

# 100 到 200 之间素数
su_shu = []
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            break
        if i == j + 1:
            su_shu.append(i)
print(su_shu)


# fib

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


# g = fib(50)
# for i in range(50):
#     print("第" + str(i + 1) + "个值：", g.__next__())
