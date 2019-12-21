# LeetCode(\673. Number of Longest Increasing Subsequence)题解

Given an unsorted array of integers, find the number of longest increasing subsequence.

**Example 1:**

```
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
```



**Example 2:**

```
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
```



**Note:** Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

## 解题思路

给一个整数序列S，找出最长子序列的条数。

这个题与找最长子序列长度其实差不多，可以使用DP来做。定义两个数组A和B，其中A\[i\]表示以i位置结尾的最大子序列长度，B\[i\]表示在i位置结尾的最大子序列个数。那么填充完这个两个数组之后，直接遍历AB数组，选取A中最大值对应位置在B上的值即可。接下来就填充AB数组。

- 首先是初始化，都初始化为1。
- 从i=1开始向上遍历，判断i位置之前的位置j，如果S\[i\]<=S\[j\]直接跳过。
- S\[i\]>S\[j\]，如果A\[i\]<A\[j\]+1说明最大长度需要更新，A\[i\] = A\[j\]+1，同时B\[i\] = B\[j\]；如果A\[i\]==A\[j\]+1说明最大长度不需要更新，但个数需要更新B\[i\] += B\[j\]；A\[i\]>A\[j\]+1说明都不需要更新，跳过即可。

代码如下，假设数组长度N，则时间复杂度O(N2)，空间复杂度O(N)。

`Runtime: 40 ms, faster than 73.56% of C++ online submissions for Number of Longest Increasing Subsequence.`

`Memory Usage: 9 MB, less than 100.00% of C++ online submissions for Number of Longest Increasing Subsequence.`

```c++
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int len = nums.size(), ret = 0, max_size = 1;
        vector<int> A(len, 1), B(len, 1);
        
        for (int i=1; i<len; i++) {
            for (int j=0; j<i; j++) {
                if (nums[i] <= nums[j]) continue;
                if (A[i] == A[j] + 1) B[i] += B[j];
                else if (A[i] < A[j] + 1) {
                    A[i] = A[j] + 1;
                    B[i] = B[j];
                }
            }
            max_size = max(max_size, A[i]);
        }
        
        for (int i=0; i<len; i++) {
            if (A[i] == max_size) ret += B[i];
        } 
        return ret;
    }
};
```

BitBrave，2019-12-21