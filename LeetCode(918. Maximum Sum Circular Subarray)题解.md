# LeetCode(918. Maximum Sum Circular Subarray)题解

Given a **circular array** **C** of integers represented by `A`, find the maximum possible sum of a non-empty subarray of **C**.

Here, a *circular array* means the end of the array connects to the beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i < A.length`, and `C[i+A.length] = C[i]` when `i >= 0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most once.  (Formally, for a subarray `C[i], C[i+1], ..., C[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % A.length = k2 % A.length`.)

 

**Example 1:**

```
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```

**Example 2:**

```
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
```

**Example 3:**

```
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
```

**Example 4:**

```
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
```

**Example 5:**

```
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
```

 

**Note:**

1. `-30000 <= A[i] <= 30000`
2. `1 <= A.length <= 30000`

## 解题思路

给一个数组，求出其元素和最大的连续子数组之和，不同的是，这个数组是首尾相连的。

这个题我个人觉得有点麻烦，花了很多时间。如果数组不是首尾相连，直接使用Kadane算法就可以了。但是首尾相连就有点麻烦。这里有下面两个办法。

1：两组首位拼成2n长的数组，再求最大连续和。我一开始就这样做，中途要判断是否超过了长度，即出现重复，但是总是有一个case。
2：因为最大连续和可能在两组中间，求起来比较麻烦，但是转换一下这时最小连续和肯定在一个数组不会跨界，用总和-最小=最大和。（这个想法太精妙了，佩服！）



代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 88 ms, faster than 85.80% of C++ online submissions for Maximum Sum Circular Subarray.`

`Memory Usage: 12.5 MB, less than 100.00% of C++ online submissions for Maximum Sum Circular Subarray.`

```c++
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& A) {
        int a = A[0], b = A[0], maxA, len = A.size(), sum = A[0];
        for(int i=1; i<len; i++){
            b = max(A[i], b + A[i]);
            a = max(a, b);
            sum += A[i];
        }
        maxA = a;
        a = b = A[0];
        for(int i=1; i<len; i++){
            b = min(A[i], b + A[i]);
            a = min(a, b);
        }
        return sum == a ? maxA : max(sum - a, maxA);
    }
};
```

