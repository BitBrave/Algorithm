# LeetCode(898. Bitwise ORs of Subarrays)题解

We have an array `A` of non-negative integers.

For every (contiguous) subarray `B = [A[i], A[i+1], ..., A[j]]` (with `i <= j`), we take the bitwise OR of all the elements in `B`, obtaining a result `A[i] | A[i+1] | ... | A[j]`.

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

**Example 1:**

```
Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
```

**Example 2:**

```
Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
```

**Example 3:**

```
Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.
```

 

**Note:**

1. `1 <= A.length <= 50000`
2. `0 <= A[i] <= 10^9`

## 解题思路

给定一个数组，求出所有的连续子数组内的元素相或的值的个数。

这个题很容易超时，要用到很多小trick。

做法如下，首先是从头到尾遍历数组，对于当前遍历到的元素，使用set记录之前的连续子数组的集合数目，这样会自动去重，从而减少遍历，虽然理论上的时间复杂度也是O(n2)，但是如果不这样做是无论如何都无法通过的。

其次是使用unorder_set，这个在C++内相比于set更快，因为不支持内部排序。

这里推荐一个bolg

<https://www.cnblogs.com/grandyang/p/10982534.html>

代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

`Runtime: 1488 ms, faster than 30.60% of C++ online submissions for Bitwise ORs of Subarrays.`

`Memory Usage: 314.3 MB, less than 33.33% of C++ online submissions for Bitwise ORs of Subarrays.`

```c++
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& A) {
        unordered_set<int> S, cur;
        int len = A.size();
        S.insert(A[0]);
        cur.insert(A[0]);
        for(int i=1; i<len; i++){
            if(A[i] == A[i-1]) continue;
            unordered_set<int> ts = {A[i]};
            for(int a : cur) ts.insert(a | A[i]);
            cur = ts;
            S.insert(cur.begin(), cur.end());
        }
        return S.size();
    }
};
```

BitBrave，2019-10-30