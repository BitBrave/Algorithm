# LeetCode(\1043. Partition Array for Maximum Sum)题解

Given an integer array `A`, you partition the array into (contiguous) subarrays of length at most `K`. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

**Example 1:**

```
Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
```

 

**Note:**

1. `1 <= K <= A.length <= 500`
2. `0 <= A[i] <= 10^6`

## 解题思路

给一个数组A和整数K，将A分为长度不超过K的若干个子数组，将每个子数组内的元素变为其中最大的元素值，然后求所有的子数组元素之和，问最终能得到的最大和为多少。

这个题可以使用DP解决，设定一个与A等长的数组dp，其中dp\[i\]表示A中0~i位置能得到的最大和，最终题目的答案就是dp\[A.size()-1\]。

状态转移方程是什么呢，因为子数组长度最多为K长度，因此我们考虑最后一个子数组的长度即可。即：

dp\[i\] = max(dp\[i-j\] + max(A\[i-j+1\], A\[i-j+2\], ..., A\[i\])),    j = 1,2, ..., K.

代码如下，时间复杂度O(nk), 空间复杂度O(n).

`Runtime: 16 ms, faster than 72.94% of C++ online submissions for Partition Array for Maximum Sum.`

`Memory Usage: 8.7 MB, less than 100.00% of C++ online submissions for Partition Array for Maximum Sum.`

```c++
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& A, int K) {
        int len = A.size();
        vector<int> dp(len + 1, 0);
        //dp[0] = A[0];
            
        for (int i=0; i<len; i++) {
            int m = A[i];
            dp[i+1] = dp[i] + m;
            for (int j=i; j>=0 and j>i-K; j--) {
                m = max(m, A[j]);
                dp[i+1] = max(dp[i+1], dp[j] + m * (i-j+1));
            }
        }
        return dp[len];
    }
};
```

BitBrave, 2020-01-05