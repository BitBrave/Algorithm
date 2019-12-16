# LeetCode(\1186. Maximum Subarray Sum with One Deletion)题解

Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be **non-empty** after deleting one element.

 

**Example 1:**

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
```

**Example 2:**

```
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
```

**Example 3:**

```
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
```

 

**Constraints:**

- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

## 解题思路

从数组中最多可以删除一个元素，然后选取最大连续子树组，返回其和。

如果不删除元素，就是一个最简单的最大连续子数组和而已。如果可以删除一个，最笨的办法就是一次删除一个数，然后求剩下的最大连续子数组和，这样时间复杂度O(n2)，我试了试会超时。

其实本题可以使用DP，从左到右遍历给定的数组，用两个数组分别记录包括当前元素在内的最大连续子数组之和，一个记录删除了一个元素的结果，一个记录不删除元素的结果。最后在这个过程中随时更新ret 即可。

代码如下，时间复杂度O(n)，空间复杂度O(n)，但是观察数组，发现状态转移至用到了相邻的数据，所以只需要常量空间也可以完成，这样时间复杂度可为O(1).我懒得做。

`Runtime: 44 ms, faster than 61.61% of C++ online submissions for Maximum Subarray Sum with One Deletion.`

`Memory Usage: 15 MB, less than 100.00% of C++ online submissions for Maximum Subarray Sum with One Deletion.`

```c++
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int len = arr.size(), ret = arr[0];
        
        vector<int> D0(len, arr[0]), D1(len, arr[0]);
        
        for (int i=1; i<len; i++) {
            D0[i] = max(D0[i-1]+arr[i], arr[i]);
            D1[i] = max(D1[i-1]+arr[i], arr[i]);
            D1[i] = max(D1[i], D0[i-1]);
            ret = max(ret, max(D0[i], D1[i]));
        }
        return ret;
    }
};
```

BitBrave, 2019-12-16