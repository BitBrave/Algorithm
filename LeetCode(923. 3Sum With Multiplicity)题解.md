# LeetCode(923. 3Sum With Multiplicity)题解

Given an integer array `A`, and an integer `target`, return the number of tuples `i, j, k`  such that `i < j < k` and `A[i] + A[j] + A[k] == target`.

**As the answer can be very large, return it modulo 10^9 + 7**.

 

**Example 1:**

```
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
```

**Example 2:**

```
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
```

 

**Note:**

1. `3 <= A.length <= 3000`
2. `0 <= A[i] <= 100`
3. `0 <= target <= 300`

## 解题思路

给一个数组，数组中有重复元素，现在要求找出三个不同位置的元素（值可以一样），其和为一个固定值target。问有多少个这样的组合。

这个题很明显就是使用双指针法，将数组升序排序，然后从左到右遍历一个元素，选定一个元素后，从其右边维护一个双指针，如果相加的和大于目标值则右指针左移，如果小于目标值则左指针右移。这里因为有重复元素，所以可以用一个字典记录重复元素出现的次数，而排序的就只排序不同的元素即可。

代码如下，时间复杂度O(n2)，空间复杂度O(n)。

`Runtime: 68 ms, faster than 99.06% of Python3 online submissions for 3Sum With Multiplicity.`

`Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 3Sum With Multiplicity.`

```python
from collections import Counter
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ret = 0
        dicA = Counter(A)
        uA = sorted(list(dicA))
        l, r, size, mod = 0, 0, len(uA), pow(10, 9) + 7
        for i in range(size):
            l, r = i, size - 1
            s = target - uA[i]
            while l <= r:
                if uA[l] + uA[r] > s: r -= 1 
                elif uA[l] + uA[r] < s: l += 1
                elif i != l and l != r: ret = (ret + dicA[uA[i]]*dicA[uA[l]]*dicA[uA[r]]) % mod; l += 1; r -= 1
                elif i == l and l != r: ret = (ret + dicA[uA[i]]*(dicA[uA[i]]-1)*dicA[uA[r]]/2) % mod; l += 1; r -= 1
                elif i != l and l == r: ret = (ret + dicA[uA[i]]*dicA[uA[r]]*(dicA[uA[r]]-1)/2) % mod; l += 1; r -= 1
                else: ret = (ret + dicA[uA[i]]*(dicA[uA[i]]-1)*(dicA[uA[i]]-2)/6) % mod; l += 1; r -= 1
        return int(ret)
```

BitBrave，2019-11-19