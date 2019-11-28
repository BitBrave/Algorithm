# LeetCode(954. Array of Doubled Pairs)题解

Given an array of integers `A` with even length, return `true` if and only if it is possible to reorder it such that `A[2 * i + 1] = 2 * A[2 * i]` for every `0 <= i < len(A) / 2`.

**Example 1:**

```
Input: [3,1,3,6]
Output: false
```

**Example 2:**

```
Input: [2,1,2,6]
Output: false
```

**Example 3:**

```
Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
```

**Example 4:**

```
Input: [1,2,4,16,8,4]
Output: false
```

 

**Note:**

1. `0 <= A.length <= 30000`
2. `A.length` is even
3. `-100000 <= A[i] <= 100000`

## 解题思路

给一个偶数个元素的数组，判断其是否能组成一个有如下规则的数组：每个偶数位置的元素都是前面一个奇数位置元素的两倍，如果可以就返回True，否则False。

这个题可以使用Map或者字典解决。使用一个字典记录数组每个元素出现的元素。然后对索引值即不同的元素进行排序，小的在前面。这样查看第一个元素，因为最小的，所以只能找放在奇数位置，然后查看是否存在对应到额偶数位置的元素值，如果不存在算法就结束了。如果存在就判断这个元素值是不是比最小的值多，如果少的话表示不够配对，算法也结束返回False。反之就将这个元素值的个数减去最小值的个数，同时更新字典。这时候等于最小值已经配对完成了且只能这样配对，而接下来的问题和初始问题一致，只是问题规模变小了。因此按照这种方法就可以判断数组是否符合要求，如果走到最后都没有不能配对，算法就返回True。

因为要建立字典和排序，使用python方便一些。代码如下，时间复杂度O(nlogn)，空间复杂度O(n)。

`Runtime: 628 ms, faster than 96.71% of Python3 online submissions for Array of Doubled Pairs.`

`Memory Usage: 15.1 MB, less than 50.00% of Python3 online submissions for Array of Doubled Pairs.`

```python
from  collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A = [abs(a) for a in A]
        C = Counter(A)
        L = sorted(C)
        for l in L:
            if C[l] == 0: continue # 可注释掉
            if C.get(2*l, 0) < C[l]: return False
            C[2*l] -= C[l]
            
        return True
```

BitBrave，2019-11-28