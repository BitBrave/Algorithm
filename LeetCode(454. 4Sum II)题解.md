# LeetCode(454. 4Sum II)题解

Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

**Example:**

```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

## 解题思路

给出四个数组，每个数组等长，从四个数组内各选出一个数，求这四个数想加为0的个数。

这个题如果直接使用最简单的办法，可以一一遍历所有的组合形式，总的时间复杂度为O(n4)。这肯定是不可接收的，这里可以用空间换时间，使用Map记录其中两个数组内所有的相加组合，然后再遍历另外两个数组的元素相加，查看相加之和和0的差值是否在Map内，如果在就表示找到一个排列，否则就表示无法配对。

代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

`Memory Usage: 34.8 MB, less than 8.33% of Python3 online submissions for 4Sum II.`

`Runtime: 320 ms, faster than 52.64% of Python3 online submissions for 4Sum II.`

```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ret = 0
        Dic = {}
        for a in A:
            for b in B:
                if a+b not in Dic: Dic[a+b] = 1
                else: Dic[a+b] += 1
        for c in C:
            for d in D:
                ret += Dic.get(-d-c, 0)
        return ret
```

更加简洁的写法如下。

```python
from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        Dic = Counter([a+b for a in A for b in B])
        return sum([Dic[-c-d] for c in C for d in D if -c-d in Dic])
```

但是这个方法肯定不是最优的，但是我在网上也没有找到更优的解法了。留待以后再看吧。

BitBrave，2019-10-29